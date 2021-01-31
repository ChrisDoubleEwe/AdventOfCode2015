import sys
import hashlib
import itertools
from printf import printf

#with open("03_input.txt") as f:
#    content = f.readlines()

key = 'ckczppom'

a_running = 1
b_running = 1
i = 1
while a_running or b_running:
  val = key + str(i)
  md = hashlib.md5(val.encode('utf-8')).hexdigest()
  if md.startswith('00000') and a_running:
    print "Part A: " + str(i)
    a_running = 0
  if md.startswith('000000') and b_running:
    print "Part B: " + str(i)
    b_running = 0

  i+=1
