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

#Time
hour = random.randint(1,12)
minute = random.randint(0,59)
TOD = random.choice("am","pm")
#MurderTime
murderHour = random.choice(11,12,1,2,3,4)
murderMinute = random.randint(0,59)
if murderHour > 10:
    murderTOD = "pm"
else:
    murderTOD = "am"
#MurderWeapon
murderWeapon = random.choice("gun","knife","poison","club","strangling")
murderVictim = victim("Andrew Hoyt", "rich", "friend")