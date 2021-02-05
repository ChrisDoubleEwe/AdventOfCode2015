import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("17_input.txt") as f:
    content = f.readlines()

buckets = []
for c in content:
  buckets.append(int(c.strip()))


combos = []
for l in range(1, len(buckets)+1):
  z = list(itertools.combinations(buckets, l))
  for x in z:
    combos.append(x)

count = 0
min_combos = 999
for c in combos:
  total = 0
  for i in c:
    total += i
  if total == 150:
    if len(c) < min_combos:
      min_combos = len(c)


for c in combos:
  total = 0
  for i in c:
    total += i
  if total == 150:
    if len(c) == min_combos:
      count += 1


print "Part B: " + str(count)

