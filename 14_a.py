import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("14_input.txt") as f:
    content = f.readlines()

data = []
deer = []

for c in content:
  match = re.search('([a-zA-Z]*) can fly ([0-9]*) .* for ([0-9]*) seconds, but then must rest for ([0-9]*) seconds.', c)

  if match:
    deer.append(match.group(1))
    d = []
    d.append(match.group(1))       # 0 - Name
    d.append(int(match.group(2)))  # 1 - dist
    d.append(int(match.group(3)))  # 2 - fly time
    d.append(int(match.group(4)))  # 3 - rest time
    d.append(1)                    # 4 - 1= flying ; 0 = rest
    d.append(int(match.group(3)))  # 5 - timer
    d.append(0)                    # 6 - total dist



    data.append(copy.deepcopy(d))

   

for sec in range(0, 2504):
  for z in range(0, len(deer)):
    i = data[z]
    if i[4] == 1:
      i[6] += i[1]
      i[5] += -1
      if i[5] == 0:
        i[4] = 0
        i[5] = i[3]
        continue
    else:
      i[5] += -1
      if i[5] == 0:
        i[4] = 1
        i[5] = i[2]



max = 0
max_p = []
for p in data:
  if p[6] > max:
    max = p[6]
    max_p = p

print "Part A: " + str(max_p[6])
