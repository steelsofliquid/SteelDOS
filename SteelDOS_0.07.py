from time import*
from random import*

# SteelDOS 0.07 - 2023 Oct. 3rd
# Can't really recreate Linux from scratch, so why not my own DOS?
# DOS means "disk operating system", sooooooo...

sleep (1)
print ("SteelDOS Version 0.07 -- PREVIEW RELEASE --")
print ("Memory can't be tested in this version.")

sleep (1.22)

print ("Starting SteelDOS...")
sleep (1.77)

for i in range (0, 9):
    print ("Module", i, "Loaded!")
    sleep (0.01)

sleep (0.92)
print ("Module", "comdline.sce", "Loaded!")
sleep (0.33)
print ("Module", "parmeter.scm", "Loaded!")
sleep (0.41)
print ("Controller \"dosline\" is currently inactive.")
sleep (0.01)

dosline = 1
command = 0
programinpu = 0
parameter = 0

knowledgebas = 2

operator = 0
calcvala = 0
calcvalb = 0
calcvalc = 0

timeropt = 0
timercustim = 0

print ("Controller \"dosline\" is now ", dosline)

sleep (0.33)

print ("Defining program codes...")

def helpcom():
    print ("\n-- SteelDOS Help Viewer --")
    print ("Knowledge Base: \nKB1: Command List\nKB2: What is SteelDOS?\nKB3: Current Limits\nKB4: Command Line\nKB5: Applications\nKB6: Errors\nKB7: Support Information")

    knowledgebas = int(input("Load Knowledge Base Article "))

    sleep (0.42)

    if knowledgebas == 1:
        print ("Command List")
        
        sleep (0.07)
        
        print ("\nhelp: Program that displays help")
        print ("ver: Displays version")
        print ("shutdown: Shuts down SteelDOS")
        print ("speak: Program that says what you input")
        print ("dir: Performs a directory listing")
        print ("calculat: Program that does math")
        print ("thread: Thread command")
        print ("softinfo: Displays program information")
        print ("timer: Program that counts down to zero from a selected value.")
        
    elif knowledgebas == 2:
        print ("What is SteelDOS?")

        sleep (0.07)

        print ("\n     SteelDOS is a modern, spiritual successor to MS-DOS, a primitive computer OS used alongside early Windows versions (as early Windows was an operating environment, meaning it needed DOS). DOS is an acronym for \"disk operating system\", but SteelDOS is moreso a reversed roles, needing Windows to run.")
        print ("\n     SteelDOS has been in development for not a long time, as it is purely an indie software project that, to an extent, is a sister project to Steel OS, though much more capable under-the-hood, being written in Python instead of Scratch/TurboWarp. I (SteelsOfLiquid) am the only person who is working on the project, meaning it may be a while before another update is released.")
        print ("\n     The first major release of SteelDOS, SteelDOS version 1.0, is in development as SteelDOS 0.xx.")

    elif knowledgebas == 3:
        print ("Current Limits")

        sleep (0.07)

        print ("\n     SteelDOS is still rather limited, as it is limited to a text-only environment. Apart from this setback, limits include: ")
        print ("- Currently, you need Windows in order to run SteelDOS.")
        print ("- You also need Python 3.9 or later in order to run SteelDOS.")
        print ("- SteelDOS can't get access to the network.")
        print ("- SteelDOS can't make changes to contents on the hard disk.")
        print ("- SteelDOS is limited to English.")
        print ("- SteelDOS can't check the time.")

        print ("\n* SteelDOS does give access to directory listings of the virtual filesystem.")
        print ("\nSo, currently, SteelDOS is rather limited. But API development is made easier, as you just need to insert code into the source file in order to install a program, plus, development of more complex programs is easier versus Steel OS.")

    elif knowledgebas == 4:
        print ("Command Line")

        sleep (0.07)

        print ("\n     The SteelDOS command line tells you to run a command or program. If the content you entered is invalid, it gives you an error.")
        print ("\n     Before executing a program, the command line will present to you the information of the program. This also applies to commands and files, but files cannot be opened directly from the line.")
        print ("\n     You can enter programs either with or without the extension. This also applies to commands, but files need their extension stated to be displayed.")

        print ("\nThe extensions of files goes:")
        print ("- *.COM: SteelDOS application (Note! MS-DOS programs use the same extension!)")
        print ("- *.CLC: SteelDOS command line command.")
        print ("- *.SCE: SteelDOS command extension")
        print ("- *.SCM: SteelDOS command module")

        print ("Note that these files appear exclusively in SteelDOS' virtual filesystem. Extensions may conflict with other programs.")

    elif knowledgebas == 5:
        print ("Applications")

        sleep (0.07)

        print ("\n  SteelDOS Help Viewer")
        print ("     SteelDOS Help Viewer is a program for viewing help articles. If you are confused on what something does in SteelDOS, run this program and look in the right knowledge base. You can execute the program by running \"help\" or \"help.com\" with the command line active.")
        print ("\n  SteelDOS SpeakCom")
        print ("     SteelDOS SpeakCom is a program for displaying a message. It is a fairly simple program.")
        print ("\n  SteelDOS Calculator")
        print ("     SteelDOS Calculator allows you to perform basic math operations, such as addition, subtraction, multiplication and division.")
        print ("\n  SteelDOS Timer")
        print ("     SteelDOS Timer is a timer program allowing you to count down to zero from a set value. Time is measured in seconds, and when time is done, a message will be displayed and the program will close.")

        print ("More programs will be added in future releases!")

    elif knowledgebas == 6:
        print ("Errors")

        sleep (0.07)

        print ("\n     Errors may be displayed when you enter code. This is a list of errors:")
        print ("- 01: This error indicates you tried to run a program, command, or file that does not exist in SteelDOS' file system.")
        print ("- 02: This error appears if you choose an option that is not shown.")
        print ("- 03: This error appears if a program experiences an issue in its runtime.")
        print ("\n     The system may also hang. In this case, there won't be a response.")
        print ("\n     Error codes may be added in later releases.")
        
    elif knowledgebas == 7:
        print ("Support Information")

        sleep (0.07)

        print ("\nIf you need \"customer support\", please contact me on Discord. You can do so by messaging steelsofliquid.")
        print ("\n     If you can't get ahold of me that way, please go to my YouTube channel and send an e-mail to my e-mail address.")
        print ("\n     If you can't get ahold of me on social media, or are under the age of 13, please ask an adult to get in touch with me.")

    else:
        print ("Error 02: Invalid Option")

    sleep (3.92)




