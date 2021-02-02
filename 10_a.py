import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

input = '1113122113'


def process(i):
  ret = ''
  last = ''
  count = 0
  for c in i:
    out = 0
    count += 1
    if last == '':
      last = c
      continue
    if c != last:
      ret += str(count-1)
      ret += last
      last = c
      count = 1
      continue
    else:
      continue

  # Deal with last one
  ret += str(count)
  ret += c
  
  return ret

  
  


for x in range(0, 40):
  out = process(input)
  input = out

print "Part A: " + str(len(out))
for x in range(0, 10):
  out = process(input)
  input = out

print "Part B: " + str(len(out))


