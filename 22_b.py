import sys
from ctypes import *
import copy
import hashlib
import itertools
import re
from printf import printf

my_min_mana = 99999

#          NAME             MANA  DAM  HEAL +ARM  TURNS +MANA
spells = [['Magic Missile', 53,   4,   0 ,  0,    0,    0],
          ['Drain',         73,   2,   2 ,  0,    0,    0],
          ['Shield',        113,  0,   0,   7,    6,    0],
          ['Poison',        173,  3,   0,   0,    6,    0],
          ['Recharge',      229,  0,   0,   0,    5,    101]]
#         MY_MANA MY_HP BOSS_HP BOSS_DAM SHIELD_TURNS POISON_TURNS RECHARGE_TURNS

wins = []

def fight(round, spell, my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns):
  global wins
  global my_min_mana
  round += 1

  my_hp += -1
  if my_hp <= 0:
    return



  if spent_mana > my_min_mana:
    return
  if round > 40:
    return
  # ME TURN
  my_arm = 0
  # DO NEW SPELL
  if spell == 'Magic Missile':
    boss_hp += -4
    spent_mana += 53
    my_mana += -53
  if spell == 'Drain':
    boss_hp += -2
    my_hp += 2
    spent_mana += 73
    my_mana += -73
  if spell == 'Shield':
    shield_turns = 6
    spent_mana += 113
    my_mana += -113
  if spell == 'Poison':
    poison_turns = 6
    spent_mana += 173
    my_mana += -173
  if spell == 'Recharge':
    recharge_turns = 5
    spent_mana += 229
    my_mana += -229


  if my_mana < 0:
    return

  if boss_hp <= 0:
    wins.append(spent_mana)
    return


  # DO IN-PLAY SPELL EFFECTS
  if shield_turns > 0:
    my_arm = 7
    shield_turns += -1
  if poison_turns > 0:
    boss_hp += -3
    poison_turns += -1
  if recharge_turns > 0:
    my_mana += 101
    recharge_turns += -1

  if boss_hp <= 0:
    wins.append(spent_mana)
    if spent_mana < my_min_mana:
      my_min_mana = spent_mana
    return


  # BOSS TURN
  if poison_turns > 0:
    boss_hp += -3
    poison_turns += -1
  if recharge_turns > 0:
    my_mana += 101
    recharge_turns += -1
  if shield_turns > 0:
    my_arm = 7
    shield_turns += -1

  dam = boss_dam - my_arm
  if dam < 1:
    dam = 1
  my_hp -= dam

  if my_hp <= 0:
    return

  # DO ALL AVAILABLE SPELLS
  fight(round, 'Magic Missile', my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns)
  fight(round, 'Drain', my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns)
  if shield_turns <= 0:
    fight(round, 'Shield', my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns)
  if poison_turns <= 0:
    fight(round, 'Poison', my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns)
  if recharge_turns <= 0:
    fight(round, 'Recharge', my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns)
  return

  

my_mana = 500
my_hp = 50
boss_hp = 58
boss_dam = 9



spent_mana = 0
shield_turns = 0
poison_turns = 0
recharge_turns = 0
#fight(0, 'Magic Missile', my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns)
#fight(0, 'Drain', my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns)
#fight(0, 'Shield', my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns)
fight(0, 'Poison', my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns)
#fight(0, 'Recharge', my_mana, spent_mana, my_hp, boss_hp, boss_dam, shield_turns, poison_turns, recharge_turns)

min_mana = 99999
for x in wins:
  if x < min_mana:
    min_mana = x

print "Part B: " + str(min_mana)
