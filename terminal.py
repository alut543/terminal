import time
import random

print("THEANNOYINGTERMINAL 🤠")
print(" ")
login = input("Would you like to install the annoying terminal? (y/n)")
time.sleep(5)
if login == "y":
    login1 = input("Type in your username > ")
    time.sleep(2)
    while True:
        stringname = input("root@" + login1 + "> ")
        if stringname == "help":
            print("Certinaly! Here are all the commands shown in this field.")
            time.sleep(2)
            print(" ")
            print("help - shows this are you stupid?")
            print("echo - says what you want")
            print("calculator - opens a calculator app.")
            print("Thats all! Thank you!")
        elif stringname == "echo":
            print("Why you want me to say something? Have a go!")
            echo = input("> ")
            print(echo)
        elif stringname == "calculator":
            print("Calculator:")
        cmdline = input("> ")
        if cmdline == "addition":
            setnumaddfirst = int(input("Enter your first number. > "))
            setnumaddsecond = int(input("Enter your second number. > "))
            time.sleep(2)
            print(setnumaddfirst + setnumaddsecond)
        elif cmdline == "subtraction":
            setnumsubfirst = int(input("Enter your first number. > "))
            setnumsubsecond = int(input("Enter your second number. > "))
            time.sleep(2) 
            print(setnumsubfirst - setnumaddsecond)
        elif cmdline == "multiplication":
            setnummultfirst = int(input("Enter your first number. > "))
            setnummultsecond = int(input("Enter your second number. > "))
            time.sleep(2)
            print(setnummultfirst * setnummultsecond)
        elif cmdline == "division":
           setnumdivfirst = int(input("Enter your first number. > "))
           setnumdivsecond = int(input("Enter your second number. > "))
           time.sleep(2)
           print(setnumdivfirst + setnumdivsecond)
        else:
            print("Sorry such command does not exist, try typing help for help stupid.")
