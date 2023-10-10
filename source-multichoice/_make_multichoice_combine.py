#
#  Program to convert several questionnaries in YAML format to
#  Docx document.
#
#  Questionary Copyright (c) 2021 Carlos Pardo
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

from _make_multichoice import Questionary
import random

multichoice_path = ''
build_path = 'build'
moodle_path = '../moodle'
html_path = '../docs'
images_path= '../images'

moodle_template = 'moodle-multichoice-template.xml'
json_template = 'json-template.json'
html_template = 'game-template.html'


projects = [
{
   'yaml_files': [
      'es-material-properties.yaml',
      'es-material-wood.yaml',
      'es-material-stone.yaml',
      'es-material-metals.yaml',
      'es-material-plastics.yaml',
      'es-material-tools-1.yaml',
      'es-material-tools-2.yaml',
      ],
   'filename_output': 'es-material',
   'yaml_category': 'Materiales y Herramientas',
   'yaml_title': 'Test global',   
   'max_questions': 35,
   'random_seed': 2022,
},

{
   'yaml_files': [
      'es-machines-simple.yaml',
      'es-machines-transmission1.yaml',
      'es-machines-transmission2.yaml',
      'es-machines-transmission3.yaml',
      'es-machines-transformation1.yaml',
      'es-machines-transformation2.yaml',
      ],
   'filename_output': 'es-machines',
   'yaml_category': 'Máquinas y Mecanismos',
   'yaml_title': 'Test global',   
   'max_questions': 35,
   'random_seed': 2022,
},

{
   'yaml_files': [
      'es-historia-tecnologia-prehistoria.yaml',
      'es-historia-tecnologia-antigua.yaml',
      'es-historia-tecnologia-moderna.yaml',
      'es-historia-tecnologia-revolucion-industrial.yaml',
      'es-historia-tecnologia-siglos-xx-xxi.yaml',
      ],
   'filename_output': 'es-historia-tecnologia',
   'yaml_category': 'Historia de la Tecnología',
   'yaml_title': 'Test global',   
   'max_questions': 35,
   'random_seed': 2022,
},

{
   'yaml_files': [
      'es-technology-objects-1.yaml',
      'es-technology-objects-2.yaml',
      'es-technology-objects-3.yaml',
      'es-technology-objects-4.yaml',
      ],
   'filename_output': 'es-technology-objects',
   'yaml_category': 'Los objetos técnicos',
   'yaml_title': 'Test global',   
   'max_questions': 35,
   'random_seed': 2022,
},

]
   

def main():
   """Main program"""
   for project in projects:

      # Read yaml files
      questionary = Questionary()
      all_questions = []
      Copyrights = []
      Licenses = []
      License_links = []
      for yaml_file in project['yaml_files']:
         print(yaml_file)
         questionary.read_yaml(yaml_file, path=multichoice_path)
         all_questions += questionary.questions
         Copyrights.append(questionary.header['Copyright'])
         Licenses.append(questionary.header['License'])
         License_links.append(questionary.header['License_link'])
      
      # Shuffle and select questions
      if project['random_seed']:
         random.seed(project['random_seed'])
      else:
         random.seed()
      random.shuffle(all_questions)

      # Write questions
      questionary = Questionary(overwrite=False)
      questionary.yaml_path = ''
      questionary.yaml_file = project['yaml_files'][0]
      questionary.filename = project['filename_output']
      questionary.header = {
         'Category': project['yaml_category'],
         'Title': project['yaml_title'],
         'Copyright': Copyrights[0],
         'License': Licenses[0],
         'License_link': License_links[0],
         'Show_max': project['max_questions'],
         }
      questionary.questions = all_questions
      questionary.docx_generate(path=build_path)
      questionary.moodle_generate(moodle_template, path=moodle_path)
      questionary.json_generate(json_template, path=html_path)
      questionary.html_generate(html_template, path=html_path)

      print()


if __name__ == "__main__":
   main()
