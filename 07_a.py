import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("07_input.txt") as f:
    content = f.readlines()

values = {}
commands = []
for line in content:
  command = []
  l = line.strip()
  match = re.search('^([0-9]+) -> ([a-z]+)', l)
  if match:
    values[match.group(2)] = int(match.group(1))

  match = re.search('^NOT ([a-z]+) -> ([a-z]+)', l)
  if match:
    command.append("NOT")
    command.append(match.group(1))
    command.append(match.group(2))

  match = re.search('^([a-z]+) AND ([a-z]+) -> ([a-z]+)', l)
  if match:
    command.append("AND")
    command.append(match.group(1))
    command.append(match.group(2))
    command.append(match.group(3))

  match = re.search('^([a-z]+) -> ([a-z]+)', l)
  if match:
    command.append("COPY")
    command.append(match.group(1))
    command.append(match.group(2))


  match = re.search('^([0-9]+) AND ([a-z]+) -> ([a-z]+)', l)
  if match:
    command.append("ANDn")
    command.append(int(match.group(1)))
    command.append(match.group(2))
    command.append(match.group(3))


  match = re.search('^([a-z]+) OR ([a-z]+) -> ([a-z]+)', l)
  if match:
    command.append("OR")
    command.append(match.group(1))
    command.append(match.group(2))
    command.append(match.group(3))

  match = re.search('^([a-z]+) LSHIFT ([0-9]+) -> ([a-z]+)', l)
  if match:
    command.append("LSHIFT")
    command.append(match.group(1))
    command.append(int(match.group(2)))
    command.append(match.group(3))

  match = re.search('^([a-z]+) RSHIFT ([0-9]+) -> ([a-z]+)', l)
  if match:
    command.append("RSHIFT")
    command.append(match.group(1))
    command.append(int(match.group(2)))
    command.append(match.group(3))

  if len(command) > 0:
    commands.append(command)

while len(commands) > 0:
  new_commands = []
  for c in commands:
    if c[0] == 'COPY':
      if c[1] in values.keys():
        values[c[2]] = values[c[1]]
      else:
        new_commands.append(c)

    if c[0] == 'AND':
      if c[1] in values.keys() and c[2] in values.keys():
        values[c[3]] = values[c[1]] & values[c[2]]
      else:
        new_commands.append(c)

    if c[0] == 'ANDn':
      if c[2] in values.keys():
        values[c[3]] = c[1] & values[c[2]]
      else:
        new_commands.append(c)


    if c[0] == 'OR':
      if c[1] in values.keys() and c[2] in values.keys():
        values[c[3]] = values[c[1]] | values[c[2]]
      else:
        new_commands.append(c)

    if c[0] == 'NOT':
      if c[1] in values.keys():
        values[c[2]] = ~ values[c[1]]
      else:
        new_commands.append(c)

    if c[0] == 'LSHIFT':
      if c[1] in values.keys():
        values[c[3]] = values[c[1]] << c[2]
      else:
        new_commands.append(c)

    if c[0] == 'RSHIFT':
      if c[1] in values.keys():
        values[c[3]] = values[c[1]] >> c[2]
      else:
        new_commands.append(c)

  commands = copy.deepcopy(new_commands)


result = -1
for x in values.keys():
  a = values[x]
  if a < 0:
    b = a + 2**16
    a = b
  if x == 'a':
    result = a

print "Part B: " + str(result)

