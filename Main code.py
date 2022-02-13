
import sys
from colorama import Fore
#counts how many times the code has been run
count = 0

def code_to_run():
  print("Running code")
  global count
  count +=1
import sys
from colorama import Fore
#while loop
UserWordInput = []
i = 0
n = 0
while True:
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
            if wronginput2 == "no":
                break
            if wronginput2 == "yes":
                continue
            else:
                print(Fore.RED,"You have one more try until you have to restart the program, please enter either yes or no very carefully.⚠️ IF YOU MISSPELL AGAIN, YOU WILL NOT GET ANOTHER TRY!\n")
                wronginput3 = input("last try, yes or no?\n")
                if wronginput3 == "yes":
                    continue
                if wronginput3 == "no":
                    break
                else:
                    print(Fore.BLACK,"You have misspelled 3 times, please restart the program to input more words.")
                    break
    

#Removes all commas/brackets/apostraphes
WordConnector = ""
VariableForList=(WordConnector.join(UserWordInput))
#Replacing words with symbols/numbers
VariableForList = VariableForList.replace('i', "!")
VariableForList = VariableForList.replace('a', "@")
VariableForList = VariableForList.replace('o', "0")
VariableForList = VariableForList.replace('q', "9")
VariableForList = VariableForList.replace('e', "E")
VariableForList = VariableForList.replace('u', "U")

#joining numbers to end and start of password
print (Fore.LIGHTBLUE_EX,"The password you have created is:", VariableForList)


print(Fore.WHITE,"")
reason = input("Why are you using this password?\n")
sys.stdout = open("Password Saver.txt", "a")
sys.stdout.write (reason)
sys.stdout.write (" password is: ")
sys.stdout.write (VariableForList)
sys.stdout.write (" You have ran the code {} times/time".format(count))
sys.stdout.write ("\n")

