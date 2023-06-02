"""
Join several xml moodle files in one single xml file 
"""

import os
import re
import codecs

output_file =  'es-hardware-all.xml'
search_files = 'es-hardware.+\.xml'

def main():
    files = [f for f in os.listdir('.') if re.search(search_files, f)]
    
    data = []
    print('Join input files:')
    for file in files:
        print('  ', file)
        lines = read_xml(file)
        lines = strip_xml(lines)
        data = data + lines
    write_xml(output_file, data)
    print('\nOutput:\n  ', output_file)


def write_xml(outputfile, data):
    with codecs.open(outputfile, 'w', encoding='utf-8') as fo:
        fo.write('<?xml version="1.0" encoding="UTF-8"?>\n<quiz>\n')
        fo.write('\n'.join(data))
        fo.write('\n</quiz>')


def strip_xml(lines):
    while True:
        line = lines.pop(0)
        if re.search('<quiz>', line) or len(line) == 0:
            break

    while True:
        line = lines.pop(-1)
        if re.search('</quiz>', line) or len(line) == 0:
            break
        
    return lines


def read_xml(filename):
    lines = []
    with codecs.open(filename, 'r', encoding='utf-8') as fi:
        lines = fi.read()
    lines = lines.split('\n')
    return lines

main()
