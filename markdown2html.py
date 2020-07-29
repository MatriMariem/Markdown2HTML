#!/usr/bin/python3
"""
a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
"""
import sys
import os

def handle_heading(line, words, size, f2):
    """ A function that handles headings """
    if words[0] == '#' * size and size in range(1, 7):
        open_tag = '<h' + str(size) + '>'
        close_tag = '</h' + str(size) + '>'
        html_line = open_tag + line[size + 1:] + close_tag + '\n'
        f2.write(html_line)

def open_ul(list_started, f2):
    """ write the opening ul tag if needed"""
    if not list_started:
        f2.write("<ul>\n")
    return True

def close_ul(list_started, f2):
    """ write the closing ul tag if needed"""
    if list_started:
        f2.write("</ul>\n")
    return False


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
        list_started = False
        for line in data:
            line = line.split('\n')[0]
            words = line.split(' ')
            size = len(words[0])
            if size > 0 and words[0][0] == '#':
                list_started = close_ul(list_started, f2)
                handle_heading(line, words, size, f2)
            elif line[0:2] == "- ":
                list_started = open_ul(list_started, f2)
                html_line = "<li>" + line[2:] + "</li>\n"
                f2.write(html_line)
            else:
                list_started = close_ul(list_started, f2)
                f2.write(line + '\n')
    exit(0)
