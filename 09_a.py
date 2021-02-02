import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

with open("09_input.txt") as f:
    content = f.readlines()

trips = []
dests = []
all_dests= []
for p in content:
  pair = p.strip()
  match = re.search('^([A-Za-z]+) to ([A-Za-z]+) = ([0-9]*)', pair)
  if match:
    trip = []
    trip.append(match.group(1))
    trip.append(match.group(2))
    all_dests.append(match.group(1))
    all_dests.append(match.group(2))

    trip.append(int(match.group(3)))
    trips.append(trip)

def get_distance(c):
  total_dist = 0
  prev = ''
  for city in c:
    if prev == '':
      prev = city
      continue
    #print "Looking for " + prev + " to " + city
    dist = 0
    for t in trips:
      if (t[0] == prev and t[1] == city) or (t[0] == city and t[1] == prev):
        #print t
        dist = t[2]
        #print dist
    total_dist += dist 
    prev = city
  
  return total_dist

dests = list(set(all_dests))
combos =  list(itertools.permutations(dests, len(dests)))
shortest = 99999999
longest = 0
for c in combos:
  d =  get_distance(c)
  if d < shortest:
    shortest = d
  if d > longest:
    longest = d

print "Part A: " + str(shortest)
print "Part B: " + str(longest)



