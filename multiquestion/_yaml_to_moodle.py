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

   db = Database()
   yaml_files = [yaml for yaml in os.listdir('.') if yaml[-5:].lower() == '.yaml']
   for yaml_file in yaml_files:
      print('\nFile: %s' % yaml_file)
      db.read_yaml(yaml_file)
      db.test_questions()
      db.preprocess()
      data = db.render(template_xml_moodle)
      output_file = os.path.splitext(yaml_file)[0] + '.xml'
      with codecs.open(output_file, 'w', encoding='utf-8') as fo:
         fo.write(data)


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
      return len(self.questions)

   def test_questions(self):
      counter = 0
      correct_questions = []
      for question in self.questions:
         counter += 1
         if not 'type' in question:
            print('Error: no type defined in question %d' % counter)
         elif question['type'] not in question_types:
            print('Error: type "%s" not recognized' % question['Type'])
         elif question['type'] in ['description', 'essay'] and not exists_member(question, 'questiontext'):
            print('Error: not "questiontext" in question %d' % counter)
         else:
            correct_questions.append(question)
      self.questions = correct_questions

   def exists_member(dictionary, member):
      if not member in dictionary:
         return False
      if not dictionary[member]:
         return False
      return True

   def preprocess(self):
      for question in self.questions:
         if 'files' in question:
            files_base64 = [{'base64':'', 'ext':''}]
            for filename in question['files']:
               files_base64.append(self.import_file(filename))
            question['files'] = files_base64

         if 'questiontext' in question:
            self.render_text(question, 'questiontext')

   def render_text(self, question, index):
      template = jinja2.Template(template_macros + question[index])
      files = []
      if 'files' in question:
         files = question['files']
      data = template.render(files = files)
      question[index] = data
      
   def import_file(self, filename):
      if not os.path.exists(filename):
         print("Error: File doesn't exists %s" % filename)
         return ""
      with open(filename, 'rb') as fi:
        data = fi.read()
      ext = os.path.splitext(filename)[1][1:]
      return {'base64': base64.b64encode(data).decode('ascii'), 'ext': ext}
      
   def render(self, template_text):
      template = jinja2.Template(template_text)
      data = template.render(header = self.header, questions = self.questions)
      return data

   def __repr__(self):
      data = yaml.dump_all([self.header, self.questions], encoding='utf-8')
      return data.decode('utf-8')


question_types = [
   'category',
   'description',
   'essay',
   ]


template_macros = """
   {%- macro image(file, alt='', width=240, height=0) %}
   <img src="data:image/{{ files[file]['ext'] }};base64,{{ files[file]['base64'] }}" alt="{{ alt }}"
   {%- if width %} width="{{ width }}" {% endif -%}
   {%- if height %} height="{{ height }}" {% endif %}>
   {% endmacro -%}
"""


template_xml_moodle = """{#- -#}
<?xml version="1.0" encoding="UTF-8"?>
<quiz>

{%- for question in questions %}

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

   {%- endif %}
{%- endfor %}

</quiz>
"""


if __name__ == "__main__":
   main()
