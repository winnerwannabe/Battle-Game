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
def get_status(user, bot): 
  os.system('clear')
  print("-" * 115)
  user.status()
  bot.status()
  print("-" * 115)

# user_move() function: asks user to choose a move, then does move against bot
# user and bot are both Player objects

def user_move(user, bot):
  user.regen_health() #regens health and subtracts one from regen health value if regen health value is over 1
  user.regen_energy() #user.regen_health but for energy
  user.poisoned(bot)#does damage every turn to the enemy if poisoned value is above one
  user.loose_energy(bot) #user.poisoned but for energy
  user.armor_loss(bot) #user.poisoned but for defence
  get_status(user, bot) #prints the get_Status define
  print_slowly("choose a move:\n")
  
  for m in user.moves: # for each key in user.moves dictionary
    print(m) # print key (name of move)
    time.sleep(.3)
  answer = input(">").lower()
  while answer not in user.moves: # repeats until user inputs valid move name
    invalad()
    time.sleep(1)
    os.system("clear")
    get_status(user,bot)
    for m in user.moves:
      print(m)
    answer = input(">").lower()
  print(user.name, ":",  answer)
  move = user.moves[answer] # looks up move in dictionary with key (name string)
  time.sleep(1)
  move(bot) # call user move against bot 
  
  # pause program for 1 second
  get_status(user, bot)
  time.sleep(1)

# bot_move() function: makes bot randomly do one of its moves against user 
# user and bot are both Player objects 

def bot_move(bot, user): 
  stay = 0
  bot.regen_health()
  bot.regen_energy()
  bot.poisoned(user)
  bot.loose_energy(user)
  bot.armor_loss(user)
  get_status(user, bot)
  print_slowly("computer move\n")
  #save reference values
  userstarthealth = user.health
  botstarthealth = bot.health # MOVENAME VALUE
  VERYTEMPSCOREADJUSTER = -100
  for i in (AISCORES):
    if AISCORES[i] > VERYTEMPSCOREADJUSTER:
      VERYTEMPSCOREADJUSTER = AISCORES[i]
    
  move_name = random.choice(list(bot.moves.keys())) # randomly choose move name from dictionary
  move = bot.moves[move_name] # look up move in dictionary with key (name string)
  print_slowly(bot.name + " : " + move_name + "\n")
  time.sleep(1)
  move(user)# call bot move against user 
  #we need the bot to remember
  #https://www.youtube.com/watch?v=dQw4w9WgXcQ OP CODE
  #probably use an if statement - winnerwannabe  
  if stay == 0:
    get_status(user, bot)
    stay += 1
  else:
    stay = 0
    get_status(bot,user)
  time.sleep(1)
  #the higher this number, the better
  moveeffectplayerhealth = userstarthealth - user.health #ur stupeed
  #the higher this number is the better
  moveeffectbothealth = botstarthealth - bot.health
  moveAIscore = moveeffectplayerhealth + moveeffectbothealth
  AISCORES[move_name] = moveAIscore