import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

def factorize(num):
    return [n for n in range(1, num + 1) if num % n == 0]

def calc(n):
  presents = 0
  facs = factorize(n)
  for f in facs:
    presents += 10*f
  return presents



n = 20
max = 0
while True:
  n+=20
  #print "House " + str(n) + "..."
  presents = calc(n)
  #print "  House " + str(n) + " : " + str(presents)
  if presents > max:
    max = presents
    print "  House " + str(n) + " : " + str(presents)
  if presents >= 29000000:
    exit()
