import os
import codecs
import re


translate_dict = [
    ]


def translate(path, filename):
   with codecs.open(os.path.join(path, filename), 'r', encoding='utf-8') as data_file:
      data = data_file.read()
   data2 = data + ''
   for pattern, repl in translate_dict:
      data2 = re.sub(pattern, repl, data2)
   if data2 == data:
      return
   with codecs.open(filename, 'w', encoding='utf-8') as data_file:
      data_file.write(data2)
   print('Translated: ', filename)

   
def main():
   for file1, file2 in translate_dict:
      if not os.path.exists(os.path.join('../../images', file1)):
         print('Not exists: ', file1)
         
   for filename in os.listdir('..'):
      if filename[-5:].lower() != '.yaml':
         continue
      translate('..', filename)    


if __name__ == "__main__":
   main()
