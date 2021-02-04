import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("15_input.txt") as f:
    content = f.readlines()

data = []
ing = []

for c in content:
  match = re.search('([a-zA-Z]*): capacity ([-0-9]*), durability ([-0-9]*), flavor ([-0-9]*), texture ([-0-9]*), calories ([-0-9]*)', c)

  if match:
    ing.append(match.group(1))
    d = []
    d.append(match.group(1))       # 0 - Name
    d.append(int(match.group(2)))  # 1 - capacity
    d.append(int(match.group(3)))  # 2 - durability
    d.append(int(match.group(4)))  # 3 - flavor
    d.append(int(match.group(5)))  # 4 - texture
    d.append(int(match.group(6)))  # 5 - calories

    data.append(copy.deepcopy(d))

amount = []
for i in ing:
  amount.append(0)

def score(l):
  s = 1
  for a in range(1, 5):
    prop = 0
    for z in range(0, len(l)):
      prop += data[z][a] * l[z]
    if prop < 0:
      prop = 0
    s *= prop
  return s

def cals(l):
  s = 1
  for a in range(5, 6):
    prop = 0
    for z in range(0, len(l)):
      prop += data[z][a] * l[z]
    if prop < 0:
      prop = 0
    s *= prop
  return s

  
counts = []
for i in ing:
  counts.append(0)


max_score = 0
last = 0
stop = 1
while stop:
  carry = 1
  total = 0
  for x in range(0, len(ing)):
    if carry == 1:
      counts[x] += 1
      if counts[x] > 100:
        if x == len(ing) -2:
          # finished
          stop = 0
        carry = 1
        counts[x] = 0
      else:
        carry = 0
    if x < len(ing)-1:
      total += counts[x]
    if x == len(ing) -2:
      if counts[x] > last and counts[x] > 0 and counts[x] % 10 == 0: 
        print str(counts[x]) + "% done..."
        last = counts[x]

    if x == len(ing)-1:
      rem = 100 - total
      if rem < 0:
        continue
      else:
        counts[x] = rem
        s = score(counts)
        if s > max_score:
          if cals(counts) == 500:
            max_score = s
  #print counts

print "Part b: " + str(max_score)
 
exit() 

amount[0] = 44
amount[1] = 100 -amount[0]

x = score(amount)
print x
