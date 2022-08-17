import os
import codecs
import re
import base64
import xml.etree.ElementTree as ElementTree



def main():
    xml_filenames = ['electricidad_scanblor.xml']
    for xml_filename in xml_filenames:
        qst = Questions()
        qst.process(xml_filename)
        qst.write('output.yaml')

        
class Questions:

    def __init__(self):
        self.image_counter = 0
        self.image_files = []
        self.yaml_questions = []

    def __str__(self):
        string = '\n'.join(self.yaml_questions)
        return string
        
    def write(self, filename):
        data = self.__str__()
        with codecs.open(filename , 'w', encoding='utf-8') as fo:
            fo.write(data)

    def process(self, xml_filename):
        print('Processing: ' + xml_filename)
        self.yaml_questions = ['\nFilename: %s\n\n---\n\n' % xml_filename]
        tree = ElementTree.parse(xml_filename)
        root = tree.getroot()
        yaml_questions = []
        for question in root:
            if question.tag =='question':
                yaml = self.process_question(question)
                if yaml:
                    self.yaml_questions.append(yaml)
        return self.yaml_questions
    
    
    def process_question(self, question):
        self.image_counter = 0
        self.image_files = []
        if question.attrib['type'] == 'category':
            return self.process_category(question)
        elif question.attrib['type'] == 'description':
            return self.process_description(question)
        elif question.attrib['type'] == 'essay':
            return self.process_essay(question)
        elif question.attrib['type'] == 'multichoice':
            return self.process_multichoice(question)
        elif question.attrib['type'] == 'shortanswer':
            return self.process_shortanswer(question)
        elif question.attrib['type'] == 'matching':
            return self.process_matching(question)
        else:
            print('   Warning: unknown question type %s' % question.attrib['type'])
        return None
    
    
    def html_to_text(self, html):
        if html == None:
            html = ''
        html = re.sub('^!\[CDATA\[|\]\]$', '', html)
        html = re.sub('[\n\r]+', ' ', html)
        html = re.sub('<img [^>]+>', self.replace_images, html)
        html = re.sub('"', '\\"', html)
        return html
    
    
    def replace_images(self, match):
        img_str = match.group()
        if img_str[-2] != '/':
            img_str = img_str[:-1] + '/>'
        root = ElementTree.fromstring(img_str)
        if not 'src' in root.attrib:
            print('   Error: no attribute "src" in image')
            return ''
        if not 'alt' in root.attrib:
            root.attrib['alt'] = ''

        self.image_counter += 1
        self.image_files.append(re.sub('@@PLUGINFILE@@/', '', root.attrib['src']))
        yaml = "{{ image(file=%d, alt='%s'" % (self.image_counter, root.attrib['alt'])
        if 'width' in root.attrib:
            yaml = yaml + ', width=%s' % root.attrib['width']
        if 'height' in root.attrib:
            yaml = yaml + ', height=%s' % root.attrib['height']
        yaml = yaml + ') }}'
        return yaml


    def add_files(self):
        yaml = ''
        if self.image_files:
            yaml = '  files:\n'
            for image_file in self.image_files:
                if not 'http://' in image_file:
                    image_file = 'images/' + re.sub('/', '-', image_file)
                yaml = yaml + '    - %s\n' % image_file
        return yaml

    
    def process_multichoice(self, question):
        data = {
            'name': '',
            'questiontext': '',
            'defaultgrade': '',
            'penalty': '',
            'single': '',
            'answers': [],
        }
        
        for item in question:
            if item.tag == 'name':
                data['name'] = item[0].text
            elif item.tag == 'questiontext':
                data['questiontext'] = self.html_to_text(item[0].text)
            elif item.tag == 'defaultgrade':
                data['defaultgrade'] = item.text
            elif item.tag == 'penalty':
                data['penalty'] = item.text
            elif item.tag == 'single':
                data['single'] = item.text
            elif item.tag == 'answer':
                answer = {
                    'fraction': '',
                    'text': '',
                    'feedback': '',
                }
                answer['fraction'] = item.attrib['fraction']
                for subitem in item:
                    if subitem.tag == 'text':
                        answer['text'] = self.html_to_text(subitem.text)
                    if subitem.tag == 'feedback':
                        answer['feedback'] = self.html_to_text(subitem[0].text)
                    
                data['answers'].append(answer)
    
        yaml = '- type: multichoice\n'
        yaml = yaml + '  name: "' + data['name'] + '"\n'
        yaml = yaml + '  questiontext: "' + data['questiontext'] + '"\n'
        yaml = yaml + '  defaultgrade: ' + data['defaultgrade'] + '\n'
        yaml = yaml + '  penalty: ' + data['penalty'] + '\n'
        yaml = yaml + '  single: ' + data['single'] + '\n'
        yaml = yaml + '  answers: \n'
        for answer in data['answers']:
           yaml = yaml + '    - fraction: ' + answer['fraction'] + '\n'
           yaml = yaml + '      text: "' + answer['text'] + '"\n'
           yaml = yaml + '      feedback: ' + answer['feedback'] + '\n'

        yaml = yaml + self.add_files()
        return yaml
    
    
    def process_essay(self, question):
        data = {
            'name': '',
            'questiontext': '',
            'defaultgrade': '',
            'penalty': '',
            'attachments': '',
        }
        
        for item in question:
            if item.tag == 'name':
                data['name'] = item[0].text
            elif item.tag == 'questiontext':
                data['questiontext'] = self.html_to_text(item[0].text)
            elif item.tag == 'defaultgrade':
                data['defaultgrade'] = item.text
            elif item.tag == 'penalty':
                data['penalty'] = item.text
            elif item.tag == 'attachments':
                data['attachments'] = item.text
    
        yaml = '- type: essay\n'
        yaml = yaml + '  name: "' + data['name'] + '"\n'
        yaml = yaml + '  questiontext: "' + data['questiontext'] + '"\n'
        yaml = yaml + '  defaultgrade: ' + data['defaultgrade'] + '\n'
        yaml = yaml + '  penalty: ' + data['penalty'] + '\n'
        yaml = yaml + '  attachments: ' + data['attachments'] + '\n'

        yaml = yaml + self.add_files()
        return yaml
    
        
    def process_description(self, question):
        data = {
            'name': '',
            'questiontext': '',
        }
        
        for item in question:
            if item.tag == 'name':
                data['name'] = item[0].text
            elif item.tag == 'questiontext':
                data['questiontext'] = self.html_to_text(item[0].text)
    
        yaml = '- type: description\n'
        yaml = yaml + '  name: "' + data['name'] + '"\n'
        yaml = yaml + '  questiontext: "' + data['questiontext'] + '"\n'

        yaml = yaml + self.add_files()
        return yaml
    
        
    def process_category(self, question):
        category = ''
        for item in question:
            if item.tag == 'category':
                category = item[0].text
                category = re.sub('^\$course\$/', '', category)
        if category:
            yaml = '- type: category\n'
            yaml = yaml + '  category: "' + category + '"\n'
            return yaml        
        return None
    

    def process_shortanswer(self, question):
        data = {
            'name': '',
            'questiontext': '',
            'defaultgrade': '',
            'penalty': '',
            'attachments': '',
            'answers': [],
        }
        
        for item in question:
            if item.tag == 'name':
                data['name'] = item[0].text
            elif item.tag == 'questiontext':
                data['questiontext'] = self.html_to_text(item[0].text)
            elif item.tag == 'defaultgrade':
                data['defaultgrade'] = item.text
            elif item.tag == 'penalty':
                data['penalty'] = item.text
            elif item.tag == 'answer':
                answer = {
                    'fraction': '',
                    'text': '',
                    'feedback': '',
                }
                answer['fraction'] = item.attrib['fraction']
                for subitem in item:
                    if subitem.tag == 'text':
                       answer['text'] = self.html_to_text(subitem.text)
                    if subitem.tag == 'feedback':
                       answer['feedback'] = self.html_to_text(subitem[0].text)
                    
                data['answers'].append(answer)
    
        yaml = '- type: shortanswer\n'
        yaml = yaml + '  name: "' + data['name'] + '"\n'
        yaml = yaml + '  questiontext: "' + data['questiontext'] + '"\n'
        yaml = yaml + '  defaultgrade: ' + data['defaultgrade'] + '\n'
        yaml = yaml + '  penalty: ' + data['penalty'] + '\n'
        yaml = yaml + '  answers: \n'
        for answer in data['answers']:
            yaml = yaml + '    - fraction: ' + answer['fraction'] + '\n'
            yaml = yaml + '      text: "' + answer['text'] + '"\n'
            yaml = yaml + '      feedback: ' + answer['feedback'] + '\n'

        yaml = yaml + self.add_files()
        return yaml


    def process_matching(self, question):
        data = {
            'name': '',
            'questiontext': '',
            'defaultgrade': '',
            'penalty': '',
            'attachments': '',
            'subquestions': [],
        }
        
        for item in question:
            if item.tag == 'name':
                data['name'] = item[0].text
            elif item.tag == 'questiontext':
                data['questiontext'] = self.html_to_text(item[0].text)
            elif item.tag == 'defaultgrade':
                data['defaultgrade'] = item.text
            elif item.tag == 'penalty':
                data['penalty'] = item.text
            elif item.tag == 'subquestion':
                subquestion = {
                    'text': '',
                    'answer': '',
                }
                for subitem in item:
                    if subitem.tag == 'text':
                        subquestion['text'] = self.html_to_text(subitem.text)
                    if subitem.tag == 'answer':
                        subquestion['answer'] = self.html_to_text(subitem[0].text)
                data['subquestions'].append(subquestion)
    
        yaml = '- type: matching\n'
        yaml = yaml + '  name: "' + data['name'] + '"\n'
        yaml = yaml + '  questiontext: "' + data['questiontext'] + '"\n'
        yaml = yaml + '  defaultgrade: ' + data['defaultgrade'] + '\n'
        yaml = yaml + '  penalty: ' + data['penalty'] + '\n'
        yaml = yaml + '  subquestions: \n'
        for subquestion in data['subquestions']:
            yaml = yaml + '    - text: "' + subquestion['text'] + '"\n'
            yaml = yaml + '      answer: ' + subquestion['answer'] + '\n'

        yaml = yaml + self.add_files()
        return yaml
    

main()
