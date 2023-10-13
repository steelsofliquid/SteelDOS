from time import*
from random import*

# SteelDOS 0.03a - 2023 Oct. 3rd
# Can't really recreate Linux from scratch, so why not my own DOS?
# DOS means "disk operating system", sooooooo...

sleep (1)
print ("SteelDOS Version 0.03a -- PREVIEW RELEASE --")
print ("Memory can't be tested in this version.")

sleep (1.22)

print ("Starting SteelDOS...")
sleep (1.77)

for i in range (0, 5):
    print ("Module", i, "Loaded!")
    sleep (0.01)

dosline = 1
command = 0
programinpu = 0

def helpcom():
    print ("\n-- SteelDOS Help Viewer --")
    print ("Knowledge Base not yet created.")

    sleep (0.42)

    print ("Command List:")

    sleep (0.07)
    
    print ("help: Program that displays help")
    print ("ver: Displays version")
    print ("shutdown: Shuts down SteelDOS")
    print ("speak: Program that says what you input")

    sleep (3.92)




def speakcom():
    programinpu = input("\n-- Speak.Com 0.03a SteelDOS --\n\nTell me what to say: ")
    print (programinpu)

    

while dosline == 1:
    command = input("\nSteelDOS 0.03a by STEELSOFLIQUID (2023 October 3rd)\nRun command or program: ")
    # command handler

    
    if command == "help" or command == "help.com":
        helpcom()
        
    elif command == "ver":
        print ("\nSteelDOS version 0.03a")

    elif command == "speak" or command == "speak.com":
        speakcom()
        
    elif command == "shutdown":
        print ("\nSteelDOS has shut down.")
        dosline = 0
        sleep (5)
        
    else:
        print ("\nError 1 - not a valid command or program")
        sleep (1)
