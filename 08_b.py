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
  l = re.sub('^"', "OOO", l)
  l = re.sub('"$', "CCC", l)
  l = re.sub('\\\\', 'XX', l)
  l = re.sub('"', 'QQ', l)
  mem_length += len(l)


print "Part B: " + str(mem_length - code_length)

