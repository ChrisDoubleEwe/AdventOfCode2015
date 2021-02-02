import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

input = 'hepxcrrq'
list_one = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz' ]
list_two = ['i', 'o', 'l']
list_three = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz' ]

def inc(i):
  global list_one
  z = list(i)
  c = z[7]
  carry = 1
  index = 8
  while carry == 1 and index >= 0:
    index += -1
    c = z[index]
    if ord(c) == 122:
      c = 'a'
      carry = 1
    else:
      c = chr(ord(c)+1)
      carry = 0
    z[index] = c
  return ''.join(z)

def test(i):
  test_one = 0
  test_two = 1
  test_three = -1
  for l in list_one:
    if l in i:
      test_one = 1
 
  for l in list_two:
    if l in i:
      test_two = 0

  for l in list_three:
    if l in i:
      test_three += 1

  if test_three > 0:
    test_three = True
  else:
    test_three = False

  if test_one and test_two and test_three:
    return True
  else:
    return False
  


input = inc(input)
while test(input) != True:
  input = inc(input)

print "Part A: " + input

input = inc(input)
while test(input) != True:
  input = inc(input)

print "Part B: " + input

