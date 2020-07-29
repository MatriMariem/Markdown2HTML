#!/usr/bin/python3
"""
a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
"""
import sys
import os


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    elif not os.path.exists(sys.argv[1]):
        error = "Missing " + sys.argv[1] + '\n'
        sys.stderr.write(error)
        exit(1)
    with open(sys.argv[1]) as f1, open(sys.argv[2], 'w') as f2:
        data = f1.readlines()
        for line in data:
            line = line.split('\n')[0]
            words = line.split(' ')
            size = len(words[0])
            if words[0] == '#' * size :
                open_tag = '<h' + str(size) + '>'
                close_tag = '</h' + str(len(size) + '>'
                html_line = open_tag + line[size + 1]) + close_tag + '\n'
                f2.write(html_line)
            else:
                html.append(line)
    exit(0)
