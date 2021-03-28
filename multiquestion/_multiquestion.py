#
#  Program to convert questions in YAML format to Moodle XML
#
#  yaml_to_moodle Copyright (c) 2021 Carlos Pardo
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#


import re
import os
import codecs
import base64

import yaml
import jinja2
from PIL import Image


def main():
   """Main program"""
   output_path = '.'
   
   db = Database()
   yaml_files = [yaml for yaml in os.listdir('.') if yaml[-5:].lower() == '.yaml']
   for yaml_file in yaml_files:
      print('\nFile: %s' % yaml_file)
      db.read_yaml(yaml_file)
      output_file = os.path.join(output_path, os.path.splitext(yaml_file)[0] + '.xml')
      if is_newer(yaml_file, output_file):
         db.preprocess()
         data = db.render(template_xml_moodle)
         with codecs.open(output_file, 'w', encoding='utf-8') as fo:
            fo.write(data)
         print('   Output: %s' % output_file)


def is_newer(filename1, filename2):
   if os.path.exists(filename2):
      if os.path.getmtime(filename1) < os.path.getmtime(filename2):
         return False
   return True


class Database():
   
   def __init__(self):
      pass

   def read_yaml(self, filename, path='./'):
      """Read questions from Yaml file"""
      with codecs.open(os.path.join(path, filename), 'r', encoding='utf-8') as yamlfile:
         yamldata = yamlfile.read()
      yaml_files = list(yaml.load_all(yamldata, Loader=yaml.SafeLoader))
      self.header = yaml_files[0]
      self.questions = yaml_files[1]
      print('   Readed: %d questions' % len(self.questions))
      return len(self.questions)

   def test_questions(self):
      counter = 0
      correct_questions = []
      for question in self.questions:
         counter += 1
         question['error'] = False
         question['counter'] = counter

         if 'files' in question:
            files_base64 = [{'base64':'', 'ext':''}]
            for filename in question['files']:
               file_base64 = self.import_file(filename)
               files_base64.append(file_base64)
               if not file_base64:
                  question['error'] = True
            question['files'] = files_base64
         else:
            question['files'] = []
            
         if not 'type' in question:
            print('   Error: type not defined in question %d' % counter)
            question['error'] = True

         elif question['type'] == 'category':
            if not self.exists_member(question, 'category'):
               print('   Error: does not exists "category" in question %d' % counter)
               question['error'] = True

         elif question['type'] == 'description':
            self.test_questiontext(question, counter)

         elif question['type'] == 'essay':
            self.test_questiontext(question, counter)
            
         elif question['type'] == 'cloze':
            self.test_questiontext(question, counter)
            
         elif question['type'] == 'multichoice':
            self.test_questiontext(question, counter)
            self.test_questiontext(question, counter)

         else:
            print('   Error: type "%s" not recognized' % question['type'])
            question['error'] = True
         
   def test_questiontext(self, question, counter):
      if not self.exists_member(question, 'questiontext'):
         print('   Error: does not exists "questiontext" in question %d' % counter)
         question['error'] = True

   def test_multichoice_answers(self, question, counter):
      if not 'answers' in question or len(question['answers']) < 2:
         print('   Error: less than 2 answers in question %d' % counter)
         question['error'] = True
         return
      sum_fractions = 0
      for answer in question['answers']:
         if not 'fraction' in answer:
            print('   Error: answer without "fraction" in question %d' % counter)
            question['error'] = True
         else:
            sum_fractions += answer['fraction']
         if not 'text' in answer or not answer['text']:
            print('   Error: answer without "text" in question %d' % counter)
            question['error'] = True
      if abs(sum_fractions) > 1:
         print('   Warning: fractions not sums zero in question %d' % counter)

   def preprocess(self):
      self.test_questions()

      for question in self.questions:
         if question['error']:
            continue
         
         if 'questiontext' in question:
            self.render_text(question, 'questiontext', question['files'])

         if question['type'] == 'multichoice':
            for answer in question['answers']:
               self.render_text(answer, 'text', question['files'])

   def exists_member(self, dictionary, member):
      if not member in dictionary:
         return False
      if not dictionary[member]:
         return False
      return True

   def render_text(self, question, index, files):
      template = jinja2.Template(template_macros + question[index])
      data = template.render(files = files)
      question[index] = data
      
   def import_file(self, filename):
      if not os.path.exists(filename):
         print("   Error: File doesn't exists %s" % filename)
         return None
      with open(filename, 'rb') as fi:
         filedata = fi.read()
      ext = os.path.splitext(filename)[1][1:].lower()
      width, height = Image.open(filename).size if ext in image_types else (0, 0)
      return { 'base64': base64.b64encode(filedata).decode('ascii'),
               'ext': ext,
               'width': width,
               'height': height,
               }

   def render(self, template_text):
      template = jinja2.Template(template_text)
      data = template.render(header = self.header, questions = self.questions)
      return data

   def __repr__(self):
      data = yaml.dump_all([self.header, self.questions], encoding='utf-8')
      return data.decode('utf-8')


