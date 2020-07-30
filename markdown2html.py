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

def open_list(list_type, list_started, f2):
    """ write the opening list tag if needed"""
    if not list_started:
        f2.write("<{}>\n".format(list_type))
    return True

def close_list(list_type, list_started, f2):
    """ write the closing list tag if needed"""
    if list_started:
        f2.write("</{}>\n".format(list_type))
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
        list_type = ''
        for line in data:
            line = line.split('\n')[0]
            words = line.split(' ')
            size = len(words[0])
            if size > 0 and words[0][0] == '#':
                list_started = close_list(list_type, list_started, f2)
                list_type = ''
                handle_heading(line, words, size, f2)
            elif line[0:2] == "- " or line[0:2] == "* ":
                if line[0:2] == "- ":
                    if list_type == 'ol':
                        list_started = close_list(list_type, list_started, f2)
                    list_type = 'ul'
                else:
                    if list_type == 'ul':
                        list_started = close_list(list_type, list_started, f2)
                    list_type = 'ol'
                list_started = open_list(list_type, list_started, f2)
                html_line = "<li>" + line[2:] + "</li>\n"
                f2.write(html_line)
                if line + '\n' == data[-1]:
                    list_started = close_list(list_type, list_started, f2)
            else:
                list_started = close_list(list_type, list_started, f2)
                list_type = ''
                if line + '\n' == data[0] or data[data.index(line + '\n') - 1] == '\n':
                    f2.write("<p>\n")
                elif data[data.index(line + '\n') - 1][:2] in ('- ', '* ', '# '):
                    f2.write("<p>\n")
                else:
                    f2.write("<br/>\n")
                f2.write("{}\n".format(line))
                if line + '\n' == data[-1] or data[data.index(line + '\n') + 1] == '\n':
                    f2.write("</p>\n")
                elif data[data.index(line + '\n') + 1][:2] in ('- ', '* ', '# '):
                    f2.write("</p>\n")
    exit(0)
