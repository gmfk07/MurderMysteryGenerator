# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:04:14 2017

@author: gmfk07
"""
import random
#Randomize values
random.seed()
#Time
hour = random.randint(1,12)
minute = random.randint(0,60)
TOD = random.choice("am","pm") 