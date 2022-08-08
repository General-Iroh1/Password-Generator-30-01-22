from __future__ import print_function
import shutil
from os.path import join
import os

reason = input("Why would you like to use this password?\n")
file= open(reason+".txt", "a+")
file = open(reason+".txt", "r+")
file.write("This is a placeholder.\n")
occ = 0

with open(reason+".txt", "r+") as file:
    for lines in file:
        for word in lines.split():
            if word == reason:
                occ += 1

if occ >= 1:
    rewrite = input("Would you like to rewrite the password for:"+ reason+ "?\n")
    if rewrite == "yes":
        file= open(reason+".txt", "a+")
        file.truncate(0)

from os import path
from json import dumps, loads
import atexit

def read_counter():
    return loads(open("counter.json", "r").read()) + 1 if path.exists("counter.json") else 1


def write_counter():
    with open("counter.json", "w") as f:
        f.write(dumps(counter))


counter = read_counter()
atexit.register(write_counter)

from colorama import Fore
#while loop
UserWordInput = []
n = 0
i = 0
while True:
    print(Fore.WHITE,"")
    if i == 7:
        break
    word = input("Enter a word you want your password to be a mixture of(The maximum is 3)\n")
    UserWordInput.append(word); n += 1
    if n == 99:
        break

    choice = input("Would you like to enter another word? Type 'yes' if you do, and 'no' if you dont\n")
    if choice == 'no'.casefold():
        break
    if choice == 'yes'.casefold():
        continue
    else:
        while i < 6:
            print (Fore.GREEN, "Sorry, you have typed a wrong input, which would you like? No or Yes?")
            wronginput = input("Input either 'yes' or 'no'\n")
            if wronginput == "yes".casefold():
                break
            if wronginput == "no".casefold():
                i = 7
                break
            else:
                i += 1


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
text = open(reason+".txt", "a+")
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
text.close()
countcomparison1  =(0)
countcomparison2  =(5)
countcomparison3  =(10)
countcomparison4  =(999)
SymbolCountComparison1 =(0)
SymbolCountComparison2 =(2)
SymbolCountComparison3 =(3)

txt = ".txt"
reason+(txt)
file = open(reason+".txt", "a")
file.write(reason)
file.write(" password is ")
file.write(VariableForList)
file.write("\n\tThe code has been run {} times\n".format(counter))
if countcomparison1 < Count < countcomparison2 or Count == countcomparison2 and SpecialCharacters > SymbolCountComparison1:
    file.write("\tThis password is - Weak\n")
    file.write("\tThe length of this password is: "+ str(Count)+ " characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters) + "\n")
    txt = ".txt"
    reason = reason + txt
    src = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', reason)
    des = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', 'Password-Generator-30-01-22/', 'Password file folder')
    folderpath = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"
    f2delete = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"+reason
    FileInFolder = os.path.exists(folderpath)
    file.close()
    if FileInFolder == True:
        os.remove(f2delete)
    file.close()
    shutil.move(src, des)
    quit()
elif countcomparison1 < Count < countcomparison2:
    file.write("\tThis password is - Slightly less than weak\n")
    file.write("\tThe length of this password is: "+ str(Count)+ " characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters) + "\n")
    txt = ".txt"
    reason = reason + txt
    src = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', reason)
    des = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', 'Password-Generator-30-01-22/', 'Password file folder')
    folderpath = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"
    f2delete = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"+reason
    FileInFolder = os.path.exists(folderpath)
    file.close()
    if FileInFolder == True:
        os.remove(f2delete)
    file.close()
    shutil.move(src, des)
    quit()
if countcomparison2 < Count < countcomparison3 and SpecialCharacters > SymbolCountComparison2 or Count == countcomparison2 and SpecialCharacters > SymbolCountComparison2:
    file.write("\tThis password is - Average\n")
    file.write("\tThe length of this password is: "+ str(Count)+ " characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters) + "\n")    
    txt = ".txt"
    reason = reason + txt
    src = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', reason)
    des = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', 'Password-Generator-30-01-22/', 'Password file folder')
    folderpath = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"
    f2delete = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"+reason
    FileInFolder = os.path.exists(folderpath)
    file.close()
    if FileInFolder == True:
        os.remove(f2delete)
    file.close()
    shutil.move(src, des)
    quit()
elif countcomparison2 < Count < countcomparison3 or Count == countcomparison2:
    file.write("\tThis password is - Slightly less than average\n")
    file.write("\tThe length of this password is: "+ str(Count)+ " characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters) + "\n")
    txt = ".txt"
    reason = reason + txt
    src = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', reason)
    des = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', 'Password-Generator-30-01-22/', 'Password file folder')
    folderpath = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"
    f2delete = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"+reason
    FileInFolder = os.path.exists(folderpath)
    file.close()
    if FileInFolder == True:
        os.remove(f2delete)
    file.close()
    shutil.move(src, des)
    quit()
if Count > countcomparison3 and SpecialCharacters > SymbolCountComparison3 or SpecialCharacters == SymbolCountComparison3 or Count == countcomparison3 and SpecialCharacters > SymbolCountComparison3 or SpecialCharacters == SymbolCountComparison3:
    file.write("\tThis password is - Strong\n")
    file.write("\tThe length of this password is: "+str(Count) +" characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters)+ "\n")
    txt = ".txt"
    reason = reason + txt
    src = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', reason)
    des = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', 'Password-Generator-30-01-22/', 'Password file folder')
    folderpath = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"+reason
    f2delete = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"+reason
    FileInFolder = os.path.exists(folderpath)
    file.close()
    if FileInFolder == True:
        os.remove(f2delete)
    file.close()
    shutil.move(src, des)
    quit()
elif Count > countcomparison3 or Count == countcomparison3:
    file.write("\tThis password is - Slightly less than strong\n")
    file.write("\tThe length of this password is: "+str(Count) +" characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters)+ "\n")
    txt = ".txt"
    reason = reason + txt
    src = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', reason)
    des = join('d:/', 'Applications/', 'Vscode/', 'Password Manager/', 'Password-Generator-30-01-22/', 'Password file folder')
    folderpath = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"
    f2delete = "d:/Applications/Vscode/Password Manager/Password-Generator-30-01-22/Password file folder/"+reason
    FileInFolder = os.path.exists(folderpath)
    file.close()
    if FileInFolder == True:
        os.remove(f2delete)
    file.close()
    shutil.move(src, des)