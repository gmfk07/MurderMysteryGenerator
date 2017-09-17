# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:51:28 2017

@author: gmfk07
"""
import random

def archetypeInit(mapJobs):
    amt = 16
    dimwit = [0 for x in range(amt)]
    dimwit[0] = '“Oh! Well, y’see, I was jus’ walking by the alleyway and I saw the dead body. I was on my way to… something… or another, I forgot. In any case, seeing the corpse snapped me out of it.”'
    dimwit[1] = '“Yeah, well, I was trying to get back home. I live in an… what do you call, the big buildings with… an APARTMENT! Yeah, thassit. Anyways, that’s when I stumbled upon the crime scene.”'
    dimwit[2] = '“I was jus’ minding my own business… walking by the alleyway… not doing anythin’ illegal. Or suspicious.” You check their file, and note that they have a history of committing petty crimes. “So yeah, that’s when I stumbled upon the crime scene, and then there’s a bunch of popo telling me I’m a suspect now. Go figure.”'
    dimwit[3] = '“Y’see, I was getting my clothes at the laundromat. I basically sleep during the day, so the 24-hour laundry place is where I get all my clothes cleaned a’least once a year. Then’s when I saw that corpse. Real shame, what happened to them.”'
    dimwit[4] = '“Welp, I’m a supervisor in this here warehouse. Don’t really know what that entails, just that I get paid more than before. I was doin’ the night shift, and I found the body next to some crate.”'
    dimwit[5] = '“I was workin’ the night shift at this here warehouse. Just puttin’ things in boxes, no big deal, when I just see this dead body next to one of the piles. Pretty freaky, if you ask me.”'
    dimwit[6] = '“I’m a security guard here, so I was keepin’ watch. Then, all of a sudden, I see something out of the corner of my eye, so I go to investigate, like a good guard. Sure enough, it was the body.”'
    dimwit[7] = '“I work the forklift. It’s a slow job, but the pay’s good. Well, the pay’s bad. The pay’s garbage, actually. While I was doin’ my darn job, I nearly ran over someone  lying on the floor. Then I realized they were dead, and that I had stumbled on a crime scene.”'
    dimwit[8] = '“I’m the hired help here, an’ I try to clean up good. Imagine how shocked I was when I was getting some last-minute work done, an’ saw a body right in the master bedroom.”'
    dimwit[9] = '"I knocked on the door to my neighbor’s house, lookin’ to borrow some salt for my late-night lasagna. The door just kind of opened on its own, so I checked up on my good neighbor friend, just to find him dead."'
    dimwit[10] = '"So I was doing some work at the front desk, checkin’ registration schedules and all that, when I realized that someone was supposed to check out but didn’t. So I went to the room and saw the reason why: they were dead."'
    dimwit[11] = "parrot"
    dimwit[12] = '"Welp, I’m the nanny of this household… though I prefer the term babysitter. I was tuckin’ the kiddies in, then I realized that I ain’t seen the head of household in quite some time. So I checked up on ‘em, and… they were dead on the ground."'
    dimwit[13] = '"I was walkin’ around the floor I was stayin’ in at the hotel, lookin’ for the pool. I saw a room that was cracked open just a peek, and inside was a dead body. Really spooked me, I tell ya."'
    dimwit[14] = '"I was in the neighborhood and decided to check up on my good ol’ friend, given that they barely ever sleep. But their front door was open, and I got mighty scared, so I tried to find them… and all I could find was their body."'
    dimwit[15] = '"I’m the… victim’s spouse, ayup. I woke up late at night and tried to look for ‘em, just to make sure they weren’t cheatin’ on me or anythin’... and instead, I found ‘em dead. Oh, god, why?!"'
    
    
    #leave this at the bottom, please!
    counter = -1
    for i in mapJobs:
        counter += 1
        s = "A " + random.choice(("rather lanky", "stout", "twitching")) + " man/woman shuffles into your office, finding a seat quickly. “Heyyy,” says name, “howz’it goin?” You tell them about your investigation and ask them about what they saw the night of the murder. They look at you without blinking for a few seconds, and just as you’re about to repeat yourself, they snap back into it. "
        mapJobs[counter][3] = s + dimwit[counter]