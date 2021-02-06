import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("19_input.txt") as f:
    content = f.readlines()

s = ''

reps = []
def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString

for c in content:
  line = c.strip()
  match = re.search('([^ ]*) => (.*)', line)
  if match:
    pair = []
    pair.append(match.group(1))
    pair.append(match.group(2))
    reps.append(pair)
  else:
    s = line


results = []
for r in reps:
  num_matches = s.count(r[0])
  for i in range(0, num_matches):
    results.append(replacenth(s, r[0], r[1], i))

my_list = list(set(results))
print "Part A: " + str(len(my_list))
