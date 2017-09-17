# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:38:54 2017

@author: gmfk07
"""
def whatDo(daysLeft, suspect1, suspect2, suspect3, suspect4, mapJobs, mapQ1, mapQ2, murderWeapon):
    print("You have " + str(daysLeft) + " days left in your investigation.")
    print("What will you do today?")
    print("")
    print("1) Investigate the crime scene")
    print("2) Question " + suspect1.getName())
    print("3) Question " + suspect2.getName())
    print("4) Question " + suspect3.getName())
    print("5) Question " + suspect4.getName())  
    
    while True:
        try:
            x = int(input("Enter a number 1-5: "))
            if x > 5 or x < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid number, try again.")
            
    print("")
    if x == 2:
        question(suspect1, mapJobs, mapQ1, mapQ2, murderWeapon)
        
def question(suspect, mapJobs, mapQ1, mapQ2, murderWeapon):
    arc = suspect.getArchetype()
    job = suspect.getJob()
    line1 = mapJobs[job][arc]
    line2 = mapQ1[job][arc]
    line3 = mapQ2[job][arc]
    suspectName = suspect.getName()
    
    if suspect.getGender() == "M":
        suspectPronoun = "he"
        suspectPronoun2 = "him"
        suspectPerson = "man"
        suspectPossessive = "his"
    if suspect.getGender() == "F":
        suspectPronoun = "she"
        suspectPronoun2 = "her"
        suspectPerson = "woman"
        suspectPossessive = "hers"
    
    line1 = line1.replace("name", suspectName)
    line1 = line1.replace("man/woman", suspectPerson)
    line1 = line1.replace("he/she", suspectPronoun)
    line1 = line1.replace("his/hers", suspectPossessive)
    line1 = line1.replace("him/her", suspectPronoun2)
    print(line1)
    print("")
    print("What do you ask them?")
    print("1) What did you see?")
    print("2) Who did you see?")
    
    while True:
        try:
            x = int(input("Enter a number 1-2: "))
            if x > 2 or x < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid number, try again.")
    
    if x == 1:
        extraitem = ""
        
        if murderWeapon == "gun":
            weapon = "a gun"
        if murderWeapon == "knife":
            weapon = "a knife"
        if murderWeapon == "poison":
            weapon = "some poison"
        if murderWeapon == "club":
            weapon = "a club"
        if murderWeapon == "strangling":
            weapon = "some rope"
            
        line2 = line2.replace("weapon", weapon)
        if extraitem == "":
            line2 = line2.partition("XXX")[0]
        else:
            line2 = line2.partition("XXX")[0] + line2.partition("XXX")[2]
        print(line2)
        
    