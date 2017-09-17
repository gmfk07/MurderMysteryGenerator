# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:51:28 2017

@author: gmfk07
"""
import random

def archetypeInit(mapJobs, mapQ1, mapQ2, mapArchetype):
    amt = 16
    
    promiscuous = [0 for x in range(amt)]
    promiscuous[0] = "walking home from the salon, when I found a body"
    promiscuous[1] = "taking out the disgusting trash from my apartment when I smelt this rotting smell. When I went to investigate, I saw a body."
    promiscuous[2] = "going for my nightly jog when I saw a body."
    promiscuous[3] = "after a day of cleaning some clothes I saw a body."
    promiscuous[4] = "getting ready to go home after a long day at the warehouse when I saw a body."
    promiscuous[5] = "polishing my nails late at work when I saw a body."
    promiscuous[6] = "doing my late night shift when I saw a faint figure in the distance and upon investigation stumbled across a body."
    promiscuous[7] = "messing around with the forklift late at night when I saw a body."
    promiscuous[8] = "cleaning my body because I thought I smelt bad when I realized there was a rotting corpse next door!"
    promiscuous[9] = "knocking on the door of my neighbor to give him my daily… gift… when I found out [he/she] was dead. Shame."
    promiscuous[10] = "pleasuring this handsome fellow by the front door, when I got a call reporting a terrible smell upstairs. I went up there and found victimName, and let me tell you hun, that corpse was not a pleasant sight."
    promiscuous[11] = "*squack*...*squack*...*squACK**SQUACK**man/woman**SQUACK**SQuack**squack*...*squack*..."
    promiscuous[12] = "cleaning victimName’s clothes when I saw him/her lying like a hot pancake on the floor."
    promiscuous[13] = "doing my daily jiggle in front of the TV when I smelt that horrific smell. I broke into my neighbor’s house and found his/her cute body lying dead in front of his/her computer screen."
    promiscuous[14] = "heading over to victimName’s house for the weekly bang and clang but turns out he/she died."
    promiscuous[15] = "on my way back from the groceries and started preparing some asparagus for my love. Eventually, I… *sobs*... I found victimName lying on my bed naked… dead."

    
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
    lethargic[1] = '"At about that time I was walking back to my apartment when I saw victimName on the ground… It was almost surreal… Did you need me to be more specific? Sorry, I’m not much for conversations…”'
    lethargic[2] = '"At about that time I was walking through the alley when I witnessed the crime. I’m not from around there, so it was my first time taking that route… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[3] = '"At about that time I was walking back from the laundromat when I saw victimName on the ground… It was almost surreal… Did you need me to be more specific? Sorry, I’m not much for conversations…”'
    lethargic[4] = '"At about that time I was just checking on things in the warehouse when I noticed victimName on the ground…  It was almost surreal… Did you need me to be more specific? Sorry, I’m not much for conversations…”' 
    lethargic[5] = '"At about that time I was just checking on things in the warehouse when I noticed victimName on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[6] = '"At about that time I was just making sure nothing suspicious was going on in the warehouse when I noticed victimName on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[7] = '"At about that time I was just shutting down the lift when I noticed victimName on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[8] = '"At about that time I was cleaning the room when I noticed victimName on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[9] = '"At about that time I was trying to pay victimName a visit, and when I got to the door, I realized it was unlocked. I walked in, and saw victimName on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[10] = '"At about that time I was The cleaning staff alerted me of the situation, and when I went to investigate, I saw victim on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    #below is the sacred parrot, what say you?
    lethargic[11] = "parrot"
    lethargic[12] = '"At about that time I was putting the baby down for a nap when I heard this abhorrent screech. I walked downstairs to investigate and saw victimName on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[13] = '"At about that time I was just relaxing on my front porch when I heard a noise from victimName’s house. I walked over to investigate and found that the front door was unlocked. When I walked in, I saw victimName on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[14] = '"At about that time I was in town for the week and staying with victimName. I heard a loud noise and walked downstairs to investigate when I saw victimName on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    lethargic[15] = '"At about that time I was I was relaxing in the living room when I heard a loud scream. I walked towards the sound to investigate and I saw victimName on the ground…  It was almost surreal… Did you need more information? Sorry, I’m not much for conversations…”'
    
    #', murdervictim.getName() ,'
    #', victimName,'
    
    narc = [0 for x in range(amt)]
    narc[0] = '"At about that time I was walking towards my new condominium! It’s just around the corner, and you literally could not find a better place to live! It’s close to transportation, park areas, restaurants, bars, you name it, it’s got it! I’m so good at home-searching. Anyways, I saw victimName lying on the ground right after I updated my snapchat, and it scared me half to death."'
    narc[1] = '"At about that time I was walking towards my new apartment! You literally could not find a better place to live! It’s close to transportation, park areas, restaurants, bars, you name it, it’s got it! I’m so good at home-searching. Anyways, I saw victimName lying on the ground right after I updated my snapchat, and it scared me half to death."'
    narc[2] = '"At about that time I was Walking around in the neighborhood. I was considering living here a couple years ago, but after I saw victimName lying on the ground, it’s clear I made the right choice!  Good thing I’m so good at home-searching…"'
    narc[3] = '"At about that time I was walking towards the new laundromat because I love supporting my local businesses! I’m much more socially-conscious than other people, clearly. Anyways, I saw victimName lying on the ground, and I was scared nearly half to death!"'
    narc[4] = '"At about that time I was keeping tabs on my underlings, I mean employees. When I making my rounds, however, I stumbled upon victimName’s body. It scared me half to death!"'
    narc[5] = '"At about that time I wasprocessing the outgoing shipments when I heard a loud noise. I went over to investigate and I stumbled upon victimName’s body. It scared me half to death!"'
    narc[6] = '"At about that time I was making my rounds throughout the building when I stumbled upon victimName lying on the ground. It scared me half to death!"'
    narc[7] = '"At about that time I was checking out my reflection in the window-I mean overviewing the gear shift functions on the forklift when I heard a loud noise. I walked over to investigate and discovered victimName lying on the ground. It scared me half to death!"'
    narc[8] = '"At about that time I was checking twitter, just about to start on victimName’s room, when I noticed victimName lying on the ground!"'
    narc[9] = '"At about that time I was just walking through the hallway when I noticed victimName’s door wide open. Being the kind and caring room-neighbor I am, I decided to have a looksie. When I found victimName lying on the ground, I was scared half to death!"'
    narc[10] = '"At about that time I was checking the room after cleaning staff alerted me of the situation and I saw victimName lying on the ground! Simply horrifying!"'
    #below is the sacred parrot, what say you?
    narc[11] = "parrot"
    narc[12] = '"At about that time I was putting the baby down for a nap when I heard this absolutely horrendous screech. I walked downstairs to investigate and saw victimName on the ground! It was horrifying, dastardly! How dare they, with me- I mean the baby!"'
    narc[13] = '"At about that time I was  just relaxing on my front porch when I heard a noise from victimName’s house. I walked over to investigate like the good neighbor I am and found that the front door was unlocked. When I walked in, I saw victimName on the ground. I was horrifying!"'
    narc[14] = '"At about that time I was in town for the week and staying with victimName. I heard a loud noise and courageously walked downstairs to investigate when I saw victimName on the ground- simply horrendous!”'
    narc[15] = '"At about that time I was I was relaxing in the living room when I heard a loud scream. I bravely walked towards the sound to investigate and I saw victimName on the ground. It was horrifying!”'
    
    anxious = [0 for x in range(amt)]
    anxious[0] = '"I wish I could help, but...I just don’t know anything. I go through there on my way home. As soon as I saw the body, I got spooked and ran."'
    anxious[1] = '"Well, here’s all I know. I heard a noise outside my window, so I went to investigate. As soon as I saw the body, I got spooked and ran."'
    anxious[2] = '"At about that time I was Walking around in the neighborhood. I was considering living here a couple years ago, but after I saw victimName lying on the ground, it’s clear I made the right choice!  Good thing I’m so good at home-searching…"'
    anxious[3] = '"I wish I could help, but...look it’s got nothing to do with me. I keep my nose clean, alright? I can’t risk it. "'
    anxious[4] = '"At about that time I was keeping tabs on my underlings, I mean employees. When I making my rounds, however, I stumbled upon  victimName’s body. It scared me half to death!"'
    anxious[5] = '"Right, right. The factory is my responsibility, you know. Well, what I know is, um, I was doing my tour, and…and then I found the body. Oh god, why. I don’t want to lose my job."'
    anxious[6] = '" I wish I had something more to tell you, but I don’t know anything. I was just cleaning up around the factory when…I found the body. Oh god, why. I used to love working here."'
    anxious[7] = '"Things used to be so simple around here. These days…I never can tell. On my last facility tour, I ran across the victim. Who could do such a thing? And why here??"'
    anxious[8] = '"Well, here’s what happened. I had just parked the forklift and was going to clock out. Then, of course, I can’t go one day without something bad happening. I wish I had never found that body."'
    anxious[9] = '"Oh no, oh no. This is really bad. I was cleaning the rooms, and to my surprise, one of them was still occupied! But the person wasn’t responding. I took a look, and...well, you’ve seen the rest."'
    anxious[10] = '"Look, I was just visiting victimName at his/her room. I got there, and...it was horrible. I wish I had never seen that. Why did that have to happen. "'
    #below is the sacred parrot, what say you?
    anxious[11] = "parrot"
    anxious[12] = '"I had just put the baby down for a nap, and went to check on victimName. What a nightmare. I nearly fainted!!"'
    anxious[13] = '"I’ll tell you what I know, but it’s not much. I was relaxing on my porch when I heard a scuffle next door. They’re normally very quiet, so I was concerned. I went to ask if everything was okay, and I could see a body lying on the ground in the front room."'
    anxious[14] = '"I can’t believe this! I just got into town to visit my victimName. And now he/she is gone. How could this happen? ”'
    anxious[15] = '"That’s my husband/wife you’re talking about! And you think it’s MY fault? I know less than you do. What do you expect me to tell you?"'

    promiscuousA = [0 for x in range(amt)]
    promiscuousA[0] = "looked like a hunk of meat"
    promiscuousA[1] = "was a jittery mess"
    promiscuousA[2] = "was like some slow turtle"
    promiscuousA[3] = "didn't seem to be right in the head"
    promiscuousA[4] = "was checking himself in the mirror"
    promiscuousA[5] = "was hot but too serious for my tast"

    anxiousA = [0 for x in range(amt)]
    anxiousA[0] = "was se-sexy"
    anxiousA[1] = "was even more nervous than me"
    anxiousA[2] = "seemed to be quite slow"
    anxiousA[3] = "was stupid looking"
    anxiousA[4] = "looked like he had a huge ego"
    anxiousA[5] = "was cold like a robot"

    dimwitA = [0 for x in range(amt)]
    dimwitA[0] = "looked really hot"
    dimwitA[1] = "were real nervous-like"
    dimwitA[2] = "seemed kinda slow"
    dimwitA[3] = "DIMWIT AAAA"
    dimwitA[4] = "were checking their phone all the time"
    dimwitA[5] = "didn't really show any feelings"
    
    lethargicA = [0 for x in range(amt)]
    lethargicA[0] = "I think they had a hooded gaze..."
    lethargicA[1] = "They seemed a bit fidgety,"
    lethargicA[2] = "LETHARGIC AAAA"
    lethargicA[3] = "They looked as if were lost..."
    lethargicA[4] = "I think they took a moment to check their phone,"
    lethargicA[5] = "They seemed rather disinterested..."
    
    narcA = [0 for x in range(amt)]
    narcA[0] = "Their clothes seemed rather complementing, but my legs look better of course!"
    narcA[1] = "The poor thing looked like a deer caught in headlights! My eyes were still bigger and more defined though."
    narcA[2] = "he/she moved so slowly! It was pretty strange."
    narcA[3] = "With the way they stumbled, I almost felt bad for them!"
    narcA[4] = "NARC AAAA"
    narcA[5] = " I think they were awake? I don’t really know I was checking my phone."
    
    #leave this at the bottom, please!
    counter = -1
    for i in mapJobs:
        counter += 1
        
        # Promiscuous
        s = "name waltzes into your office showing much of his/her legs; making sure to discreetly reveal just a peek of his/her thick thigh.\n\n"
        s += '"Why hey there babe, what do you need from me?“ he/she says with a seductive grin.\n\n'
        s += '"Please stop,” you say.'
        s += '“Alright sugar. Well at timeFound, I was '
        mapJobs[counter][0] = s + promiscuous[counter]

        #Anxious
        
        #Lethargic
        s = 'name walks into your office slowly, stopping to stretch and yawn. They blink around, dazed, until they eventually make their way to your desk. "Good afternoon... Why am I here again? Oh, right... the murder...Let’s see...It was around timeFound ..."'
        mapJobs[counter][2] = s + lethargic[counter]
        
        #DimWit
        s = "A " + random.choice(("rather lanky", "stout", "twitching")) + " man/woman shuffles into your office, finding a seat quickly. “Heyyy,” says name, “howz’it goin?” You tell them about your investigation and ask them about what they saw the night of the murder. They look at you without blinking for a few seconds, and just as you’re about to repeat yourself, they snap back into it. "
        mapJobs[counter][3] = s + dimwit[counter]
        
        #Narc
        s = "name walks into your office with a confident stride, taking a moment to glance in a window and flip his/her bangs to the side. They take a seat on a nearby couch, engrossed with their phone until one of your assistants directs them to your desk. “Good afternoon. I'm name and it’s your pleasure to meet me!” As he/she chuckles at his/her joke, you stare, unamused. “Anyways, let’s talk about the murder. It was around timeFound.”"
        mapJobs[counter][4] = s + lethargic[counter]
        
    counter = -1
    for i in mapQ1:
        counter += 1
          
          # Promiscuous
        s = "Oh dear… I believe with all my heart that I saw a weapon!XXX I also found item."
        mapQ1[counter][0] = s
        
        #Lethargic
        s = "Let me see if I can remember what I saw… Maybe a weapon?XXX Maybe an item? I don’t know…"
        mapQ1[counter][2] = s
        
        #DimWit
        s = "‘Round the body, I saw weapon.XXX And wouldn’t cha know it, I also found item."
        mapQ1[counter][3] = s
        
        #Narc
        if counter == 5:
           s = "Well I was preoccupied with checking my phone for messages- I mean working, but I did see something that looked like weapon.XXX I also saw something that looks like item."  
        elif counter == 8:
           s = "Well I was preoccupied with my phone, but I did see something that looked like weapon.XXX I also saw something that looks like item."
        elif counter == 9:
           s = "Well I was preoccupied with my phone, but I did see something that looked like weapon.XXX I also saw something that looks like item."
        elif counter == 12:
           s = "Well I was swiping through my phone, but I did see something that looked like weapon.XXX I also saw something that looks like item."
        else:
            s = "Well I spent most of the time checking my phone for messages, it never stops ringing sometimes, but I did see something that looked like weapon.XXX I also saw something that looks like item."
        mapQ1[counter][4] = s
        
    counter = -1
    for i in mapQ2:
        counter += 1
        
        #Promiscuous
        s = "It was a mighty fine good looking man/woman that archetype"
        mapQ2[counter][0] = s
       
        #Lethargic
        if counter == 6:
            s = "Nobody else was there... XXXI think I saw a man/woman that was about age years old... archetype but they dashed off before I could get a good look..."
        if counter == 9:
            s = "Nobody else was there... XXXI think I saw a man/woman walking down the hallway... archetype but I didn’t really get a good look…"
        else:
            s = "Nobody else was there... XXXI think I saw a man/woman...archetype but I didn’t really get a good look"
        mapQ2[counter][2] = s

        #DimWit
        s = "There wasn’t noone else with me, just me and the body.XXX There was someone else there with me… they archetype. I’m purdy sure they were a gender."
        mapQ2[counter][3] = s
        
        #Narc
        if counter == 6:
            s = "Nobody else was there... XXXIt was hard to make out, but I think I saw a man/woman... archetype Anyways, I got distracted and they managed to sneak away."
        elif counter == 8:
            s = "Nobody else was there... XXXIt was hard to make out, but I think I saw a man/woman in the hallway...archetype" 
        elif counter == 9:
            s = "Nobody else was there... XXXIt was hard to make out, but I think I saw a man/woman in the hallway...archetype"
        else:
            s = "Nobody else was there... XXXIt was hard to make out, but I think I saw a man/woman... archetype"
        mapQ2[counter][4] = s
    
    counter = -1
    for i in mapArchetype:
        counter += 1
        
        mapArchetype[counter][0] = promiscuousA[counter]
        mapArchetype[counter][2] = lethargicA[counter]
        mapArchetype[counter][3] = dimwitA[counter]
        mapArchetype[counter][4] = narcA[counter]
        