def speakcom():
    programinpu = input("\n-- Speak.Com 0.03a SteelDOS --\n\nTell me what to say: ")
    print (programinpu)



def calcucom():
    print ("\n-- SteelDOS Calculator 0.07 --")
    operator = int(input("\n1 = Add numbers\n2 = Subtract numbers\n3 = Multiply numbers\n4 = Divide numbers\nSelect an operation to do: "))
    if operator == 1:
        calcvala = int(input("Enter the first number: "))
        calcvalb = int(input("Enter the second number: "))
        calcvalc = (calcvala + calcvalb)
        print (calcvala, "+", calcvalb, "=", calcvalc)
        
    elif operator == 2:
        calcvala = int(input("Enter the first number: "))
        calcvalb = int(input("Enter the second number: "))
        calcvalc = (calcvala - calcvalb)
        print (calcvala, "-", calcvalb, "=", calcvalc)
        
    elif operator == 3:
        calcvala = int(input("Enter the first number: "))
        calcvalb = int(input("Enter the second number: "))
        calcvalc = (calcvala * calcvalb)
        print (calcvala, "×", calcvalb, "=", calcvalc)
        
    elif operator == 4:
        calcvala = int(input("Enter the first number: "))
        calcvalb = int(input("Enter the second number: "))
        if calcvalb == 0:
            print ("Error 03 - This program has performed an illegal operation and will be terminated.\nIf the problem persists, contact the program developer/publisher.")

        else:
            calcvalc = (calcvala / calcvalb) # don't know if variables work inside functions (probably not >_<), but we'll see...
            print (calcvala, "÷", calcvalb, "=", calcvalc)

    else:
        print ("Error 02 - Invalid Option")

    sleep (3.92)
    

