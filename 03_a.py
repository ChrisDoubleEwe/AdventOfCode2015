import sys
import itertools
from printf import printf

with open("03_input.txt") as f:
    content = f.readlines()

dirs = []

for line in content:
  for c in line.strip():
    dirs.append(c)

x = 0
y = 0

locs = []
loc = ";x:"+str(x)+":y:"+str(y)+";"
locs.append(loc)


for d in dirs:
  if d == '^':
    y = y-1
  if d == 'v':
    y = y+1
  if d == '<':
    x = x-1
  if d == '>':
    x = x+1
  loc = ";x:"+str(x)+":y:"+str(y)+";"
  locs.append(loc)






count = 0
uniq_locs = set(locs)
for loc in uniq_locs:
  count += 1
  #print loc + " : " + str(locs.count(loc))


print "Part A: " + str(count)

