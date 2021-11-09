#!/bin/python3
#this works fix
#? - winnerwannabe
#if you miss spell your character you crash
import random, time, os
from time import sleep
from player import *
from special import *
from special import Blue_Fire64 as Blue_Fire64
from special import Hercules as Hercules
from helper import *
from helper import print_slowly, print_quickly, invalad
win = 0
loss = 0
rounds = 0
winstreak = 0
randomchoice = random.randint(1,2)

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
    'crawler' : crawler,
    'withered stone' : withered_stone,
    'moss growth' : moss_growth
  }
  villains = [c.name for c in villains_map.values()]


  def __init__(self, h_or_v, selectedClass):
    self.charClass = None
    self.charStr = None

    if 'v' == h_or_v:
      class_map = classChooser.villains_map
    if 'h' == h_or_v:
      class_map = classChooser.heroes_map
    if 'r' == h_or_v:
      if randomchoice == 1:
        class_map = classChooser.heroes_map
      elif randomchoice == 2:
        class_map = classChooser.villains_map

    self.charClass = class_map[selectedClass]
    self.charStr = selectedClass

    return(None)

def player_chooser():
  print_slowly("is this character a player or bot? (p/b)\n")
  player_or_bot = input('>').lower()
  while player_or_bot != 'p' and player_or_bot != 'b':
    invalad()
    print_quickly("Valid inputs are 'p' or 'b'\n")
    player_or_bot = input('>').lower()

  print_slowly("do you want to be the hero or the villain? (type 'h' for hero, 'v' for villain, and 'r'for random)\n")
  mode = input('>').lower()
  while mode != 'h' and mode != 'v' and mode != "r":
      print_slowly("invalid\n")
      mode = input(">").lower()
  time.sleep(1)
  os.system('clear')
  print()

  if mode == 'h': #user chose hero
    userchars = classChooser.heroes
    time.sleep(2)
    os.system('clear')
  elif mode ==  "v": #user chose villain
    userchars = classChooser.villains
    time.sleep(2)
    os.system('clear')
  elif mode == "r": #user chose random
    if randomchoice == 1: #if a random is equal to 1 it chooses hero
      userchars = classChooser.heroes
      time.sleep(2)
      print_slowly("you are...\n")
      time.sleep(2)
      os.system("clear")
      print_slowly("a hero!")
    if randomchoice == 2: #if a random is equal to 2 it chooses villain
      userchars = classChooser.villains
      time.sleep(2)
      print_slowly("you are...\n")
      time.sleep(2)
      os.system("clear")
      print_slowly("a villain!")


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
    print_slowly("choose one of the following characters to fight against your enemy\n") 
    time.sleep(1)
    for i in userchars:
      print_quickly(str(i)+"\n")
      time.sleep(.5)

    userClass = None ;
    userClass = classChooser(mode, input(">").lower())

    while not userClass.charClass:
      invalad()
      userClass = classChooser(mode, input(">").lower())

    user = userClass.charClass(player_or_bot)

  elif answer == 'r':
    userClass = classChooser(mode, random.choice(userchars).lower())
    user = userClass.charClass(player_or_bot)
    print_slowly("your character is...\n")
    time.sleep(1)
    print_slowly(str(user))
    print("")
    time.sleep(1)

  return (user)

def consider_result(user, bot):
  global loss
  global win
  global winstreak
  if user.health <= 0:
    print_slowly("{} has no more health...\n".format(user))
    time.sleep(1)
    print_slowly(str(user)+" loses "+str(bot)+" wins!\n")
    loss += 1
    winstreak = 0
    return(False)

  elif bot.health <= 0:
    print_slowly("{} has no more health...\n".format(bot))
    time.sleep(1)
    print_slowly(str(bot)+" loses "+str(user)+" wins!\n")
    return(False)

  elif bot.health <= 0 and user.health <= 0:
    print_slowly("no one has any health...\n")
    time.sleep(1)
    print_slowly("how???\n")
    return(False)
  
  return(True)

if __name__=="__main__":
  print()
  print_slowly("welcome to the battlegame.\n")
  time.sleep(1)

  while True:
    player1 = player_chooser()
    os.system("clear")
    player2 = player_chooser()
    print_slowly("the enemy {} will be fighting against is...\n".format(player1))  
    time.sleep(1)
    print_slowly("{}!".format(str(player2)))
    time.sleep(1)
    get_status(player1, player2)
    time.sleep(1)

    while True:
      if player1.p_or_b == 'p':
        user_move(player1, player2)
      elif player1.p_or_b == 'b':
        bot_move(player1, player2)
      time.sleep(1)
      
      if not consider_result(player1, player2):
        break

      if player2.p_or_b == 'p':
        user_move(player2, player1)
      elif player2.p_or_b == 'b':
        bot_move(player2, player1)
      time.sleep(1)

      if not consider_result(player2, player1):
        break

    time.sleep(1)
    print("_"*115)
    time.sleep(1)
    print_slowly("player1 wins: " + str(win) + " player2 wins: " + str(loss) + "\n")
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