import os
import codecs
import re
import base64
import xml.etree.ElementTree as ET


def main():
    xml_filenames = [filename for filename in os.listdir('.') if filename[-4:].lower() == '.xml']
    for xml_filename in xml_filenames:
        xml = ET.parse(xml_filename)
        process(xml_filename, xml)
        

def extract_file(itemfile):
    path = 'images'
    name = itemfile.attrib['name']
    basename = re.sub(r'[/\\]', '-', itemfile.attrib['path'].strip('/\\'))
    if basename:
        name =  basename + '-' + name
    b64image = itemfile.text
    image = base64.b64decode(b64image)
    if not os.path.exists(os.path.join(path, name)):
        print('   ' + name)
        with open(os.path.join(path, name), 'wb') as outfile:
            outfile.write(image)    


def process_item(item):
    for subitem in item:
        if 'file' in subitem.tag:
            extract_file(subitem)
        process_item(subitem)

def process(xml_filename, xml):
    print('Processing: ' + xml_filename)
    root = xml.getroot()
    for question in root:
        process_item(question)


main()
