import os, sys, time
from importlib import import_module as require

name = "main"
load = False
sysd = {"lib" : None , "dat" : None}
sysi = {"ver" : "1.4", "cpr" : "\ncopyright (c) BOSS (Bucket Operational\nSystem Simulator) 05/2019 - 11/2019 by\nMateus Morais D. de Souza."}

def match(wrd, sub, msg): #

    Bin = input("<<< ")
    while Bin.replace(sub, "") != wrd : #
        
        print(msg)
        Bin = input("<<< ")

        if Bin == "ext" : #
            
            print(">>> bye")
            time.sleep(0.3)
            sys.exit()
        #
    #

    print(">>> did")
    return True
#

def main() : #

    ## Read user info ##
    file = open("conf.txt")
    data = file.readlines()
    data = [l.replace("\n", "") for l in data]
    file.close()

    log = match(data[0], "log ", ">>> wrg log")
    key = match(data[1], "key ", ">>> wrg key")
    
    ## Enabled ##
    while log and key : #

        ## Hello ##
        global load
        if not load : #

            print("")
            print(">>> wll come back")
            load = True
        #

        ## ode line ##
        code = input("<<< ")

        ## Who am i ##
        if code == "who am i" : #
            
            print("")
            os.system("echo %USERNAME%")
            print("")
        #

        ## sys ##
        elif code.startswith("sys ") : #
            
            #Version
            if code.endswith("ver") : print(">>> sys " + sysi["ver"])

            #Copy right
            elif code.endswith("cpr") : print("" + sysi["cpr"] +"\n")

            #Change color
            elif code.startswith("sys colr") : #
                
                color = code.replace("sys colr ", "")
                os.system('color ' + color)

                print(">>> did")
            #
            
            #Show time
            elif code.endswith("time") : print(">>> ", time.time)

            #Sys path
            elif code.startswith("sys set path ") : #

                os.system("cd " + code[13:])
                print(">>> did")
            #

            elif code.startswith("sys see path") : os.system("cd")

            #Run a new terminal
            elif code.endswith("rrun") : #

                print(">>> bye")
                time.sleep(0.3)
                os.system("cd " + os.path.dirname(os.path.abspath(__file__)))

                global name
                os.system("start "+name+".py")
                sys.exit()
            #

            #This is not a function
            else : print(">>> it's not sys cod")
        #

        ## Open file ##
        elif code.startswith("opn ") : #
            
            #Open a text
            if code.endswith("txt") : #

                name = input("... ")

                try : #
                    
                    sysd["dat"] = open(name + ".txt", "r")
                    print(">>> did")
                #

                except FileNotFoundError :
                    print(">>> can not find this")
            #

            #Generic File
            elif code.endswith("file") : #
                
                name = input("... ")

                try : #
                    
                    sysd["dat"] = open(name, "r")
                    print(">>> did")
                #

                except FileNotFoundError :
                    print(">>> can not find this")
            #

            else : print(">>> can not load this")
        #

        ##New file #
        elif code.startswith("new ") : #
            
            #New text file
            if code.endswith("txt") : #

                name = input("... ")

                #Check if exists a file with this name
                try : #

                    dat = open(name + ".txt")
                    dat.close()

                    print("<<< this file already exists. try othr name")
                #

                #Create file
                except FileNotFoundError : #
                    
                    dat = open(name + ".txt", "w+")
                    dat.close()

                    print(">>> did")
                #
            #
            
            #Generic File
            elif code.endswith("file") : #
                
                name = input("... ")

                #Check if exists a file with this name
                try : #

                    dat = open(name)
                    dat.close()

                    print("<<< this file already exists. try othr name")
                #

                #Create file
                except FileNotFoundError : #
                    
                    dat = open(name, "w+")
                    dat.close()

                    print(">>> did")
                #
            #

            else : print(">>> try othr type") 
        #

        ## File mananger ##
        elif code.startswith("dat ") : #
            
            #If no file
            if sysd["dat"] == None : print(">>> no txt loadd")
            
            #Current name
            elif code == "dat" : print(sysd["dat"].name) 

            #Read lines
            elif code.endswith("read") : #

                print("")

                #Get every line
                lines = sysd["dat"].readlines()
                lines = [l.replace("\n", "") for l in lines]

                #Print every line
                for l in lines : print(l)
                print("")
            #

            #Write in
            elif code.endswith("edit") : #
                
                #Close fine in read mode
                name = sysd["dat"].name
                sysd["dat"].close()
                
                #Open in whrite mode
                sysd["dat"] = open(name, "w")

                #Write on
                sysd["dat"].write(newText())
                sysd["dat"].close()

                #Open in read mode again
                sysd["dat"] = open(name, "r")
            #

            #Rename
            elif code.endswith("name") : #

                #Get the new name
                name = input("... ")

                #Get old name and close
                oldN = sysd["dat"].name
                sysd["dat"].close()

                #Rename and open again
                os.rename(oldN, name + ".txt")
                sysd["dat"] = open(name + ".txt")
                
                print(">>> did")
            #

            #Close file
            elif code.endswith("cls") : #
                
                sysd["dat"].close()
                print(">>> did")
            #

            else : print(">>> can not load this")
        #

        ## Delete an file ##
        elif code.startswith("del ") : #
            
            #Delete an text file
            if code.endswith("txt") : #
                
                name = input("... ")

                try : #
                    
                    os.remove(name + ".txt")
                    print(">>> did")
                #

                except FileNotFoundError :
                    print(">>> can not dell this")
            #

            #Generic File
            elif code.endswith("file") : #

                name = input("... ")

                try : #
                    
                    os.remove(name)
                    print(">>> did")
                #

                except FileNotFoundError :
                    print(">>> can not dell this")
            #

            else : print(">>> can not dell this")
        #

        ## Run a python module ##
        elif code.startswith("run ") : #
            
            sub = code.replace("run ", "")

            print(">>> running program", end="")
            print("...", end="")
            
            try : #

                exe = require(sub)

                time.sleep(0.4)
                exe.init()
                
                print("")
            #

            except : #

                time.sleep(0.4)
                print(" error!")
            #
        #

        ## Windows CMD ##
        elif code.startswith("cmd ") : #
            
            print("")
            os.system(code[3:])
            print("")
        #

        ## Clear terminal ##
        elif code == "clr" : os.system('cls')

        ## Help ##
        elif code.startswith("help") : #
            
            print("")
            Help(code)
        #

        ## Exit ##
        elif code == "ext" : #
            
            print(">>> bye")
            time.sleep(0.3)
            sys.exit()
        #

        ## Strange comand ##
        else : print(">>> unknow prompt comand.")
    #
