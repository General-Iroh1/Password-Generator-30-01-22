from __future__ import print_function
import atexit
from os import path
from json import dumps, loads


def read_counter():
    return loads(open("counter.json", "r").read()) + 1 if path.exists("counter.json") else 1


def write_counter():
    with open("counter.json", "w") as f:
        f.write(dumps(counter))


counter = read_counter()
atexit.register(write_counter)
import sys
from colorama import Fore, Back, Style
#while loop
UserWordInput = []
i = 0
n = 0
while True:
    print(Fore.WHITE,"")
    word = input("Enter A Word you want your password te be a mixture of(The maximum is 3)\n")
    UserWordInput.append(word); n += 1
    if n == 3:
        break

    choice = input("Would you like to enter another word? Type 'yes' if you do, and 'no' if you dont\n")

    if choice.casefold() == 'no':
        break
    if choice.casefold() == 'yes':
        continue
    else:
        print (Fore.GREEN, "Sorry, you have typed a wrong input, which would you like? No or Yes?")
        wronginput = input("Input either 'yes' or 'no'\n")
        if wronginput == "yes":
            continue
        if wronginput == "no":
            break
        else:
            print(Fore.YELLOW,"You have misspelled either 'yes' or 'no', please try again")
            wronginput2 = input("yes or no?\n")
            if wronginput2.casefold == "no":
                break
            if wronginput2.casefold == "yes":
                continue
            else:
                print(Fore.RED,"You have one more try until you have to restart the program, please enter either yes or no very carefully.⚠️ IF YOU MISSPELL AGAIN, YOU WILL NOT GET ANOTHER TRY!\n")
                wronginput3 = input("last try, yes or no?\n")
                if wronginput3.casefold == "yes":
                    continue
                if wronginput3.casefold == "no":
                    break
                else:
                    print(Fore.LIGHTBLACK_EX,"You have misspelled 3 times, please restart the program to input more words.")
                    break
    

#Removes all commas/brackets/apostraphes
WordConnector = ""
VariableForList=(WordConnector.join(UserWordInput))
#Replacing words with symbols/numbers
VariableForList = VariableForList.replace('i', "!")
VariableForList = VariableForList.replace('I', "!")
VariableForList = VariableForList.replace('a', "@")
VariableForList = VariableForList.replace('A', "@")
VariableForList = VariableForList.replace('o', "0")
VariableForList = VariableForList.replace('O', "0")
VariableForList = VariableForList.replace('Q', "9")
VariableForList = VariableForList.replace('q', "9")
VariableForList = VariableForList.replace('e', "E")
VariableForList = VariableForList.replace('u', "U")
VariableForList = VariableForList.replace('s', "$")
VariableForList = VariableForList.replace('S', "$")
#joining numbers to end and start of password
print (Fore.LIGHTBLUE_EX,"The password you have created is:", VariableForList, "*Saved*\n")

print (Fore.WHITE)
reason = input("Why are you using this password?\n")
sys.stdout = open("Password Saver.rtf", "a")
sys.stdout.write ("\\rtf1 ")
sys.stdout.write (" password is: ")
sys.stdout.write (VariableForList)
sys.stdout.write ("\n\tYou have ran the code {} times/time\n".format(counter))

count = len(VariableForList)
if count == 1 or count == 2 or count == 3 or count == 4 or count == 0:
    print("\tThis password is - Weak")
    print("\tThe length of this password is: ", count, "characters long\n")
if count == 5 or count == 6 or count == 7 or count == 8 or count == 9:
    print("\tThis password is - Average")
    print("\tThe length of this password is: ", count, "characters long\n")
if count == 10 or count == 11 or count == 12 or count == 13 or count == 15 or count == 16 or count == 17 or count == 18 or count == 19 or count == 20:
    print("\tThis password is - Strong")
    print("\tThe length of this password is: ", count, "characters long\n")