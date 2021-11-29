#/bin/python3
import random, time
from player import *
from player import Player
from helper import print_slowly

# Child Classes (special players)

#####################################
########### Child Classes ###########
#####################################

#character ideas:
#piece maker/hero/


# Spiderman class
class Spiderman(Player): # create child class of Player
  name = 'Spiderman'

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "Spiderman") # use __init__ method from Player
    self.moves["web shooter"] = self.web_shooter # add new move to dictionary
    self.moves["face punch"] = self.face_punch
    self.moves["flying kick"] = self.flying_kick
    self.moves["think"] = self.think
    self.special_move = 10

  def __str__(self): # returns a string when the object is called in a string context
      return(Spiderman.name)

  def web_shooter(self, enemy): # defines special move for child class
    self.attack(enemy, random.randint(40, 50)) #calls player's attack move and gives it a new damage number
    self.special_move -= 1
    if self.special_move <= 0:
      self.moves.pop("web shooter")
  
  def face_punch(self, enemy):
    damage = random.randint(30, 45) #you can doit this way too
    self.attack(enemy, damage)
  
  def flying_kick(self, enemy):
    if random.random() <= 0.75:#75% chance of one type of damage
      damage = random.randint(35, 60)
      self.attack(enemy, damage)
    else:#the other 25% chance
      print_slowly("Spiderman didn't do a good kick...")
      time.sleep(1)
      damage = random.randint(20, 25)
      self.attack(enemy, damage)
  
  def think(self, enemy):
    self.energy += 0.2 * self.energy
    print_slowly(self.name + " has increased energy.")
    if self.energy >= 2: # if energy gets too high...
      self.moves.pop("think") # remove from dictionary of possible moves
      print_slowly("you can't use this move anymore")

#shobe class
class shobe(Player): # create child class of Player
  name = "shobe"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "shobe")
    self.moves["cheese toss"] = self.cheese_toss
    self.moves["cheese wall"] = self.cheese_wall
    self.moves["cheesy onslaught"] = self.cheesy_onslaught

  def __str__(self):
      return(shobe.name)

  def cheesy_onslaught(self,enemy):
    self.attack(enemy, 69)

  def cheese_toss(self,enemy):
    self.attack(enemy, 30)
    self.health += 15 * self.energy

  def cheese_wall(self,enemy):
    n = 7 # random (who did this? it's a set number.) number for health increase 
    n *= self.energy # multiplied by energy level
    if n >= 0:
      self.defence += n 
      print_slowly(self.name+" gained "+"%.2f" %n+" defence")
      time.sleep(1)
    else:
      self.defence += 0
      print_slowly(self.name+" gained 0 defence")
      time.sleep(1)
    v = 10 # random (again, SET NUMBER) number for health increase 
    v *= self.energy # multiplied by energy level
    if v >= 0:
      self.health += v 
      print_slowly(self.name+" gained "+"%.2f" %v+" health")
      time.sleep(1)
    else:
      self.health += 0
      print_slowly(self.name+" gained 0 health")
      time.sleep(1)
    self.health += self.energy * 10

#wyvern class
class wyvern(Player):
  name = "wyvern"
  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "wyvern")
    self.moves["fire breath"] = self.fire_breath
    self.moves["claw swipe"] = self.claw_swipe
    self.defence = 10
    self.health = 110

  def __str__(self): # returns a string when the object is called in a string context
      return(wyvern.name)

  def fire_breath(self,enemy):
    self.attack(enemy,random.randint(20,30))
    enemy.energy -= .05 * self.energy

  def claw_swipe(self,enemy):
    self.attack(enemy, random.randint(40,70))

