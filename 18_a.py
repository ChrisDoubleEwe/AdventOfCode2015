import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("18_input.txt") as f:
    content = f.readlines()

map = []
for line in content:
  row = []
  for c in line.strip():
    row.append(c)
  map.append(row)

width = len(map)-1

def count_on(x, y):
  global map
  result = 0
  if x > 0 and y > 0:
    if map[y-1][x-1] == '#':
      result += 1
  if y > 0:
    if map[y-1][x] == '#':
      result += 1
  if x < width and y > 0:
    if map[y-1][x+1] == '#':
      result += 1

  if x > 0:
    if map[y][x-1] == '#':
      result += 1
  if x < width:
    if map[y][x+1] == '#':
      result += 1

  if x > 0 and y < width:
    if map[y+1][x-1] == '#':
      result += 1
  if y < width:
    if map[y+1][x] == '#':
      result += 1
  if y < width and x < width:
    if map[y+1][x+1] == '#':
      result += 1
  return result




    
def move():
  global map
  new_map = copy.deepcopy(map)
  for x in range(0, width+1):
    for y in range(0, width+1):
      z = count_on(x, y)
      if map[y][x] == '#':
        if (z == 2 or z == 3):
          new_map[y][x] = '#'
        else:
          new_map[y][x] = '.'
      else:
        if z == 3:
          new_map[y][x] = '#'
        else:
          new_map[y][x] = '.'

  map = copy.deepcopy(new_map)
     
      
for iter in range(0, 100):
  move()    


total = 0
for x in range(0, width+1):
  for y in range(0, width+1):
    if map[y][x] == '#':
      total += 1


print "Part A: " + str(total)

