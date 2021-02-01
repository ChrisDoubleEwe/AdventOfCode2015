import sys
import re
import hashlib
import itertools
from printf import printf

with open("05_input.txt") as f:
    content = f.readlines()

pairs = []
for p in 'abcdefghijklmnopqrstuvwxyz':
  pr = '('+p+'.'+p+')'
  pairs.append(pr)

dubs = []
for x in 'abcdefghijklmnopqrstuvwxyz':
  for y in 'abcdefghijklmnopqrstuvwxyz':
    p = '('+x+y+'.*'+x+y+')'
    dubs.append(p)



nice = 0
tot_p = 0
tot_r = 0
iter = -1
for w in content:
  iter+=1
  print str(iter) + " / " + str(len(content))
  word = w.strip()
  rep = 0
  pair = 0


  for p in pairs:
    match = re.search(p, word)
    if match:
      rep = 1
      break

  for d in dubs:
    match = re.search(d, word)
    if match:
      pair = 1
      break



  if pair == 1:
    tot_p += 1
  if rep == 1:
    tot_r += 1
  if rep == 1 and pair == 1:
    nice += 1

print "Part B: "+ str(nice)
