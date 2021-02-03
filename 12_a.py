import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("12_input.txt") as f:
    content = f.readlines()

result = ''
for line in content:
  for c in line:
    if c.isdigit() or c == '-':
      result += c
    else:
      result += ' '

nums = result.split(' ')

total = 0
for n in nums:
  if n != '':
    total += int(n)


print "Part A: " + str(total)
