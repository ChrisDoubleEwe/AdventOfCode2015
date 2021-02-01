import sys
import hashlib
import itertools
from printf import printf

with open("05_input.txt") as f:
    content = f.readlines()

forbidden_list = ['ab', 'cd', 'pq', 'xy']
nice = 0

for w in content:
  word = w.strip()
  vowels = 0
  last = ''
  double = 0
  forbidden = 0
  for c in word:
    if c in ['a','e','i','o','u']:
      vowels += 1
    if c == last:
      double = 1
    last = c
  for f in forbidden_list:
    if f in word:
      forbidden = 1

  if vowels >= 3 and double == 1 and forbidden == 0:
    nice += 1

print "Part A: "+ str(nice)
