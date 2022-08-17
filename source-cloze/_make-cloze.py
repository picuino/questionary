#
#  Program to convert cloze test from YAML format to html format and
#  Moodle XML format.
#
#  Tests de tecnología tipo cloze Copyright (c) 2022 Carlos Pardo
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
import random
import copy
import hashlib
import shutil

import yaml
import jinja2
from PIL import Image


def main():
   """Main program"""

   moodle_template = 'template-cloze-moodle.xml'
   html_template = 'template-cloze.html'

   build_path = 'build'
   html_path = '../docs'
   
   cloze = Cloze()

   # Process all yaml files of this directory
   questions_counter = DictCounter()
   yaml_files = [yaml for yaml in os.listdir('.') if yaml[-5:].lower() == '.yaml']
   for yaml_file in yaml_files:
      print('\nFile: %s' % yaml_file)
      questions = cloze.read_yaml(yaml_file, path='.')
      questions_counter.add(questions, yaml_file)
      cloze.html_generate(html_template, path=html_path)
      # cloze.moodle_generate(moodle_template, path=build_path)
   print('\nTotal questions= %s' % str(questions_counter))


class DictCounter():
   def __init__(self):
     self.counter = {}

   def add(self, count, name):
      prefix = re.split('[_ -]', name, maxsplit=1)[0]
      if prefix in self.counter:
         self.counter[prefix] += count
      else:
         self.counter[prefix] = count
      
   def __str__(self):
      return str(self.counter)



class Cloze():

   def __init__(self):
      self.templates_path = '.'
      self.hash_len = 20
      self.questions = []
      random.seed(1000)

   def read_yaml(self, filename, path='./'):
      """Read questions from Yaml file"""
      with codecs.open(os.path.join(path, filename), 'r', encoding='utf-8') as yamlfile:
         yamldata = yamlfile.read()
      yaml_files = list(yaml.load_all(yamldata, Loader=yaml.SafeLoader))
      self.header = yaml_files[0]
      self.questions = yaml_files[1]
      self.clean_questions()
      self.test_errors()
      self.extract_gaps()
      self.yaml_path = path
      self.yaml_file = filename
      self.filename = os.path.splitext(os.path.basename(filename))[0]
      self.add_image_info()
      self.add_title()
      print('   Readed %d questions' % len(self.questions))
      return len(self.questions)


   def write_file(self, filename, data):
      if os.path.exists(filename):
         with codecs.open(filename, 'r', encoding='utf-8') as infile:
            old_data = infile.read()
         if old_data == data:
            return
      print('   Writing: ' + filename)
      with codecs.open(filename, 'w', encoding='utf-8') as outfile:
         outfile.write(data)


   def not_key(self, dictionary, key):
      if key in dictionary and dictionary[key]:
         return False
      return True


   def clean_questions(self):
      for question in self.questions:
         new_text = question['Cloze'].strip('\n')
         if new_text != question['Cloze']:
            question['Cloze'] = new_text


   def test_errors(self):
      # Test errors in header
      if not 'Category' in self.header:
         print('   Warning: no Category value')
         self.header['Category'] = 'General'
      if not 'Title' in self.header:
         print('   Warning: no Title value')
         self.header['Title'] = 'No title available'
      if not 'Copyright' in self.header:
         print('   Warning: no Copyright value')
         self.header['Copyright'] = ''
      if not 'Show_max' in self.header:
         print('   Warning: no Show_max value')
         self.header['Show_max'] = 0

      # Test Cloze
      safe_questions = []
      for question in self.questions:
         if not question:
            print('   Error: question empty ')
            continue
         if not 'Cloze' in question:
            print('   Error: cloze question without text ' + str(question))
            continue
         safe_questions.append(question)

      self.questions = safe_questions


   def add_title(self):
      """Add Title to every question if does not exists"""
      for question in self.questions:
         if not 'Title' in question or not question['Title']:
            question['Title'] = question['Cloze']


   def extract_gaps(self):
      """Extract gaps from cloze text"""
      gap_pattern = re.compile('{[^}]*}')
      for question in self.questions:
         cloze = question['Cloze']
         match = gap_pattern.findall(cloze)
         gaps = []
         for gap in match:
            gap = gap.strip('{}')
            if '|' in gap:
               gap = re.split('\|', gap)
               print(gap)
            gaps.append(gap)
         question['Gaps'] = gaps
         
         new_cloze = gap_pattern.split(cloze + '.')
         cloze_gaps = []
         for i in range(len(new_cloze)-1):
            cloze_gaps = cloze_gaps + [new_cloze[i]] + ['{%d}' % i]
         cloze_gaps = cloze_gaps + [new_cloze[-1]]
         new_cloze = ''.join(cloze_gaps)
         new_cloze = new_cloze[:-1]
         question['Cloze'] = new_cloze


   def read_b64(self, filename):
      """Read image and returns data in ascii base64 format"""
      data = open(filename, 'rb').read()
      return base64.b64encode(data).decode('ascii')


   def hashname(self, filename):
      data = open(filename, 'rb').read()
      return hashlib.sha224(data).hexdigest()[:self.hash_len] + os.path.splitext(filename)[1]

   
   def add_image_info(self):
      """Read images from disk and add it several info and translations"""
      for question in self.questions:
         if 'Image' in question and question['Image']:
            imagedict = {}
            imagedict['filename'] = question['Image']
            if os.path.exists(imagedict['filename']):
               imagedict['hashname'] = self.hashname(imagedict['filename'])
               imagedict['path'] = os.path.dirname(imagedict['filename'])
               imagedict['mtime'] = os.path.getmtime(imagedict['filename'])
               imagedict['base64'] = self.read_b64(imagedict['filename'])
               width, height = Image.open(imagedict['filename']).size
               imagedict['width'] = width
               imagedict['height'] = height
               if not 'Image_width' in question:
                  imagedict['display_width'] = width
               else:
                  imagedict['display_width'] = question['Image_width']
                  del question['Image_width']
               if imagedict['display_width'] > 800:
                  print('   Warning image file too large. Display width=%3d  File=%s' % (imagedict['display_width'], imagedict['filename']))
               question['Image'] = imagedict                  
            else:
               print('Image file does not exists: ' + imagedict['filename'])
               question['Image'] = {}
         else:
            question['Image'] = {}
   
   
   def jinja_template(self, template_file):
      """Load jinja environment and template file.
         return a jinja template object"""
      templateLoader = jinja2.FileSystemLoader(searchpath=self.templates_path)
      templateEnv = jinja2.Environment(loader=templateLoader)
      self.template = templateEnv.get_template(template_file)
      
   
   def moodle_generate(self, template_file, path='./'):
      """Genera los cuestionarios en formato Moodle xml a partir de las
         cuestiones. Se genera un archivo por cada bloque de cuestiones"""
      xml_filename = os.path.join(path, self.filename + '.xml')
      self.jinja_template(template_file)
      xml_data = self.template.render(questions = self.questions, header = self.header, filename = self.filename)
      self.write_file(xml_filename, xml_data)
   
   
   def suffle_choices(self, question):
       choices = copy.copy(question['Choices'])
       random.shuffle(choices)
       return choices
   
   
   def html_generate(self, template_file, path='./'):
      """Genera los archivos html para jugar con las cuestiones."""
      html_filename = os.path.join(path, self.filename + '.html')
      self.jinja_template(template_file)
      html_data = self.template.render(filename=self.filename, header=self.header, questions = self.questions)
      self.write_file(html_filename, html_data)


if __name__ == "__main__":
   main()