#thanos class
class Thanos(Player):
  name = "Thanos"
  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "Thanos")
    self.moves["smash"] = self.smash
    self.moves["Thanos Snap"] = self.finger_snap
    self.moves["rewind"] = self.rewind
    self.moves["true heal"] = self.true_heal
    self.moves["power stone shield"] = self.power_stone_shield
    self.specialmove  = 1

  def __str__(self): # returns a string when the object is called in a string context
      return(Thanos.name)

  def power_stone_shield(self,ememy):
    self.defence += self.energy * 50
    self.specialmove -= 1
    if self.specialmove <= 0:
      self.moves.pop("power stone shield")

  def true_heal(self,enemy):
    if self.energy <= 1:
      self.health += 50
    else:
      self.health += 50 * self.energy

  def finger_snap(self, enemy):
    if random.random() <= 0.5:
      self.attack(enemy, random.randint(50, 70))
    else:
      print_slowly("I am iron man")
      self.attack(self, 50)   

  def rewind(self, enemy):
    if self.energy >= 0.5:
      if self.health <= 100:
        self.health = 100
      else:
        self.energy = self.energy
      if self.defence <= 0:
        self.defence = 0
      else:
        self.energy = self.energy
      if self.energy <= 1:
        self.energy = 1
      else:
        self.energy = self.energy 
      if enemy.defence <= self.defence * 1.5:
        if random.random() <= 0.5:
          print_slowly(enemy.name+" resisted!")
          time.sleep(1)
        else:
          if enemy.defence >= self.defence *2.5:
            enemy.health = 100
            enemy.defence = 0
            enemy.energy = 1
            enemy.imortal = 0
      else:
        print_slowly("you are not strong enough right now")
        time.sleep(1)

  def smash(self, enemy):
    damage = random.randint(25, 45)
    self.attack(enemy, damage)

# Pikachu class
class Pikachu(Player):
  name = "Pikachu"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "Pikachu")
    self.name = Pikachu.name
    self.moves["thunder shock"] = self.thunder_shock
    self.moves["tail slap"] = self.tail_slap
    self.moves["pika block"] = self.pika_block
    self.moves["evolve"] = self.evolve
    self.specialmove = 2

# special move:
  def thunder_shock(self, enemy):
    
    damage = random.randint(40, 50)
    self.attack(enemy, damage)
    if random.random() <= 0.5: # 50% chance of lowering own health
      self.attack(self, 10)
  
  def tail_slap(self, enemy):
    self.attack(enemy, 35)
  
  def pika_block(self, enemy):
    self.imortal = 1
    time.sleep(1)
    self.attack(enemy, random.randint(5, 10))
  
  def evolve(self, enemy):
    self.name = "Raichu"
    self.health = 100
    print_slowly("Pikachu evolving ...")
    time.sleep(1)
    print_slowly("Pikachu evolved to Raichu!")
    time.sleep(1)
    self.moves.pop("thunder shock")
    self.moves.pop("tail slap")
    self.moves.pop("pika block")
    self.moves.pop("evolve")
    self.moves["thunder punch"] = self.thunder_punch
    self.moves["wild charge"] = self.wild_charge
    self.moves["raichu block"] = self.raichu_block
    self.moves["unevolve"] = self.unevolve
    self.specialmove1 = 2
  
  def thunder_punch(self, enemy):
    self.attack(enemy, random.randint(45, 55))
  
  def wild_charge(self, enemy):
    self.defence -= 2
    self.attack(enemy, random.randint(50, 60))
    if random.random() >= .5:
      self.attack(self,random.randint(10,25))
  
  def raichu_block(self, enemy):
    self.imortal = 1
    time.sleep(1)
    self.attack(enemy, random.randint(10, 15))
  
  def unevolve(self, enemy):
    self.name = "Pikachu"
    self.health = 100
    print_slowly("Raichu unevolved to Pikachu.")
    self.moves.pop("thunder punch")
    self.moves.pop("wild charge")
    self.moves.pop("raichu block")
    self.moves.pop("unevolve")
    self.moves["thunder shock"] = self.thunder_shock
    self.moves["tail slap"] = self.tail_slap
    self.moves["pika block"] = self.pika_block
    self.moves["evolve"] = self.evolve


# Hercules class
class Hercules(Player):
  name = "Hercules"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "Hercules")
    self.moves["arrow shots"] = self.arrow_shots
    self.moves["club strike"] = self.club_strike
    self.moves["equalize healths"] = self.equalize_healths

  def arrow_shots(self, enemy):
    if random.random() <= 0.25:
      self.attack(enemy, random.randint(50, 65))
    else:
      print_slowly("Hercules missed!")
  
  def club_strike(self, enemy):
    self.attack(enemy, 35)
  
  def equalize_healths(self, enemy):
    if self.health < enemy.health:
      print_slowly("This move will make Hercules's health equal to the enemy's.")
      time.sleep(1)
      difference = enemy.health - self.health
      self.health += difference


