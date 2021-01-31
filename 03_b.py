import sys
import itertools
from printf import printf

with open("03_input.txt") as f:
    content = f.readlines()

dirs = []

for line in content:
  for c in line.strip():
    dirs.append(c)

s_x = 0
s_y = 0
r_x = 0
r_y = 0

s_locs = []
r_locs = []

loc = ";x:"+str(s_x)+":y:"+str(s_y)+";"
s_locs.append(loc)
r_locs.append(loc)


robo = 0
for d in dirs:
  if robo == 0:
    x = s_x
    y = s_y
  else:
    x = r_x
    y = r_y

  if d == '^':
    y = y-1
  if d == 'v':
    y = y+1
  if d == '<':
    x = x-1
  if d == '>':
    x = x+1
  loc = ";x:"+str(x)+":y:"+str(y)+";"
  if robo == 1:
    r_locs.append(loc)
    r_x = x
    r_y = y
  else:
    s_locs.append(loc)
    s_x = x
    s_y = y
  robo += 1
  if robo > 1:
    robo = 0






locs = s_locs
locs.extend(r_locs)


count = 0
uniq_locs = set(locs)
for loc in uniq_locs:
  count += 1


print "Part B: " + str(count)

