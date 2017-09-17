# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:51:28 2017

@author: gmfk07
"""
import random

=======
def archetypeInit(mapJobs, mapQ1, mapQ2, mapArchetype):
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

    lethargic = [0 for x in range(amt)]
    lethargic[0] = '"At about that time I was walking through the alley when I witnessed the crime. I’m a resident from around the corner, so I take that route fairly frequently… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[1] = '"At about that time I was walking back to my apartment when I saw', victimName,'on the ground… It was almost surreal… Did you need me to be more specific? Sorry, I’m not much for conversations…”'
    lethargic[2] = '"At about that time I was walking through the alley when I witnessed the crime. I’m not from around there, so it was my first time taking that route… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[3] = '"At about that time I was walking back from the laundromat when I saw', victimName ,'on the ground… It was almost surreal… Did you need me to be more specific? Sorry, I’m not much for conversations…”'
    lethargic[4] = '"At about that time I was just checking on things in the warehouse when I noticed', victimName ,'on the ground…  It was almost surreal… Did you need me to be more specific? Sorry, I’m not much for conversations…”' 
    lethargic[5] = '"At about that time I was just checking on things in the warehouse when I noticed',victimName ,'on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[6] = '"At about that time I was just making sure nothing suspicious was going on in the warehouse when I noticed',victimName ,'on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[7] = '"At about that time I was just shutting down the lift when I noticed', victimName,'on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[8] = '"At about that time I was cleaning the room when I noticed', victimName,'on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[9] = '"At about that time I was trying to pay', murdervictim.getName() ,'a visit, and when I got to the door, I realized it was unlocked. I walked in, and saw', victimName ,'on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[10] = '"At about that time I was The cleaning staff alerted me of the situation, and when I went to investigate, I saw victim on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    #below is the sacred parrot, what say you?
    lethargic[11] = "parrot"
    lethargic[12] = '"At about that time I was putting the baby down for a nap when I heard this abhorrent screech. I walked downstairs to investigate and saw', victimName,'on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[13] = '"At about that time I was just relaxing on my front porch when I heard a noise from', victimName+'’s house. I walked over to investigate and found that the front door was unlocked. When I walked in, I saw', victimName,'on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[14] = '"At about that time I was in town for the week and staying with', victimName +'. I heard a loud noise and walked downstairs to investigate when I saw', victimName,'on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[15] = '"At about that time I was I was relaxing in the living room when I heard a loud scream. I walked towards the sound to investigate and I saw', victimName,'on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    
    #', murdervictim.getName() ,'
    #', victimName,'
    
    narc = [0 for x in range(amt)]
    narc[0] = '"At about that time I was walking towards my new condominium! It’s just around the corner, and you literally could not find a better place to live! It’s close to transportation, park areas, restaurants, bars, you name it, it’s got it! I’m so good at home-searching. Anyways, I saw', victimName,'lying on the ground right after I updated my snapchat, and it scared me half to death."'
    narc[1] = '"At about that time I was walking towards my new apartment! You literally could not find a better place to live! It’s close to transportation, park areas, restaurants, bars, you name it, it’s got it! I’m so good at home-searching. Anyways, I saw', victimName,'lying on the ground right after I updated my snapchat, and it scared me half to death."'
    narc[2] = '"At about that time I was Walking around in the neighborhood. I was considering living here a couple years ago, but after I saw', victimName,'lying on the ground, it’s clear I made the right choice!  Good thing I’m so good at home-searching…"'
    narc[3] = '"At about that time I was walking towards the new laundromat because I love supporting my local businesses! I’m much more socially-conscious than other people, clearly. Anyways, I saw', victimName,'lying on the ground, and I was scared nearly half to death!"'
    narc[4] = '"At about that time I was keeping tabs on my underlings, I mean employees. When I making my rounds, however, I stumbled upon ', victimName+'’s body. It scared me half to death!"'
    narc[5] = '"At about that time I wasprocessing the outgoing shipments when I heard a loud noise. I went over to investigate and I stumbled upon', victimName+'’s body. It scared me half to death!"'
    narc[6] = '"At about that time I was making my rounds throughout the building when I stumbled upon', victimName,'lying on the ground. It scared me half to death!"'
    narc[7] = '"At about that time I was checking out my reflection in the window-I mean overviewing the gear shift functions on the forklift when I heard a loud noise. I walked over to investigate and discovered', victimName,'lying on the ground. It scared me half to death!"'
    narc[8] = '"At about that time I was checking twitter, just about to start on', victimName+'’s room, when I noticed', victimName,'lying on the ground!"'
    narc[9] = '"At about that time I was just walking through the hallway when I noticed', victimName+'’s door wide open. Being the kind and caring room-neighbor I am, I decided to have a looksie. When I found', victimName,'lying on the ground, I was scared half to death!"'
    narc[10] = '"At about that time I was checking the room after cleaning staff alerted me of the situation and I saw', victimName,'lying on the ground! Simply horrifying!"'
    #below is the sacred parrot, what say you?
    narc[11] = "parrot"
    narc[12] = '"At about that time I was putting the baby down for a nap when I heard this absolutely horrendous screech. I walked downstairs to investigate and saw', victimName,'on the ground! It was horrifying, dastardly! How dare they, with me- I mean the baby!"'
    narc[13] = '"At about that time I was  just relaxing on my front porch when I heard a noise from ', victimName+'’s house. I walked over to investigate like the good neighbor I am and found that the front door was unlocked. When I walked in, I saw', victimName,'on the ground. I was horrifying!"'
    narc[14] = '"At about that time I was in town for the week and staying with', victimName+'. I heard a loud noise and courageously walked downstairs to investigate when I saw', victimName,'on the ground- simply horrendous!”'
    narc[15] = '"At about that time I was I was relaxing in the living room when I heard a loud scream. I bravely walked towards the sound to investigate and I saw', victimName,'on the ground. It was horrifying!”'

    dimwitA = [0 for x in range(amt)]
    dimwitA[0] = "looked really hot"
    dimwitA[1] = "were real nervous-like"
    dimwitA[2] = "seemed kinda slow"
    dimwitA[3] = "DIMWIT AAAA"
    dimwitA[4] = "were checking their phone all the time"
    dimwitA[5] = "didn't really show any feelings"
    
    #leave this at the bottom, please!
    counter = -1
    for i in mapJobs:
        counter += 1
        
        s = name + ' walks into your office slowly, stopping to stretch and yawn. They blink around, dazed, until they eventually make their way to your desk. "Good evening/morning/afternoon... Why am I here again? Oh, right... the murder...Let’s see...It was around', timeFound + '..."'
        mapJobs[counter][2] = s + lethargic[counter]
        
        s = "A " + random.choice(("rather lanky", "stout", "twitching")) + " man/woman shuffles into your office, finding a seat quickly. “Heyyy,” says name, “howz’it goin?” You tell them about your investigation and ask them about what they saw the night of the murder. They look at you without blinking for a few seconds, and just as you’re about to repeat yourself, they snap back into it. "
        mapJobs[counter][3] = s + dimwit[counter]
        
        s = name + ' walks into your office with a confident stride, taking a moment to glance in a window and flip his/her bangs to the side. They take a seat on a nearby couch, engrossed with their phone until one of your assistants directs them to your desk. “Good evening/morning/afternoon. My name is', name, 'and it’s your pleasure to meet me!” As he/she chuckles at his/her joke, you stare, unamused. “Anyways, let’s talk about the murder. It was around', timeFound +'."'
        mapJobs[counter][4] = s + lethargic[counter]
        
    counter = -1
    for i in mapQ1:
        counter += 1
        s = "‘Round the body, I saw weapon.XXX And wouldn’t cha know it, I also found item."
        mapQ1[counter][3] = s
        
    counter = -1
    for i in mapQ2:
        counter += 1
        s = "There wasn’t noone else with me, just me and the body.XXX There was someone else there with me… they archetype. I’m purdy sure they were a gender."
        mapQ2[counter][3] = s
    
    counter = -1
    for i in mapArchetype:
        counter += 1
        mapArchetype[counter][3] = dimwitA[counter]