# Jedi class
class Jedi(Player):
  name = "Jedi"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "Jedi")
    self.moves.pop("attack") # makes it unusable
    self.moves["lightsaber slash"] = self.attack # rename basic attack move
    self.moves["force whirlwind"] = self.force_attack
    self.moves["battlemind"] = self.force_mind
    self.specialmove = 2 # track use of special move

# special support move (can only be used if energy is not too high)
  def force_mind(self, enemy):
    self.energy += 0.4 * self.energy # increase energy (attack/heal strength)
    print_slowly("Meditation increases the concentration and willpower of " + self.name)
    print_slowly(self.name + " has increased energy.")
    if self.energy >= 1.8: # if energy gets too high...
      self.moves.pop("battlemind")  # remove from dictionary of possible moves
      print_slowly("you can't use this move anymore")
  
  # special attack move (limited to 2 uses)
  def force_attack(self, enemy):
    self.attack(enemy, 60)
    self.specialmove -= 1 # subtract 1 use of specialmove
    if self.specialmove > 0:
      print_slowly(str(self.specialmove) + " time left to use this move.")
    else: # if 0 specialmove left
      time.sleep(1)
      print_slowly("You cannot use this move anymore.")
      self.moves.pop("force whirlwind") # remove from dict of possible moves

 
