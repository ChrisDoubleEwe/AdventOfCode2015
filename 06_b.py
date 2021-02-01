import sys
import copy
import hashlib
import itertools
import re
from printf import printf

with open("06_input.txt") as f:
    content = f.readlines()

commands = []
for line in content:
  l = line.strip()
  command = []
  match = re.search('turn on ([0-9]*),([0-9]*) through ([0-9]*),([0-9]*)', l)
  if match:
    command.append('ON')
    command.append(int(match.group(1)))
    command.append(int(match.group(2)))
    command.append(int(match.group(3)))
    command.append(int(match.group(4)))
  match = re.search('turn off ([0-9]*),([0-9]*) through ([0-9]*),([0-9]*)', l)
  if match:
    command.append('OFF')
    command.append(int(match.group(1)))
    command.append(int(match.group(2)))
    command.append(int(match.group(3)))
    command.append(int(match.group(4)))
  match = re.search('toggle ([0-9]*),([0-9]*) through ([0-9]*),([0-9]*)', l)
  if match:
    command.append('TOGGLE')
    command.append(int(match.group(1)))
    command.append(int(match.group(2)))
    command.append(int(match.group(3)))
    command.append(int(match.group(4)))



  commands.append(command)

lights = []
size = 1000
for x in range(0, size):
  row = []
  for y in range(0, size):
    row.append(0)
  lights.append(copy.deepcopy(row))

for c in commands:
  if c[0] == 'ON':
    for x in range(c[1], c[3]+1):
      for y in range(c[2], c[4]+1):
        lights[y][x] += 1

  if c[0] == 'OFF':
    for x in range(c[1], c[3]+1):
      for y in range(c[2], c[4]+1):
        lights[y][x] += -1
        if lights[y][x] < 0:
          lights[y][x] = 0

  if c[0] == 'TOGGLE':
    for x in range(c[1], c[3]+1):
      for y in range(c[2], c[4]+1):
        lights[y][x] += 2

count = 0
for x in range(0, size):
  for y in range(0, size):
    count += lights[y][x] 

print "Part B: " + str(count)





    
  

  
