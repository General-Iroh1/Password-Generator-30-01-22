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
from colorama import Fore
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
        if wronginput == "yes".casefold():
            continue
        if wronginput == "no".casefold():
            break
        else:
            print(Fore.YELLOW,"You have misspelled either 'yes' or 'no', please try again")
            wronginput2 = input("yes or no?\n")
            if wronginput2 == "no".casefold():
                break
            if wronginput2 == "yes".casefold():
                continue
            else:
                print(Fore.RED,"You have one more try until you have to restart the program, please enter either yes or no very carefully.⚠️ IF YOU MISSPELL AGAIN, YOU WILL NOT GET ANOTHER TRY!\n")
                wronginput3 = input("last try, yes or no?\n")
                if wronginput3 == "yes".casefold():
                    continue
                if wronginput3== "no".casefold():
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
sys.stdout = open("Password Saver.rtf", "a+")
sys.stdout.write (reason)
sys.stdout.write (" password is: ")
sys.stdout.write (VariableForList)
sys.stdout.write ("\n\tYou have ran the code {} times/time\n".format(counter))

Count = len(VariableForList)

SpecialCharacters = (0)
countcomparison1  =(0 or 1 or 2 or 3 or 4)
countcomparison2  =(5 or 6 or 7 or 8 or 9)
countcomparison3  =(10 or 11 or 12 or 13 or 15 or 16 or 17 or 18 or 19 or 20)
countcomparison4  =(999)
SymbolCountComparison1 =0
SymbolCountComparison2 =(1 or 2)
SymbolCountComparison3 =(3 or 4 or 5 or 6 or 7 or 9 or 8 or 9 or 10 or 11 or 12 or 13 or 15 or 16 or 17 or 18 or 19 or 20)
SymbolCountComparison4 =(999)
SpecialCharacters += sum(c.isspace() for c in VariableForList)
for letter in range(len(VariableForList)):
    if(VariableForList[letter].isalpha()):
        SpecialCharacters = SpecialCharacters + 0
    elif(VariableForList[letter].isdigit()):
        SpecialCharacters = SpecialCharacters + 1
    else:
        SpecialCharacters = SpecialCharacters + 1
if countcomparison1 < Count < countcomparison2:
    print("\tThis password is - Weak")
    print("\tThe length of this password is: ", Count, "characters long\n")
    print("\tThe amount of special characters in your password is:", SpecialCharacters)
if countcomparison2 < Count < countcomparison3:
    print("\tThis password is - Average")
    print("\tThe length of this password is: ", Count, "characters long\n")
    print("\tThe amount of special characters in your password is:", SpecialCharacters)
if Count > countcomparison3:
    print("\tThis password is - Strong")
    print("\tThe length of this password is: ", Count, "characters long")
    print("\tThe amount of special characters in your password is:", SpecialCharacters, "\n")