# winnerwannabe class
class winnerwannabe(Player):
  name = "winnerwannabe"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "winnerwannabe")
    self.moves["bow shot"] = self.bow_shot
    self.moves["axe hit"] = self.axe_crit
    self.moves["god apple"] = self.god_apple
    self.moves["enchant armor"] = self.enchant_armor
    self.moves["/kill"] = self.slash_kill
    self.moves["potion of weakness"] = self.potion_of_weakness
    self.moves["shield"] = self.shield
    self.moves["energy drain"] = self.energy_drain
    self.moves["sacrifice"] = self.sacrifice
    self.moves["potion of poison"] = self.potion_of_poison
    self.moves["corode"] = self.corode
    self.thorn_level = 0
    self.poison_thorn_level = 0
    self.energy_thorn_level = 0
    self.energy_poison_thorn_level = 0

  def corode(self,enemy):
    enemy.alpr += 5 * self.energy
    enemy.rounds_of_armor_loss += 2 * self.energy

  def potion_of_poison(self,enemy):
    enemy.dpr += 5 * self.energy
    enemy.poisoned_value += random.randint(4,6) * self.energy

  def sacrifice(self,enemy):
    while True:
      print_slowly("do you want to sacrifice health and gain energy (1) or sacrifice energy and gain health (2)\n")
      health_or_energy = input(">")
      if health_or_energy == "1":
        while True:
          print_slowly("would you like to choose how much health you will have left (1)  or how much damage you will take (2)\n")
          howleftorhowmuch = input(">")
          if howleftorhowmuch == "1":
            while True:
              print_slowly("how much health would you like to have left?\n")
              howleft = float(input(">"))
              trueleft = float(self.health - howleft)
              if howleft > 0:
                self.health = howleft
                self.energy += trueleft*self.energy*.005
                break
              else:
                print_slowly("that will kill you!\n")
                time.sleep(1)
            break
          elif howleftorhowmuch == "2":#how much damage you take
            try:
              da = float(input("chose how much damage you take: "))
            except:
              da = float(input("chose how much damage you take: "))
            while da >= self.health:
              print_slowly("that will kill you!")
              da = float(input("chose how much damage you take: "))
            self.health -= da
            self.energy += da * self.energy  * .005
            break
          else:
            print_slowly("pick 1 or 2\n")
          break
        break
      elif health_or_energy == "2":
        print_slowly("would you like to choose how much energy you will have left (1) or how much energy you will loose (2)\n")
        howleftorhowmuch = input(">")
        if howleftorhowmuch == "1":
          while True:
            print_slowly("how much energy do you want to have left?\n")
            howleft = float(input(">"))
            trueleft = float(self.energy - howleft)
            if self.energy >= 1:
              if self.health+trueleft*self.energy*100 > 0:
                self.health += trueleft*self.energy*200
                self.energy -= trueleft
                break
              else:
                print("that will kill you!")
                time.sleep(1)
            else:
              if self.health-trueleft*200 > 0:
                self.health += trueleft*200
                self.energy -= trueleft
                break
              else:
                print("that will kill you!")
                time.sleep("1")
          break
        elif howleftorhowmuch == "2":
          print_slowly("how much energy do you want to loose?\n")
          while True:
            try:
              el = float(input(">"))
            except:
              invalad()
              el = float(input(">"))
            if self.energy < 0:
              if self.health + el*200*self.energy > 0:
                self.health += el*200*self.energy
                self.energy -= el
                break
              else:
                print("that will kill you!")
                time.sleep(1)
            else:
              if self.health + el*200 > 0:
                self.health += el*200
                self.energy -= el
                break
              else:
                print("that will kill you!")
                time.sleep(1)
          break
        break
      else:
        print_slowly("please choose 1 or 2\n")


  def energy_drain(self,enemy):
    n = random.randint(10,30) * self.energy
    enemy.health -= n - enemy.defence / self.energy
    self.health += n * .5
    self.energy += n * .0025
    enemy.energy -= n * .005
    if enemy.defence > 0:
      enemy.defence -= 1

  def shield(self,enemy):
    self.imortal = 1

  def bow_shot(self, enemy):
    if random.random() <= 0.75:
      self.attack(enemy, random.randint(20,70))
    else:
      self.attack(enemy, random.randint(0,40))
  
  def axe_crit(self, enemy):
    if random.random() <= .5:
      print_slowly("it's a crit! ")
      self.attack(enemy, 50)
      if enemy.defence >= self.energy * 5:
        enemy.defence -= 5 * self.energy
      else:
        enemy.defence = 0
      if enemy.imortal > 0:
        enemy.imortal = 0
    else:
      self.attack(enemy,25)
      if enemy.defence >= self.energy:
        enemy.defence -= self.energy
      else:
        enemy.defence = 0
    
  def god_apple(self, enemy):
    n = (15)
    n *= self.energy
    if self.energy >= 0:
      self.defence += 3 * self.energy
      self.health += n
      print_slowly(self.name+"ate a god apple. all stats increased.")
      time.sleep(1)
      self.energy += .01 * self.energy
      self.regen_energy_value += 4 * self.energy
      self.health_regened_per_round += 5 * self.energy
      self.regen_health_value += 4 * self.energy
    else:
      self.health += 0

  def enchant_armor(self, enemy):
    multi = 1
    s = ""
    f = (random.randint(10,20))
    f *= self.energy
    if self.defence >= 100:
      multi = .5
    if f >= 0:
      self.defence += f*multi # makes defence go up by f
    else:
      self.defence += 0
    if self.defence >= 100:
      s = "s"
    print_slowly('defence went up by %.2f' % (f))
    thorn_type = random.randint(1,4)
    if thorn_type == 1:
      self.thorn += .025*self.energy/multi
      self.thorn_level += 1 / multi
      print_slowly("\nyou have "+str(self.thorn_level)+" level"+s+" in thorns now!")
    elif thorn_type == 2:
      self.poison_thorn += .5*self.energy/multi
      self.poison_thorn_level += 1 / multi
      print_slowly("\nyou have "+str(self.poison_thorn_level)+" level"+s+" in poison thorns now!")
    elif thorn_type == 3:
      self.energy_thorn += .01*self.energy/multi
      self.energy_thorn_level += 1 / multi
      print_slowly("\nyou have "+str(self.energy_thorn_level)+" level"+s+" in energy thorns now!")
    elif thorn_type == 4:
      self.energy_losses_thorns += .5*self.energy/multi
      self.energy_poison_thorn_level += 1 / multi
      print_slowly("\nyou have "+str(self.energy_poison_thorn_level)+" level"+s+" in energy poison thorns now!")
    time.sleep(2)

  def slash_kill(self,enemy):
    self.health = 0
    print_slowly("killed "+self.name+"\n")
    print_slowly(self.name+" fell out of the world")
    time.sleep(1)

  def potion_of_weakness(self,enemy):
    enemy.energy -= self.energy * .2
    enemy.elpr += .005 * self.energy 
    enemy.alpr += 2 * self.energy
    enemy.rounds_of_armor_loss += 2 * self.energy
    enemy.energy_losses += 4 * self.energy
    if enemy.defence >= 1 * self.energy:
      enemy.defence -= 1 * self.energy
    else:
      enemy.defence = 0

