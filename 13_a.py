import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("13_input.txt") as f:
    content = f.readlines()
data = []
peeps = []

for c in content:
  match = re.search('([a-zA-Z]*) would ([a-z]*) ([0-9]*) happiness units by sitting next to ([a-zA-Z]*)\.', c)
  if match:
    if match.group(1) not in peeps:
      peeps.append(match.group(1))
    d = []
    d.append(match.group(1))
    d.append(match.group(4))
    val = int(match.group(3))
    if match.group(2) == 'lose':
      val = 0 - val
    d.append(val)
    data.append(copy.deepcopy(d))

    
combos =  list(itertools.permutations(peeps, len(peeps)))

def calc(l):
  hap = 0
  for i in range(0, len(l)):
    cur = l[i]
    if i > 0:
      prev = l[i-1]
    else:
      prev = l[len(l)-1]
    if i < len(l)-1:
      next = l[i+1]
    else:
      next = l[0]
    for d in data:
      if d[0] == cur and d[1] == next:
        hap += d[2]
      if d[0] == cur and d[1] == prev:
        hap += d[2]
  return hap
 
max_hap = 0
max_combo = []
for c in combos:
  hap = calc(c)
  if hap > max_hap:
    max_hap = hap
    max_combo = copy.deepcopy(c)

print "Part A: " + str(max_hap)
