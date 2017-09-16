# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:04:14 2017

@author: gmfk07
"""
import random, intro, routine
#Randomize values
random.seed()

# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 6, 16;
mapJobs = [[0 for x in range(w)] for y in range(h)] 
mapQ1 = [[0 for x in range(w)] for y in range(h)] 
mapQ2 = [[0 for x in range(w)] for y in range(h)] 
#mapQ3 = [[0 for x in range(w)] for y in range(h)] 

class victim():
    def __init__(self, name, trait1, trait2, age, gender):
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
    
    def getGender(self):
        return self.gender

class suspect():
    def __init__(self, name, archetype, job, gender):
        self.name = name
        self.archetype = archetype
        self.job = job
    def getName(self):
        return self.name
    def getArchetype(self):
        return self.archetype
    def getJob(self):
        return self.job
    def getGender(self):
        return self.gender
    
def genSuspect():
    name = genName()
    archetype = random.randint(0,w-1)
    job = random.randint(0, h-1)
    gender = random.choice(("M","F"))
    return suspect(name, archetype, job, gender)
    
def genName():
    return "Andrew Hoyt"
    
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
murderVictim = victim("Andrew Hoyt", t1, t2, age, "M")
murderLocation = random.choice(("alleyway", "warehouse", "hotel room", "house"))
#Complications/plot twists
complicationCount = 2;
complications = ("wrong weapon", "wrong location", "wrong identity", "missing evidence", "planted evidence", "suspect gone")
#Suspects
suspects = [genSuspect(),genSuspect(),genSuspect(),genSuspect()]
#Investigation days
daysLeft = 3

intro.intro(murderVictim, month, day, murderWeapon, murderLocation, murderHour, murderTOD)
routine.whatDo(daysLeft, suspects[0], suspects[1], suspects[2], suspects[3])