# Blue_Fire64 class
class Blue_Fire64(Player):
  name = "Blue_Fire64"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "Blue_Fire64")
    self.moves["/kill"] = self.slash_kill
    self.moves["burn"] = self.burn
    self.moves["stab"] = self.stab
    self.moves["bone shield"] = self.bone_shild
    self.moves["god apple"] = self.god_apple
    self.moves["armor break"] = self.armor_break
    self.moves["shield"] = self.shield
    self.moves["enchant armor"] = self.enchant_armor
    self.moves["accelerate regeneraton"] = self.accelerate_regeneration
    self.thorn_level = 0
    self.poison_thorn_level = 0
    self.energy_thorn_level = 0
    self.energy_poison_thorn_level = 0

  def accelerate_regeneration(self,enemy):
    self.rohg += .2 * self.energy
    self.roeg += .2 * self.energy

  def enchant_armor(self, enemy):
    multi = 1
    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""
    f = (random.randint(10,20))
    f *= self.energy
    if self.defence >= 100:
      multi = .5
    if f >= 0:
      self.defence += f*multi # makes defence go up by f
    else:
      self.defence += 0
    if self.thorn_level >= 1:
      s1 = "s"
    if self.poison_thorn_level >= 1:
      s2 = "s"
    if self.energy_thorn_level >= 1:
      s3 = "s"
    if self.energy_poison_thorn_level >= 1:
      s4 = "s"
    print_slowly('defence went up by %.2f' % (f))
    thorn_type = random.randint(1,4)
    if thorn_type == 1:
      self.thorn += .025*self.energy/multi
      self.thorn_level += 1 / multi
      print_slowly("\nyou have "+str(self.thorn_level)+" level"+s1+" in thorns now!")
    elif thorn_type == 2:
      self.poison_thorn += .5*self.energy/multi
      self.poison_thorn_level += 1 / multi
      print_slowly("\nyou have "+str(self.poison_thorn_level)+" level"+s2+" in poison thorns now!")
    elif thorn_type == 3:
      self.energy_thorn += .01*self.energy/multi
      self.energy_thorn_level += 1 / multi
      print_slowly("\nyou have "+str(self.energy_thorn_level)+" level"+s3+" in energy thorns now!")
    elif thorn_type == 4:
      self.energy_losses_thorns += .5*self.energy/multi
      self.energy_poison_thorn_level += 1 / multi
      print_slowly("\nyou have "+str(self.energy_poison_thorn_level)+" level"+s4+" in energy poison thorns now!")
    time.sleep(2)

  def shield(self,enemy):
    self.imortal = 1

  def slash_kill(self, enemy):
    self.health = 0

  def burn(self, enemy):
    self.attack(enemy, 35)
    enemy.dpr += 5
    enemy.energy -= .075 * self.energy
    enemy.poisoned_value += 4

  def stab(self, enemy):
    if random.random() <= 0.75:
      self.attack(enemy, random.randint(20,80))
    else:
      self.attack(enemy, random.randint(0,40))

  def bone_shild(self,enemy):
    f = (random.randint(5,15))
    f *= self.energy
    self.defence += f # makes defence go up by f
    self.attack(enemy, 10)
    print_slowly('defence went up by %s' % (f))

  def god_apple(self, enemy):
    
    self.defence += self.energy * 3
    n = (10)
    n *= self.energy
    self.health += n #make it so that this heals 10 health every round for 4 rounds if posible
    print_slowly(self.name+" ate a god apple. all stats increased.")
    self.energy += .01
    self.regen_energy_value += 4
    self.regen_health_value += 4
  
  def armor_break(self,enemy):
    enemy.imortal = 0
    self.attack(enemy,10)
    if enemy.defence <= 50:
      enemy.defence = 0
      print_slowly(enemy.name+"'s defence is now zero")
    else:
      enemy.defence -= 50
      print_slowly(enemy.name+"'s defence is now "+enemy.defence)

#coral guardian class
class coral_guardian(Player):
  name = "coral guardian"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "coral guardian")
    self.moves["ocean's light"] = self.ocean_light
    self.moves["protecter of the tomb"] = self.protec_the_tomb

  def protec_the_tomb (self,enemy):
    self.attack(enemy, random.randint(25,45))

  def ocean_light (self,enemy):
    self.energy += 0.05 * self.energy
    self.defence += random.randint(5,20) * self.energy
  
