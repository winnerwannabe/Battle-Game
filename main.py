#!/bin/python3
#this works fix
#? - winnerwannabe
import random, time, os, re, sys
from time import sleep
from player import *
from special import *
from helper import *
from helper import print_slowly, print_quickly, invalad
win = 0
loss = 0
rounds = 0
winstreak = 0

class classChooser:
  heroes_map = {
    'spiderman' : Spiderman,
    'pikachu' : Pikachu,
    'hercules' : Hercules,
    'jedi' : Jedi,
    'blue_fire64' : Blue_Fire64,
    'coral guardian' : coral_guardian,
    'winnerwannabe' : winnerwannabe,
    'wyvern' : wyvern,
    'covid vaccine' : covid_vaccine,
    'shobe' : shobe
  }
  heroes = [c.name for c in heroes_map.values()]
  villains_map = {
    'voldemort' : Voldemort,
    'thanos' : Thanos,
    'mewtwo' : Mewtwo,
    'medusa' : Medusa,
    'teacher' : teacher,
    'dummy' : dummy,
    'spinal millipede' : spinal_millipede,
    'wyvern' : wyvern,
    'covid-19' : covid19,
    'firebeast' : firebeast,
    'crawler' : crawler
  }
  villains = [c.name for c in villains_map.values()]


  def __init__(self, h_or_v, selectedClass):
    self.charClass = None
    self.charStr = None

    if 'v' == h_or_v:
      class_list = classChooser.villains
      class_map = classChooser.villains_map
    if 'h' == h_or_v:
      class_list = classChooser.heroes
      class_map = classChooser.heroes_map
    if selectedClass not in [c.lower() for c in class_list]:
      return(None)

    self.charClass = class_map[selectedClass]
    self.charStr = selectedClass
    return(None)

print()
print_slowly("welcome to the battlegame.\n")
time.sleep(1)

while True:
  print_slowly("do you want to be the hero or the villain? (type 'h' for hero and 'v' for villain.)\n")
  mode = input('>').lower()
  while mode != 'h' and mode != 'v':
      print_slowly("invalid\n")
      mode = input(">").lower()
  time.sleep(1)
  os.system('clear')
  print()

  if mode == 'h':
    print_slowly("the computer will be the villain and you will be the hero")
    userchars = classChooser.heroes
    botchars = classChooser.villains
    time.sleep(2)
    os.system('clear')
  elif mode ==  "v":
    print_slowly("the computer will be the hero and you will be the villain")
    userchars = classChooser.villains
    botchars = classChooser.heroes
    time.sleep(2)
    os.system('clear')

  print()
  time.sleep(1)
  print_slowly("Do you want to choose your character or do you want it to be random? (Type 'c' for choose and 'r' for random.)\n")
  answer = input(">").lower()
  while answer != 'c' and answer != 'r':
      print_slowly("invalid\n")
      answer = input(">").lower()
  time.sleep(2)

  if answer == 'c':
    os.system('clear')
    print()
    time.sleep(1)
    print_slowly("choose one of the following characters to fight against the enemy\n") 
    time.sleep(1)
    for i in userchars:
      print_quickly(str(i)+"\n")
      time.sleep(.5)

    userClass = None ;
    userClass = classChooser(mode, input(">").lower())

    while not userClass.charClass:
      invalad()
      userClass = classChooser(mode, input(">").lower())

    user = userClass.charClass()

  elif answer == 'r':
    userClass = classChooser(mode, random.choice(userchars))
    user = userClass.charClass()
    print_slowly("your character is...\n")
    time.sleep(1)
    print_slowly(str(user))
    print("")
    time.sleep(1)

  if 'h' == mode:
    vc = 'v'
  elif 'v' == mode:
    vc = 'h'
  botClass = classChooser(vc, random.choice(botchars))
  bot = botClass.charClass() #has glitch sometimes this nometype is not callable

  print_slowly("the enemy {} will be fighting against is...\n".format(user))  
  time.sleep(1)
  print_slowly("{}!".format(str(bot)))
  time.sleep(1)
  get_status(user, bot)
  time.sleep(1)

  while True:
    user_move(user, bot)
    time.sleep(1)
    
    if user.health <= 0:
      print_slowly("{} has no more health...\n".format(user))
      time.sleep(1)
      print_slowly("you lose\n")
      loss += 1
      winstreak = 0
      break

    elif bot.health <= 0:
      print_slowly("{} has no more health...\n".format(bot))
      time.sleep(1)
      print_slowly("you win\n")
      win += 1
      winstreak += 1
      break

    elif bot.health <= 0 and user.health <= 0:
      print_slowly("no one has any health...\n")
      time.sleep(1)
      print_slowly("how???\n")
      winstreak = 0
      break
    
    bot_move(user, bot)
    time.sleep(1)
    
    if user.health <= 0:
      print_slowly("{} has no more health...\n".format(user))
      time.sleep(1)
      print_slowly("you lose\n")
      loss += 1
      winstreak = 0
      break

    elif bot.health <= 0:
      print_slowly("{} has no more health...\n".format(bot))
      time.sleep(1)
      print_slowly("you win\n")
      win += 1
      winstreak += 1
      break

    elif bot.health <= 0 and user.health <= 0:
      print_slowly("no one has any health...\n")
      time.sleep(1)
      print_slowly("how???\n")
      winstreak = 0
      break

  time.sleep(1)
  print("_"*115)
  time.sleep(1)
  print_slowly("wins: " + str(win) + " losses: " + str(loss) + " winstreak: " + str(winstreak) + "\n")
  print_slowly("want to play another round? y/n\n")
  time.sleep(1)
  new_round = input(">").lower()

  while new_round != 'y' and new_round != 'yes' and new_round != 'n' and new_round != 'no':
    print("")
    invalad()
    time.sleep(1)
    new_round = input(">").lower()
  
  if new_round == 'y' or new_round == 'yes':
    os.system('clear')
    print("")
  
  elif new_round == 'n' or new_round == 'no':
    print_slowly("...")
    time.sleep(1)
    print_slowly("okay then.")
    time.sleep(1)
    break