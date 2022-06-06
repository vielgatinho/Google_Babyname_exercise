#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re


def sort_names(a):
  return a

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename, 'r')
  read = f.read()
  matchyear = re.search(r'\d+', filename)
  year = matchyear.group()
  matchname = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', read)
  
  dictnames_boys = {}
  dictnames_girls = {}
  for name in matchname:
    dictnames_boys[name[0]] = name[1]
    dictnames_girls[name[0]] = name[2]

  list = [year]
  list_boys = []
  list_girls = []
  for k, v in dictnames_boys.items():
    d = v + " " + k
    list_boys.append(d)
  for k, v in dictnames_girls.items():
    d = v + " " + k
    list_girls.append(d)
  list_boys.extend(list_girls)
  list_boys = sorted(list_boys, key=sort_names)
  list.extend(list_boys)
  return print(list)

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  if args[0] == '--baby1990.html':
    filename = 'baby1990.html'
    extract_names(filename)
  elif args[0] == '--baby1992.html':
    filename = 'baby1992.html'
    extract_names(filename)
  elif args[0] == '--baby1994.html':
    filename = 'baby1994.html'
    extract_names(filename)
  elif args[0] == '--baby1996.html':
    filename = 'baby1996.html'
    extract_names(filename)
  elif args[0] == '--baby1998.html':
    filename = 'baby1998.html'
    extract_names(filename)
  elif args[0] == '--baby2000.html':
    filename = 'baby2000.html'
    extract_names(filename)
  elif args[0] == '--baby2004.html':
    filename = 'baby2004.html'
    extract_names(filename)
  elif args[0] == '--baby2006.html':
    filename = 'baby2006.html'
    extract_names(filename)
  elif args[0] == '--baby2008.html':
    filename = 'baby2008.html'
    extract_names(filename)
  else: sys.exit(1)
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