#covid_vacine class
class covid_vaccine(Player):
  name = "covid vaccine"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "covid vaccine")
    self.moves["antibodies"] = self.antibodies
    self.moves["pureify"] = self.pureify
    self.moves["imune system"] = self.imune_system
	 
  def imune_system(self,enemy):
    self.defence += 10 * self.energy

  def pureify(self,enemy):
    self.energy += .1 * self.energy
    self.health += 25 * self.energy
    self.poisoned_value = 0
    self.energy_losses = 0
    self.rounds_of_armor_loss = 0

  def antibodies(self,enemy):
    self.attack(enemy, random.randint(20,50))

# Voldemort class
class Voldemort(Player):
  name = "Voldemort"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "Voldemort")
    self.moves.pop("attack")
    self.moves["crucio"] = self.attack
    self.moves["killing curse"] = self.avadakedavra
    self.moves["regeneration"] = self.regeneration
    self.moves["create Horcrux"] = self.create_Horcrux
    self.specialmove = 7

  def regeneration(self,enemy):
    self.regen_health_value += 6 * self.energy
    self.health_regened_per_round += 5

  def avadakedavra(self, enemy):
    print_slowly("AVADA KEDAVRA!")
    time.sleep(1) # wait 1 second
    if random.random() <= 0.75: # 3/4 chance attack will succeed
      self.attack(enemy, 50)
    else: # 1/4 chance that it will rebound
      print_slowly("Voldemort's curse rebounded!")
      self.attack(self, 50) # attacks himself!
  
  def create_Horcrux(self, enemy):
    if self.health <= 50:
      difference = 100 - self.health
      self.health += difference
      print_slowly("Voldemort got {} more health.".format(difference))
    else:
      self.health += 50
      print_slowly("Voldemort got 50 more health.")
      self.specialmove -= 1 # subtract 1 use of specialmove
    if self.specialmove > 0:
      print_slowly(str(self.specialmove) + " time left to use this move.")
    else: # if 0 specialmove left it makes the move imposible
      time.sleep(1)
      print_slowly("You cannot use this move anymore.")
      self.moves.pop("create Horcrux")

#mewtwo class
class Mewtwo(Player): 
  name = "Mewtwo"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "Mewtwo")
    self.moves["doom desire"] = self.crush_grip
    self.moves["spacial rend"] = self.spacial_rend
    self.moves["psycho boost"] = self.psycho_boost

  def spacial_rend(self, enemy):
    damage = random.randint(50, 70)
    self.attack(enemy, damage)

  def crush_grip(self, enemy):
    damage = random.randint(25, 35)
    self.attack(enemy, damage)
    if random.random() < 0.5:
      self.attack(self, random.randint(5, 15))

  def psycho_boost(self, enemy):
      	zdamage = random.randint(30,80)
      	self.attack(enemy, damage)

#medusa class
class Medusa(Player): 
  name = "Medusa"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "Medusa")
    self.moves["claw slice"] = self.attack
    self.moves["stone gaze"] = self.stone_attack
    self.moves["snake bite"] = self.snake_bite
    self.thorn = .1
    self.energy_thorn = .01
    self.poison_thorn = .5
    self.energy_losses_thorns = .5

  def stone_attack(self, enemy):
    print_slowly("DUCK!")
    time.sleep(1)
    if random.random() <= 0.5:
      self.attack(enemy, 50)
    else:
      print_slowly("The attack did nothing!")
  
  def claw_slice(self, enemy):
    self.attack(enemy, 35)
  
  def snake_bite(self, enemy):
    if random.random() <= 0.6:
      self.attack(enemy, random.randint(40, 45))
      enemy.poisoned_value += random.randint(1,6)
      enemy.dpr += 5
    else:
      time.sleep(1)
      print_slowly("The bite wasn't that bad!")
      self.attack(enemy, random.randint(15, 25))

#teacher class
class teacher(Player): 
  name = "teacher"
  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "teacher")
    self.moves["ruler smack"] = self.ruler_smack
    self.moves["apple"] = self.apple
    self.moves["pencil stab"] = self.pencil_stab

  def ruler_smack(self, enemy):
    self.attack(enemy,random.randint(30,45))

  def apple(self, enemy):
    if random.random() <= 0.75:
      apple_health = random.randint(25,50)
      self.health += apple_health
      print_slowly("healed {} more health.\n".format(apple_health))
      time.sleep(1)
    else:
      if random.random() <= 0.75:
        print_slowly("it was rotten\n")
        rotten_apple_health = random.randint(0,30)
        self.health += rotten_apple_health
        print_slowly("healed {} more health.\n".format(rotten_apple_health))
        time.sleep(1)
      else:
        print_slowly("it was rotten\n")
        rotten_apple_health = random.randint(0,30)
        self.health -= rotten_apple_health
        print_slowly("you took {} damage.\n".format(rotten_apple_health))
        time.sleep(1)

  def pencil_stab(self, enemy):
    self.attack(enemy, 35)

