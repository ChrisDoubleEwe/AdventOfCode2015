import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf
import json


total = 0
input = ''
output = ''

with open("12_input.txt") as f:
    content = f.readlines()

for line in content:
  input = input + line

jsonObject = json.loads(input)

def process(e):
  global total
  if type(e) is list:
    for x in e:
      process(x)
  elif type(e) is dict:
    red = 0
    for key in e.keys():
      if e[key] == 'red':
        red = 1
    if red == 0:
      for key in e.keys():
        process(e[key])
  else:
    num = 1
    for c in str(e):
      if c.isdigit() or c == '-':
        num = num
      else:
        num = 0

    if num == 1:
      print "NUM " + str(e)
      total += int(e)
    else:
      print "non " + str(e) 


for element in jsonObject:
  process(element)

print "Part B: " + str(total)
