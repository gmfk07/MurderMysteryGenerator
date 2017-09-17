# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:04:14 2017

@author: gmfk07
"""
import random, intro, routine, archetypeInit
#Randomize values
random.seed()

# Creates a list containing 5 lists, each of 16 items, all set to ""
w = 5
h = 16
mapJobs = [["" for x in range(w)] for y in range(h)] 
mapQ1 = [["" for x in range(w)] for y in range(h)] 
mapQ2 = [["" for x in range(w)] for y in range(h)] 
mapArchetype = [[""for x in range(w)] for y in range(w)]
arcList = [0,1,2,3,4]

#Populate mapJobs
archetypeInit.archetypeInit(mapJobs, mapQ1, mapQ2, mapArchetype)

#mapQ3 = [[0 for x in range(w)] for y in range(h)] 
class victim():
    def __init__(self, name, trait1, trait2, age, gender):
        self.name = name
        self.trait1 = trait1
        self.trait2 = trait2
        self.age = age
        self.gender = gender
        
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
    def __init__(self, name, archetype, job, gender, timeFound):
        self.name = name
        self.archetype = archetype
        self.job = job
        self.gender = gender
        self.timeFound = timeFound
    def getName(self):
        return self.name
    def getArchetype(self):
        return self.archetype
    def getJob(self):
        return self.job
    def getGender(self):
        return self.gender
    def getTime(self):
        return self.timeFound
    
def genSuspect():
    name = genName()
    archetype = arcList.pop(random.randint(0,len(arcList)-1))
    job = jobList.pop(random.randint(0,len(jobList)-1))
    gender = random.choice(("M","F"))
    timeFound = murderHour + random.randint(1,3)
    if timeFound > 12:
        timeFound -= 12
    return suspect(name, archetype, job, gender, timeFound)
    
def genName():
    firstNames = ["Caelan", "Jean", "Alexis", "Niaz", "Carmen", "Fey", "Cameron", "Morgan", "Sydney", "Tristan", "Yuri", "Inge", "Blaine", "Rene", "Anwar", "Zulema"]
    lastNames =  ["Hartley", "Hernandez", "Hoyt", "Price", "Goosens", "Oakley", "Leung", "Smith", "Menzies", "Kouriatchev", "Shalhoub", "Bishara"]
    return random.choice(firstNames) + " " + random.choice(lastNames)
#Day
mts = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
month = random.choice(mts)
day = random.randint(1,28)
#MurderTime
murderHour = random.choice((11,12,1,2))
if murderHour > 11:
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
#Job tracking
modifier = 0
if murderLocation == "warehouse":
    modifier += 4
if murderLocation == "hotel room":
    modifier += 8
if murderLocation == "house":
    modifier += 12
jobList = [modifier, modifier+1, modifier+2, modifier+3]
#Complications/plot twists
complicationCount = 2;
complications = ("wrong weapon", "wrong location", "wrong identity", "missing evidence", "planted evidence", "suspect gone")
#Suspects
suspects = [genSuspect(),genSuspect(),genSuspect(),genSuspect()]
murderer = random.choice(suspects)
#Investigation days
daysLeft = 3

if random.choice((True, True, False)):
    initLeave = routine.leaveItem(murderer)
else:
    initLeave = ""

if (murderHour > 12):
    m1 = murderHour - 12
else:
    m1 = murderHour
if (murderHour > 11):
    m2 = murderHour + 1 - 12
else:
    m2 = murderHour + 1
if (murderHour > 10):
    m3 = murderHour + 2 - 12
else:
    m3 = murderHour + 2
if (murderHour > 9):
    m4 = murderHour + 3 - 12
else:
    m4 = murderHour + 3
dictItem = {m1:initLeave, m2:initLeave, m3:initLeave, m4:initLeave} 

for s in suspects:
    if s != murderer and random.choice((True, True, False)):
        counter = 1
        while counter <= 3:
            tm = s.getTime() + counter - 1
            if tm > 12:
                tm -= 12
            if tm in dictItem:
                if counter == 1:
                    firstOne = dictItem[tm]
                else:
                    if dictItem[tm] == firstOne:
                        dictItem[tm] = routine.leaveItem(s)
            counter += 1

intro.intro(murderVictim, month, day, murderWeapon, murderLocation, murderHour, murderTOD)
while daysLeft > 0:
    routine.whatDo(daysLeft, suspects[0], suspects[1], suspects[2], suspects[3], mapJobs, mapQ1, mapQ2, mapArchetype, murderWeapon, murderVictim, murderer, dictItem)
    daysLeft -= 1