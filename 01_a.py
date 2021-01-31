import sys
import itertools
from printf import printf

with open("01_input.txt") as f:
    content = f.readlines()


floor = 0
pos = 0
basement_pos = 0
for line in content:
  for c in line:
    pos += 1
    old_floor = floor
    if c == '(':
      floor += 1
    if c == ')':
      floor += -1
    if floor == -1:
      if basement_pos == 0:
        basement_pos = pos


print "Part A: " + str(floor)
print "Part B: " + str(basement_pos)

