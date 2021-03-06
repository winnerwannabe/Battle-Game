#/bin/python3
import random, time, os, re, sys
from time import sleep
from player import *
import player
AISCORES = {"random": 0,}




def print_slowly(str):
    for char in str:
      sleep(.025) #how fast print slowly prints
      sys.stdout.write(char)
      sys.stdout.flush()
    print()

def print_quickly(str):
    for char in str:
      sleep(.01)
      sys.stdout.write(char)
      sys.stdout.flush()

def invalad():
  htp = '''invalad\n'''

  for char in htp:
    sleep(.025)
    sys.stdout.write(char)
    sys.stdout.flush()

###########################
#### Helper functions #####
###########################
# get_status() function: displays status of Player objects (user and bot) 
def get_status(p1, p2): 
  os.system('clear')
  print("-" * 101)
  p1.status()
  p2.status()
  print("-" * 101)

# user_move() function: asks user to choose a move, then does move against bot
# user and bot are both Player objects

def user_move(user, bot, number):
  user.regen_health() #regens health and subtracts one from regen health value if regen health value is over 1
  user.regen_energy() #user.regen_health but for energy
  user.poisoned(bot)#does damage every turn to the enemy if poisoned value is above one
  user.loose_energy(bot) #user.poisoned but for energy
  user.armor_loss(bot) #user.poisoned but for defence
  if number == 1: #prints the get_Status define
    get_status(user, bot)
  else:
    get_status(bot,user)
  if user.tpr >= user.stalled:
    user.tpr -= user.stalled
    user.stalled = 0
  else:
    user.stalled -= user.tpr
    user.tpr = 0
  if user.tpr == 0:
    print_slowly("you don't have any moves!") 
    time.sleep(1)
  for i in range(user.tpr):
    print_slowly("choose a move:")
    for m in user.moves: # for each key in user.moves dictionary
      print(m) # print key (name of move)
      time.sleep(.3)
    answer = input(">").lower()
    while answer not in user.moves: # repeats until user inputs valid move name
      invalad()
      time.sleep(1)
      os.system("clear")
      if number == 1:
        get_status(user, bot)
      else:
        get_status(bot,user)
      for m in user.moves:
        print(m)
      answer = input(">").lower()
    print(user.name, ":",  answer)
    move = user.moves[answer] # looks up move in dictionary with key (name string)
    time.sleep(1)
    move(bot) # call user move against bot 
    os.system("clear")
    if number == 1:
      get_status(bot,user)
    else:
      get_status(user,bot)
  
  # pause program for 1 second
  if number == 1:
    get_status(user, bot)
  else:
    get_status(bot,user)
  time.sleep(1)

# bot_move() function: makes bot randomly do one of its moves against user 
# user and bot are both Player objects 

def bot_move(bot, user, number): 
  bot.regen_health()
  bot.regen_energy()
  bot.poisoned(user)
  bot.loose_energy(user)
  bot.armor_loss(user)
  if number == 1:
    get_status(bot, user)
  else:
    get_status(user,bot)
  if bot.tpr >= bot.stalled:
    bot.tpr -= bot.stalled
    bot.stalled = 0
  else:
    bot.stalled -= bot.tpr
    bot.tpr = 0
  if bot.tpr == 0:
    print_slowly("you don't have any moves!")
    time.sleep(1)
  for i in range(bot.tpr):
    print_slowly("computer move")
      
    move_name = random.choice(list(bot.moves.keys())) # randomly choose move name from dictionary
    move = bot.moves[move_name] # look up move in dictionary with key (name string)
    print_slowly(bot.name + " : " + move_name + "")
    time.sleep(1)
    move(user)# call bot move against user 
    os.system("clear")
    if number == 1:
      get_status(bot,user)
    else:
      get_status(user,bot)
  #we need the bot to remember
  #https://www.youtube.com/watch?v=dQw4w9WgXcQ OP CODE
  #probably use an if statement - winnerwannabe  
  if number == 1:
    get_status(bot, user)
  else:
    get_status(user,bot)
  time.sleep(1)