def timercom():
    print ("\n-- SteelDOS Timer 0.07 --")
    print ("\n-- OPTIONS --\n1: 10-Second Timer\n2: 30-Second Timer\n3: 1-Minute Timer\n4: 2-Minute Timer\n5: Custom Length")
    timeropt = int(input("Enter the timer option: ")) # oops, did a "==" here... >_< (my brain is going to go up in flames one of these days...)
    
    if timeropt == 1:
        for i in range (0, 11):
            print (10 - i)
            sleep (1)
        print ("TIMER DONE!!")

    elif timeropt == 2:
        for i in range (0, 31):
            print (30 - i)
            sleep (1)
        print ("TIMER DONE!!")

    elif timeropt == 3:
        for i in range (0, 61):
            print (60 - i)
            sleep (1)
        print ("TIMER DONE!!")

    elif timeropt == 4:
        for i in range (0, 121):
            print (120 - i)
            sleep (1)
        print ("TIMER DONE!!")

    elif timeropt == 5:
        timercustim = int(input("Select a custom value to use for the timer: "))
        if timercustim <= 0:
            print ("Error 03 - This program has performed an illegal operation and will be terminated.\nIf the problem persists, contact the program developer/publisher.")
        else:
            for i in range (0, (timercustim + 1)):
                print (timercustim - i)
                sleep (1)
            print ("TIMER DONE!!")

    else:
        print ("Error 02 - Invalid Option")

    sleep (3.92)


    

sleep (1.22)

print ("SteelDOS is now ready to use.")

while dosline == 1:
    command = input("\nRun command or program: ")
    # command handler

    
    if command == "help" or command == "help.com":
        print ("help.com // COM Executable\n\"SteelDOS Help Viewer\" - SteelsOfLiquid")

        # Scrapped a file options menu here. Thought it'd be too complex > ‿ |
        
        helpcom()
        
    elif command == "ver":
        print ("\nSteelDOS version 0.07 [Version 0.07.66 Codename \"Mystic\"]")

    elif command == "speak" or command == "speak.com":
        print ("speak.com // COM Executable\n\"SpeakCom\" - SteelsOfLiquid")
        speakcom()

    elif command == "dir":
        print ("root:")
        print (" - calculat.com")
        print (" - comdline.sce")
        print (" - dir.clc")
        print (" - dosline.sys")
        print (" - help.com")
        print (" - parameter.scm")
        print (" - softinfo.clc")
        print (" - speak.com")
        print (" - thread.clc")
        print (" - timer.com")
        print (" - ver.clc")
        print (" kb:")
        print ("  - kb1.kb")
        print ("  - kb2.kb")
        print ("  - kb3.kb")
        print ("  - kb4.kb")
        print ("  - kb5.kb")
        print ("  - kb6.kb")
        print ("  - kb7.kb")
        print (" records:")
        print ("  - osname.a")
        print ("  - osver.a")
        print (" modules:")
        print ("  - bomebis.scm")
        print ("  - filesyst.scm")
        print ("  - line.scm")
        print ("  - progdisp.scm")

    elif command == "thread":
        for i in range (0, 65):
            print ("::thread (", i, randint(1, 64), ")")
            sleep (0.01)

    elif command == "softinfo":
        print ("SteelDOS\nVersion: 0.07\nBuild: 66\nCodename: \"Mystic\"\nLanguage: EN-US (translations coming soon!)")

    elif command == "calculat" or command == "calculat.com":
        print ("calculat.com // COM Executable\n\"SteelDOS Calculator\" - SteelsOfLiquid")
        calcucom()

    elif command == "timer" or command == "timer.com":
        print ("timer.com // COM Executable\n\"SteelDOS Timer\" - SteelsOfLiquid")
        timercom()

    elif command == "shutdown":
        print ("\nSteelDOS has shut down.")
        dosline = 0
        sleep (5)
        
    else:
        print ("\nError 01 - Invalid command or program")
        sleep (1)