#

## Read all typed lines ##
def newText() : #

    data = ["",]

    print("... type #cls to ext\n")
    
    #Get first line
    line = input("<<< ")

    #Add to lines
    while line != "#cls" : #

        data.append(line)
        line = input("<<< ")
    #

    print("")
    print(">>> did")
    
    #Remove the temporary item
    del data[0]
    data = "\n".join(data)

    return data
#

## Help ##
def Help(arg) : #

    print("")

    sysH = ("""
    sys cmd can do:\n
    <<< log : set your login        \n
    <<< key : set your password     \n
    ...                             \n
    <<< who am i : show user name   \n
    ...                             \n
    <<< sys ver  : show sys version \n
    <<< sys cpr  : show copyright   \n
    ...                             \n
    <<< sys colr : set line color   \n
    <<< sys time : show crnt time   \n
    ...                             \n
    <<< sys set path : set crnt path\n
    <<< sys see path : show sys path\n
    ...                             \n
    <<< sys rrun : re launch :MCP   \n
    ...                             \n
    <<< cmd : run windows comands   \n
    <<< clr : clear all the lines   \n
    <<< ext : exit from BucketMCP   \n
    """)

    opnH = ("""
    opn cmd can do:\n
    <<< opn txt : open a txt file   \n
    ... by name                     \n
    <<< opn file: open a ... file   \n
    ... by name and extention (.)   \n
    """)

    newH = ("""
    new cmd can do:\n
    <<< new txt : make a new text   \n
    ... by name                     \n
    <<< opn file: make a new file   \n
    ... by name and extention (.)   \n
    """)

    datH = ("""
    dat cmd can do:\n
    <<< dat : show data name        \n
    <<< dat read : show cont        \n
    <<< dat edit : edit cont        \n
    <<< dat name : rename           \n
    ...                             \n
    <<< dat cls : close data        \n
    """)

    delH = ("""
    del cmd can do:\n
    <<< del txt : dell a txt file   \n
    ... by name                     \n
    <<< opn file: dell a ... file   \n
    ... by name and extention (.)   \n
    """)

    runH = ("""
    run cmd can do:
    ... run *name* : run a game in  \n
    ... the memory                  \n
    >>> run rps : run Rock Paper &  \n
    ... Scisor
    """)

    cmdH = ("""
    cmd cmd can do:\n
    ... use a windows comand with   \n
    ... "cmd" as prefix             \n
    """)

    #help sys
    if arg.endswith("sys") : print(sysH)

    #help opn
    elif arg.endswith("opn") : print(opnH)

    #help new
    elif arg.endswith("new") : print(newH)
	
    #help dat
    elif arg.endswith("dat") : print(datH)
    
    #help del
    elif arg.endswith("del") : print(delH)
    
    #help run
    elif arg.endswith("run") : print(runH)

    #help cmd
    elif arg.endswith("cmd") : print(cmdH)

    #all
    elif arg == "help" : print(sysH, opnH, newH, datH, sep = "", end = "")
    
    #no help
    else : print(">>> can not help with this")
#

#Check if has a loggin
try : #

    file = open("conf.txt")
    data = file.readlines()
    data = [l.replace("\n", "") for l in data]
    file.close()
#

except FileNotFoundError : #

    print(">>> You dont have log")
    print(">>> We will create to you")

    #open a new file and edit
    file = open("conf.txt", "w+")
    file.write("user\npass")
    file.close()

    print("... type:\n")
    print("<<< log user")
    print("<<< key pass\n")
    print(">>> try help\n")
#

#Start
main()