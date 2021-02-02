import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("08_input.txt") as f:
    content = f.readlines()

code_length = 0
mem_length = 0
for line in content:
  l = line
  code_length += len(l)
  l = re.sub('^"', "", l)
  l = re.sub('"$', "", l)
  l = re.sub('\\\\"', '"', l)
  l = re.sub('\\\\\\\\', '\\\\', l)
  replace_hex = 1
  while replace_hex == 1:
    match = re.search('\\\\x([abcdefABCDEF0123456789][abcdefABCDEF0123456789])', l)
    if match:
      rep_str = '\\\\x' + match.group(1)
      rep_char = chr(int(match.group(1), 16))
      #if (int(match.group(1), 16)) < 33:
      if rep_char.isspace():
        rep_char = "X"
      else:
        rep_char = "X"
      if rep_char == '\\':
        rep_char = '\\\\'
      l = re.sub(rep_str, rep_char, l)
    else:
      replace_hex = 0
  mem_length += len(l)


print "Part A: " + str(code_length - mem_length)

