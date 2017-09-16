# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:04:14 2017

@author: gmfk07
"""
import random, intro
#Randomize values
random.seed()

class victim():
    def __init__(self, name, trait1, trait2, age):
        self.name = name
        self.trait1 = trait1
        self.trait2 = trait2
        self.age = age
        
    def getName(self):
        return self.name
    
    def getTrait1(self):
        return self.trait1
    
    def getTrait2(self):
        return self.trait2
    
    def getAge(self):
        return self.age

#Day
mts = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
month = random.choice(mts)
day = random.randint(1,28)
#MurderTime
murderHour = random.choice((11,12,1,2,3,4))
if murderHour > 10:
    murderTOD = "pm"
else:
    murderTOD = "am"
#Murder Details
murderWeapon = random.choice(("gun","knife","poison","club","strangling"))
t1 = random.choice(("rich", "politician", "average"))
t2 = random.choice(("friend", "boss child", "good"))
age = random.randint(23,42)
murderVictim = victim("Andrew Hoyt", t1, t2, 69)
murderLocation = random.choice(("alleyway", "warehouse", "hotel room", "house"))
#Complications/plot twists
complicationCount = 2;
complications = ("wrong weapon", "wrong location", "wrong identity", "missing evidence", "planted evidence", "suspect gone")

intro.intro(murderVictim, month, day, murderWeapon, murderLocation, murderHour, murderTOD)