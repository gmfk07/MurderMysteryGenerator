# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:04:14 2017

@author: gmfk07
"""
import random
#Randomize values
random.seed()

class victim(Object):
    def __init__(self, name, trait1, trait2):
        self.name = name
        self.trait1 = trait1
        self.trait2 = trait2

#Day
month = random.choice("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
day = random.randint(1,28)
#MurderTime
murderHour = random.choice(11,12,1,2,3,4)
murderMinute = random.randint(0,59)
if murderHour > 10:
    murderTOD = "pm"
else:
    murderTOD = "am"
#Murder Details
murderWeapon = random.choice("gun","knife","poison","club","strangling")
t1 = random.choice("rich", "politician", "average")
t2 = random.choice("friend", "boss child", "good")
murderVictim = victim("Andrew Hoyt", "rich", "friend")
murderLocation = ("alleyway", "warehouse", "hotel room", "house")
#Complications/plot twists
complicationCount = 2;
complications = ("wrong weapon", "wrong location", "wrong identity", "missing evidence", "planted evidence", "suspect gone")