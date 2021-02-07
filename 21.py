import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

weapons = [['Dagger',        8,     4,       0],
           ['Shortsword',   10,     5,       0],
           ['Warhammer',    25,     6,       0],
           ['Longsword',    40,     7,       0],
           ['Greataxe',     74,     8,       0]]

armor =   [['Leather',      13,     0,       1],
           ['none',         0,      0,       0],
           ['Chainmail',    31,     0,       2],
           ['Splintmail',   53,     0,       3],
           ['Bandedmail',   75,     0,       4],
           ['Platemail',   102,     0,       5]]

rings =   [['Damage +1',    25,     1,       0],
           ['none1',         0,     0,       0],
           ['none2',         0,     0,       0],
           ['Damage +2',    50,     2,       0],
           ['Damage +3',   100,     3,       0],
           ['Defense +1',   20,     0,       1],
           ['Defense +2',   40,     0,       2],
           ['Defense +3',   80,     0,       3]]

def fight(w, a, r1, r2):
  my_hp = 100
  my_dam = w[2] + a[2] + r1[2] + r2[2]
  my_arm = w[3] + a[3] + r1[3] + r2[3]
  boss_hp = 109
  boss_dam = 8
  boss_arm = 2
  while my_hp > 0 and boss_hp > 0:
    boss_hp -= (my_dam - boss_arm)
    if boss_hp <= 0:
      return True
    my_hp -= (boss_dam - my_arm)
    if my_hp <= 0:
      return False


min_cost = 99999
max_cost = 0
for w in weapons:
  for a in armor:
    for r1 in rings:
      for r2 in rings:
        if r1 == r2: 
          continue
        cost = w[1] + a[1] + r1[1] + r2[1]
        result = fight(w,a,r1,r2)
        if result:
          if cost < min_cost:
            min_cost = cost
        else:
          if cost > max_cost:
            max_cost = cost

print "Part A: " + str(min_cost)
print "Part B: " + str(max_cost)

