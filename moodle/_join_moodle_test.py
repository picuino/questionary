"""
Join several xml moodle files in one single xml file 
"""

import os
import re
import codecs

join_moodle_jobs = [
    {'search_file': 'es-hardware.+\.xml',
     'output_file': 'es-hardware-all.xml'},
    {'search_file': 'es-software.+\.xml',
     'output_file': 'es-software-all.xml'},
]

def main():
    for moodle_job in join_moodle_jobs:
        search_file = moodle_job['search_file']
        output_file = moodle_job['output_file']
       
        files = [f for f in os.listdir('.') if re.search(search_file, f)]
       
        print('Join input files:')
        data = []
        for file in files:
            print('    ' + file)
            lines = read_xml(file)
            lines = strip_xml(lines)
            data = data + lines
        write_xml(output_file, data)
        print('    Output: ' + output_file)


def write_xml(outputfile, data):
    with codecs.open(outputfile, 'w', encoding='utf-8') as fo:
        fo.write('<?xml version="1.0" encoding="UTF-8"?>\n<quiz>\n')
        fo.write(''.join(data))
        fo.write('\n</quiz>')


def strip_xml(lines):
    while True:
        line = lines.pop(0)
        if re.search('<quiz>', line):
            break

    while True:
        line = lines.pop(-1)
        if re.search('</quiz>', line):
            break

    return lines


def read_xml(filename):
    lines = []
    with codecs.open(filename, 'r', encoding='utf-8') as fi:
        for line in fi:
            lines.append(line)
    return lines

main()
