#/bin/python3
import random, time
from helper import *
from helper import print_slowly

#player class, parent of all classes
class Player:
  name = 'Player'

  # __init__() method initializes new instance of Player
  def __init__(self, name):
    self.name = name #what the name of the character your playing is ._.
    self.health = 100 #your health ._. if it <= 0 you die
    self.hpr = 0 #how much health regen_health gives you
    self.energy = 1 #most things are multiplied by this
    self.epr = .015 #hpr but for regen_energy
    self.defence = 0 #makes damage = damgage - defence
    self.moves = {}# create dictionary of moves
    self.imortal = 0 #if more than 1, imortal
    self.regen_health_value = 0#regeneration for health
    self.health_regened_per_round = 15
    self.regen_energy_value = 0#line above but for energy
    self.poisoned_value = 0#line above but for damage
    self.dpr = 15 #how much damage poisoned does
    self.energy_losses = 0 #poisoned but for energy
    self.elpr = .005 #dpr but for energy_losses
    self.rounds = 1 #what round it is
    self.even_out = 0 #makes it so that rounds work
    self.if_armor_loss = 0 #poisoned but for defence
    self.roal = 1 #dpr but for defence

    # moves property is a dictionary - used to look up a Player's moves    
    # key = string (name of move), value = method (function for move)  
    
    self.moves["attack"] = self.attack# add attack move to dictionary
    self.moves["heal"] = self.heal# add heal move to dictionary
    self.moves["defend"] = self.defend#ups defence
    self.moves["rest"] = self.rest #heals and gives energy
    self.moves["skip"] = self.skip #skips your turn

  def __str__(self):
    return (self.__class__.name)

  # status() method prints out a Player's name and health properties    
  def status(self): 
    if self.even_out >= 4: #status is called 4 times per round if it has been called 4 times (one round's worth)
      self.rounds += 1 #marks rounds up 1
      self.even_out = 0 #resets rounds
      print(self.name, " health:", "%.2f"%self.health," energy:","%.2f"%self.energy, " defence:","%.2f"%self.defence, " round:", self.rounds) #prints health, energy, defence, and what round it is
    else: #if even out is not = to 4
      self.even_out += 1 #adds one to even_out
      print(self.name, " health:", "%.2f"%self.health," energy:","%.2f"%self.energy, " defence:","%.2f"%self.defence, " round:", self.rounds)

  # attack() method: move that lowers health of enemy Player 
  # enemy: Player object 
  # damage: integer (optional). If no 2nd argument given, does random damage.
 
  def attack(self, enemy, damage=-1): #defines attack
    if damage == -1:# if there is no 2nd argument 
      damage = random.randint(20, 40)# random number for damage
    damage *= self.energy# multiplies damage by energy level
    damage -= enemy.defence#should make damage damage - defence
    if enemy.imortal >= 1: # if enemy.imortal is greater than or equal to 1:
      damage = 0 # damage is 0
      print_slowly("blocked! " + self.name + " did 0 damage to " + enemy.name + "\n") # says that the attack did nothing
      time.sleep(2)
    else:
      if damage <= 0: #if damgage is less than or equal to 0
        print_slowly(self.name + " did 0 damage to " + enemy.name + "\n") # says that the attack did nothing
        time.sleep(2)
      else: # damage is not less than or equal to 0
        enemy.health -= damage #subtracts damage from enemy's health
        print_slowly(str(self.name+" did "+"%.2f"%damage+" damage to "+enemy.name + "\n"))
        time.sleep(2)

  # heal() method: move that increases a Player's own health (by random amount)  
  # enemy: Player object 
  
  def heal(self, enemy): #defines heal
    n = random.randint(25, 40) # random number for health increase 
    n *= self.energy # multiplied by energy level
    if n >= 0: #if n is greater than or = too 0
      self.health += n #adds n to health
      print_slowly(str(self.name+" healed self "+"%.2f"%n)) # says how much you healed
      time.sleep(1)
    else: #if n is not greater than or equal to 0
      self.health += 0 # adds 0 to health
      print_slowly(self.name + " healed self 0") # says that you healed nothing
      time.sleep(1)

  def defend(self,enemy):
    self.defence += random.randint(1,10) * self.energy
    n = random.randint(1,10) # random number for health increase 
    n *= self.energy # multiplied by energy level
    if n >= 0:
      self.defence += n 
      print_slowly(str(self.name+" gained "+"%.2f"%n+" defence"))
      time.sleep(1)
    else:
      self.defence += 0
      print_slowly(self.name + " gained 0 defence")
      time.sleep(1)

  def rest(self, enemy): #good way to get energy
    n = (10)
    n *= self.energy
    if n >= 0:
      self.health += self.energy * n 
      print_slowly(self.name+" health and energy incresed")
      time.sleep(1)
      self.energy += self.energy * .05
    else:
      self.energy += 0

  def skip(self, enemy):
    print_slowly("you skipped your turn")
    time.sleep(1)

  def regen_health(self):
    if self.regen_health_value >= 1:
      if self.health_regened_per_round * self.energy >= 5:
        self.health += self.health_regened_per_round * self.energy
      else:
        self.health += 5
      self.regen_health_value -= 1
    else:
      self.regen_health_value += .2

  def regen_energy(self):
    if self.regen_energy_value >= 1:
      n = self.epr * self.energy
      if n >= self.epr:
        self.energy += n
      else:
        self.energy += self.epr
      self.regen_energy_value -= 1
    else:
      self.regen_energy_value += .2

  def poisoned(self,enemy):
    if self.poisoned_value >= 1:
      self.health -= self.dpr * enemy.energy
      self.poisoned_value -= 1
    else:
      self.poisoned_value += 0

  def loose_energy(self,enemy):
    if self.energy_losses >= 1:
      self.energy -= self.elpr * enemy.energy
      self.energy_losses -= 1
    else:
      self.energy_losses += 0

  def armor_loss(self,enemy):
    if self.if_armor_loss >= 1 and self.defence > 0:
      if self.defence >= enemy.energy * self.roal:
        self.defence -= self.roal * self.energy
      else:
        self.defence = 0
    else:
      self.defence -= 0