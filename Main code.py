reason = input("Why would you like to use this password?\n")
f = open("Password Saver.rtf", "a+")
file = open("Password Saver.rtf", "r+")
file.close()
occ = 0
ques = input("Which part of the storage would you like to remove (Just enter the reason, ItS cAsE sEnSiTiVe!)?\n")
for line in f:
        words = line.split()
        for i in words:
            if i == ques:
                i.replace(reason, "\n")
from os import path
from json import dumps, loads
def read_counter():
    return loads(open("counter.json", "r").read()) + 1 if path.exists("counter.json") else 1

def write_counter():
    with open("counter.json", "w") as f:
        f.write(dumps(counter))

counter = read_counter()
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
Count = len(VariableForList)

SpecialCharacters = (0)
countcomparison1  =(0)
countcomparison2  =(5)
countcomparison3  =(10)
countcomparison4  =(999)
SymbolCountComparison1 =0
SymbolCountComparison2 =(2)
SymbolCountComparison3 =(3)
text = open("Password Saver.rtf", "a+")
l = text.readlines()
for i in l:
    if i == VariableForList:
        Replacement = i.replace(VariableForList)
SymbolCountComparison4 =(999)
SpecialCharacters += sum(c.isspace() for c in VariableForList)
for letter in range(len(VariableForList)):
    if(VariableForList[letter].isalpha()):
        SpecialCharacters = SpecialCharacters + 0
    elif(VariableForList[letter].isdigit()):
        SpecialCharacters = SpecialCharacters + 1
    else:
        SpecialCharacters = SpecialCharacters + 1

file = open("Password Saver.rtf", "a+")
file.write (reason)
file.write (" password is: ")
file.write (VariableForList)
file.write ("\n\tYou have ran the code {} times/time\n".format(counter))
if countcomparison1 < Count < countcomparison2 or Count == countcomparison2 and SpecialCharacters > SymbolCountComparison1:
    file.write("\tThis password is - Weak\n")
    file.write("\tThe length of this password is: "+ str(Count)+ "characters long\n")
    file.write("\tThe amount of special characters in your password is:"+ str(SpecialCharacters) + "\n")
if countcomparison2 < Count < countcomparison3  or Count == countcomparison2 and SpecialCharacters > SymbolCountComparison2:
    file.write("\tThis password is - Average\n")
    file.write("\tThe length of this password is: "+ str(Count)+ "characters long\n")
    file.write("\tThe amount of special characters in your password is:"+ str(SpecialCharacters) + "\n")
if Count > countcomparison3 or Count == countcomparison3 and SpecialCharacters > SymbolCountComparison3 or SpecialCharacters == SymbolCountComparison3:
    file.write("\tThis password is - Strong\n")
    file.write("\tThe length of this password is: "+str(Count) +"characters long\n")
    file.write("\tThe amount of special characters in your password is:"+ str(SpecialCharacters)+ "\n")
