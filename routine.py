# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:38:54 2017

@author: gmfk07
"""

def whatDo(daysLeft, suspect1, suspect2, suspect3, suspect4):
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