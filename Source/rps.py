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

        opt = ["r", "p", "s"]

        print("")
        print(">>> type your option")
        print("... rock : r | paper : p | scsor : s")

        BIn = choice("<<< ", opt)

        #Game

        #System option
        sys = rand.choice(opt)

        #Pick rock
        if BIn == "r" : #

            #Sys pick paper
            if sys == "r" : #

                print(">>> sys pick rock")
                print("... draw!")
            #

            #Sys pick 
            if sys == "p" : #

                print(">>> sys pick paper")
                print("... sys win!")
            #

            #Sys pick 
            if sys == "s" : #

                print(">>> sys pick scsor")
                print("... you win!")
            #

        #Pick paper
        if BIn == "p" : #

            #Sys pick paper
            if sys == "r" :

                print(">>> sys pick rock")
                print("... you win!")
            #

            #Sys pick 
            if sys == "p" : #

                print(">>> sys pick paper")
                print("... draw!")
            #

            #Sys pick 
            if sys == "s" : #

                print(">>> sys pick scsor")
                print("... sys win!")
            #

        #Pick rock
        if BIn == "s" : #

            #Sys pick paper
            if sys == "r" : #

                print(">>> sys pick rock")
                print("... sys win!")
            #

            #Sys pick 
            if sys == "p" : #

                print(">>> sys pick paper")
                print("... you win!")
            #

            #Sys pick 
            if sys == "s" : #

                print(">>> sys pick scsor")
                print("... draw!")
            #
        #


        print("\n>>> resset game?")
        end = choice("... (S/n): ", ["s", "n"])

        if end == "s" : continue
        if end == "n" : break
    #
#