#dummy class
class dummy(Player): 
  name = "dummy"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "dummy")
    self.moves.pop("attack")
    self.moves.pop("rest")
    self.moves.pop("heal")
    self.moves.pop("defend")
    self.moves["attack self"] = self.attack_self
    self.moves["gain energy"] = self.gain_energy
    self.moves["lose energy"] = self.lose_energy   

  def lose_energy (self,enemy):
    self.energy -= .1

  def attack_self(self, enemy):
    self.attack(self, 10)

  def gain_energy(self, enemy):
    self.energy += self.energy * .1

#spinal millipede class
class spinal_millipede(Player):
  name = "spinal millipede"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "spinal millipede")
    self.moves["steel skin"] = self.steel_skin
    self.moves["needle barrage"] = self.needle_barrage
    self.defence = 20

  def steel_skin (self,enemy):
    self.defence += random.randint(5,30) * self.energy

  def needle_barrage (self,enemy):
    self.attack(enemy, random.randint(25,45))

#covid-19 class
class covid19(Player):
  name = "covid-19"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "covid-19")
    self.moves["infect"] = self.infect
    self.moves["poison"] = self.poison
    self.moves["virus"] = self.virus

  def virus(self,enemy):
    self.attack(enemy, 50)

  def infect(self,enemy):
    enemy.poisoned_value += 4 * self.energy
    enemy.energy -= .05 * self.energy

  def poison(self,enemy):
    enemy.poisoned_value += 4 * self.energy
    enemy.poisoned_value += 10 * self.energy

#firebeast class
class firebeast(Player):
  name = "firebeast"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "firebeast")
    self.moves["fire beam"] = self.fire_beam
    self.moves["beast slash"] = self.beast_slash
    self.moves["spiritual flame"] = self.spirit_flame
    self.moves["wings of flame"] = self.wings_of_flame

  def wings_of_flame(self,enemy):
    n = random.randint(10,20) # random number for health/defense increase 
    n *= self.energy # multiplied by energy level
    if n >= 0:
      self.defence += n 
      self.health += n
      d = str(n)
      print_slowly(self.name+" gained "+d+" defense and health")
      time.sleep(1)
    else:
      self.defence += 0
      print_slowly(self.name+"gained 0 defense and health")
      time.sleep(1)

  def spirit_flame(self,enemy):
    self.energy += .025
    self.attack(enemy, 15)
    self.defence += 10

  def beast_slash(self,enemy):
    self.attack(enemy, random.randint(40,50))

  def fire_beam(self,enemy):
    self.attack(enemy, random.randint(20,40))
    enemy.energy -= .05

#crawler class
class crawler(Player):
  name = "crawler"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "crawler")
    self.moves["blazeing rage"] = self.blazeing_rage
    self.moves["bloody onslaught"] = self.bloody_onslaught

  def bloody_onslaught(self,enemy):
    self.attack(enemy,50)

  def blazeing_rage(self,enemy):
    self.energy += .075 * self.energy

#withered stone class
class withered_stone(Player):
  name = "withered stone"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "withered stone")
    self.defence = 5
    self.moves["pound"] = self.pound
    self.moves["absorb"] = self.absorb
  
  def pound(self,enemy):
    self.attack(enemy,20)
  
  def absorb(self,enemy):
    enemy.health -= 10
    enemy.energy -= .2
    if self.energy > 0.5:
      self.health += 10 * self.energy
    else:
      self.health += 5
    if self.energy > 0.5:
      self.energy += .2*self.energy
    else:
      self.energy += .01

#moss growth class
class moss_growth(Player):
  name = "moss growth"

  def __init__(self, player_or_bot):
    Player.__init__(self, player_or_bot, "moss growth")
    self.moves["air slash"] = self.air_slash

  def air_slash(self,enemy):
    self.attack(enemy,random.randint(50,70))