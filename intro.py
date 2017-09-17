# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:20:46 2017

@author: gmfk07
"""
import random

def intro(victim, month, day, murderWeapon, murderLocation, murderHour, murderTOD):
    name = victim.getName()
    t1 = victim.getTrait1()
    t2 = victim.getTrait2()
    age = victim.getAge()
    gender = victim.getGender()
    
    if gender == "M":
        title = "Mr."
    if gender == "F":
        title = "Mrs."
    
    if t1 == "rich":
        t1line = "rather wealthy."
    if t1 == "politician":
        t1line = "climbing up the ranks to be a successful politician."
    if t1 == "average":
        t1line = "worked a decent-paying job."
    
    if t2 == "friend":
        t2line = "You remember them fondly - they were your best friend back in college."
    if t2 == "boss child":
        t2line = "The boss handed you the case personally, making you promise to catch the culprit who killed their " + random.choice(("only child.","eldest child."))
    if t2 == "good":
        t2line = "It seems the whole city is grieving over the sudden loss of someone that special."
 
    if murderWeapon == "gun":
        mword = "shot"
    if murderWeapon == "knife":
        mword = "stabbed"
    if murderWeapon == "poison":
        mword = "poisoned"
    if murderWeapon == "club":
        mword = "bludgeoned"
    if murderWeapon == "strangling":
        mword = "strangled"
        
    if murderLocation == "alleyway":
        mline = "some old alleyway that nobody bothered to renovate."
    if murderLocation == "warehouse":
        mline = "a warehouse down by the docks."
    if murderLocation == "hotel room":
        mline = "a hotel room on the nicer side of town."
    if murderLocation == "house":
        mline = "the victim’s own house."
    
    print ("This city is " + random.choice(("crime-ridden", "dark")) + " and " + random.choice(("brutal", "seedy")) + " and you " + random.choice(("love it", "hate it", "got used to it")) + ".")
    print ("You got your most recent case handed to you unceremoniously - solving the murder of " + title + " " + name + ". " + t2line)
    print ("On " + month + " " + str(day) + " at " + str(murderHour) + " " + murderTOD + ", " + name + " was murdered, and the autopsy report suggests they were " + mword + ". At the time of their death, they were " + str(age) + " and " + t1line + " The crime scene is " + mline)
    print ("Nothing left to do now but solve the case and then " + random.choice(("go on that vacation you’ve always wanted", "retire", "go back to work next week")) + ".")