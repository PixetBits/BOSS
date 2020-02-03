## Rock, Paper and Scissor ##
## sub program for BB-BOSS ##

import random as rand

def choice(msg, option): #

    rtrn = input(msg)
    while not rtrn in option: #
        
        rtrn = input(msg)
    #

    return rtrn
#

def init() : #

    print("")

    while True: #

        opt = ["q", "p", "s"]
        key = {"q" : "quartz", "p" : "parchment", "s" : "shears"}

        print("")
        print(">>> type your option")
        print("... quartz : q | parchment : p | shears : s")

        BIn = choice("<<< ", opt)

        #Game

        #System option
        sys = rand.choice(opt)
        print(">>> sys pick " + key[sys])

        #Pick rock
        if BIn == "q" : #

            #Sys pick paper
            if sys == "q" : print("... draw!")

            #Sys pick 
            if sys == "p" : print("... sys win!")

            #Sys pick 
            if sys == "s" : print("... you win!")
		#
		
        #Pick paper
        if BIn == "p" : #

            #Sys pick paper
            if sys == "q" : print("... you win!")


            #Sys pick 
            if sys == "p" : print("... draw!")


            #Sys pick 
            if sys == "s" : print("... sys win!")

        #Pick rock
        if BIn == "s" : #

            #Sys pick paper
            if sys == "q" : print("... sys win!")

            #Sys pick 
            if sys == "p" : print("... you win!")

            #Sys pick 
            if sys == "s" : print("... draw!")
        #


        print("\n>>> resset game?")
        end = choice("... (Y/n): ", ["y", "n"])

        if end == "y" : continue
        if end == "n" : break
    #
#