image_types = ['png', 'jpg', 'jpeg', 'gif']


template_macros = """
   {%- macro image(file, alt='', width=240, height=0) -%}
   <img src="data:image/{{ files[file]['ext'] }};base64,{{ files[file]['base64'] }}" alt="{{ alt }}"
   {%- if width > 0 %} width="{{ width }}" {% endif %}
   {%- if height > 0 %} height="{{ height }}" {% endif %}>
   {%- endmacro -%}
"""


template_xml_moodle = """{#- -#}
<?xml version="1.0" encoding="UTF-8"?>
<quiz>

{%- for question in questions if not question['error'] %}

   <!-- question: {{ '%04d' % question['counter'] }} -->

   {%- if question['type'] == 'category' %}
   <question type="category">
      <category> <text>$course$/top/{{ question['category'] }}</text> </category>
   </question>

   {%- elif question['type'] == 'description' %}
   <question type="description">
      <name> <text>{{ question['name'] }}</text> </name>
      <questiontext format="html">
      <text><![CDATA[{{ question['questiontext'] }}]]></text>
      </questiontext>
      <generalfeedback format="html"> <text></text> </generalfeedback>
      <defaultgrade>0.0000000</defaultgrade>
      <penalty>0.0000000</penalty>
      <hidden>0</hidden>
      <idnumber></idnumber>
   </question>

   {%- elif question['type'] == 'essay' %}
   <question type="essay">
      <name> <text>{{ question['name'] }}</text> </name>
      <questiontext format="html">
      <text><![CDATA[{{ question['questiontext'] }}]]></text>
      </questiontext>
      <generalfeedback format="html"> <text></text> </generalfeedback>
      <defaultgrade>{% if 'defaultgrade' in question %}{{ question['defaultgrade'] }}{% else %}1.0000000{% endif%}</defaultgrade>
      <penalty>0.0000000</penalty>
      <hidden>0</hidden>
      <responseformat>editor</responseformat>
      <responserequired>1</responserequired>
      <responsefieldlines>15</responsefieldlines>
      <attachments>{% if 'attachments' in question %}{{ question['attachments'] }}{% else %}0{% endif%}</attachments>
      <attachmentsrequired>{% if 'attachments' in question %}{{ question['attachments'] }}{% else %}0{% endif%}</attachmentsrequired>
      <graderinfo format="html"> <text></text> </graderinfo>
      <responsetemplate format="html"> <text></text> </responsetemplate>
   </question>

   {%- elif question['type'] == 'cloze' %}
   <question type="cloze">
      <name> <text>{{ question['name'] }}</text> </name>
      <questiontext format="html">
      <text><![CDATA[{{ question['questiontext'] }}]]></text>
      </questiontext>
      <generalfeedback format="html"> <text></text> </generalfeedback>
      <penalty>{% if 'penalty' in question %}{{ question['penalty'] }}{% else %}0{% endif%}</penalty>
      <hidden>0</hidden>
      <idnumber></idnumber>
   </question>

   {%- elif question['type'] == 'multichoice' %}
   <question type="multichoice">
      <name> <text>{{ question['name'] }}</text> </name>
      <questiontext format="html">
      <text><![CDATA[{{ question['questiontext'] }}]]></text>
      </questiontext>
      <generalfeedback format="html"> <text></text> </generalfeedback>
      <defaultgrade>1.0000000</defaultgrade>
      <penalty>{% if 'penalty' in question %}{{ question['penalty'] }}{% else %}0{% endif%}</penalty>
      <hidden>0</hidden>
      <single>true</single>
      <shuffleanswers>true</shuffleanswers>
      <answernumbering>abc</answernumbering>
      <correctfeedback format="html"> <text></text> </correctfeedback>
      <partiallycorrectfeedback format="html"> <text></text> </partiallycorrectfeedback>
      <incorrectfeedback format="html"> <text></text> </incorrectfeedback>
      {%- for answer in question['answers'] %}
      <answer fraction="{{ answer['fraction'] }}" format="html">
         <text><![CDATA[{{ answer['text'] }}]]></text>
         <feedback format="html"> <text>{{ answer['feedback'] }}</text> </feedback>
      </answer>
      {%- endfor %}
   </question>

   {%- endif %}
{%- endfor %}

</quiz>
"""


if __name__ == "__main__":
   main()
