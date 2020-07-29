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
    html = []
    with open(sys.argv[1]) as f1:
        data = f1.readlines()
        for line in data:
            line = line.split('\n')[0]
            words = line.split(' ')
            if words[0][0] == '#':
                open_tag = '<h' + str(len(words[0])) + '>'
                close_tag = '</h' + str(len(words[0])) + '>'
                html_line = open_tag + ' '.join(words[1:]) + close_tag
                """+ '\n'"""
                html.append(html_line)
            """else:
                html.append(line)"""
    try:
        with open(sys.argv[2], 'w') as f2:
            f2.writelines(html)
    except:
        pass
    exit(0)
