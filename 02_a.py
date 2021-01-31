import sys
import itertools
from printf import printf

with open("02_input.txt") as f:
    content = f.readlines()

def wrap(p):
  dims = p.split('x')
  dim_ints = []
  l = int(dims[0])
  w = int(dims[1])
  h = int(dims[2])
  dim_ints.append(l)
  dim_ints.append(w)
  dim_ints.append(h)
  dim_ints.sort()
  smallest_side = dim_ints[0] * dim_ints[1]
  sa = 2*l*w + 2*w*h + 2*h*l + smallest_side
  return sa


def ribbon(p):
  dims = p.split('x')
  dim_ints = []
  l = int(dims[0])
  w = int(dims[1])
  h = int(dims[2])
  dim_ints.append(l)
  dim_ints.append(w)
  dim_ints.append(h)
  dim_ints.sort()
  smallest_perim = (2 * dim_ints[0]) + (2 * dim_ints[1])
  bow = l * w * h
  return smallest_perim + bow


total = 0
total_ribbon = 0
for p in content:
  w = wrap(p.strip())
  total += w
  r = ribbon(p.strip())
  total_ribbon += r


print "Part A: " + str(total)
print "Part B: " + str(total_ribbon)

