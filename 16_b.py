import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("16_input.txt") as f:
    content = f.readlines()

data = {}
data['children'] = 3
data['cats'] = 7
data['samoyeds'] = 2
data['pomeranians'] = 3
data['akitas'] = 0
data['vizslas'] = 0
data['goldfish'] = 5
data['trees'] = 3
data['cars'] = 2
data['perfumes'] = 1

for c in content:
  match = re.search('Sue ([^:]*): (.*)$', c)

  if match:
    sue = int(match.group(1))
    all = 1
    for pair in match.group(2).split(', '):
      key = pair.split(': ')[0]
      val = int(pair.split(': ')[1])
      #print key + ' -- ' + val
      if key == 'cats' or key == 'trees':
        if val <= data[key]:
          all = 0
      elif key == 'pomeranians' or key == 'goldfish':
        if val >= data[key]:
          all = 0
      elif data[key] != val:
        all = 0
        #print key + " -- " + str(val) + " != " + str(data[key]) + " : no match"
      else:
        dummy = 0
        #print key + " -- " + str(val) + " : MATCH!"
    if all == 1:
      print "Part A: Sue " + str(sue)


