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

def do(s, moves):
  global results
  all_e = 1
  for i in s:
    if i != 'e':
      all_e = 0
      break

  if all_e == 1:
    if moves not in results:
      print "Part B: " + str(moves)
      exit()
      results.append(moves)
    return

  any_moves = 0
  for r in reps:
    num_matches = s.count(r[1])
    #if num_matches > 0:
      #print "There are " + str(num_matches) + " instances of " + r[1] + " in " + s
    any_moves += num_matches
    for i in range(0, num_matches):
      #print "Replacing instance " + str(i) + " of " + r[1] + " in " + s
      x = replacenth(s, r[1], r[0], i)
      do(x, moves+1)
  
  if any_moves == 0:
    return


do(s, 0)

min = 999999
for i in results:
  if i < min:
    min = i 

print "Part B: " + str(min)
