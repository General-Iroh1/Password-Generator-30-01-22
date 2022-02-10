#while loop
import sys

UserWordInput = []
i = 0
n = 0
while True:
    word = input("Enter A Word you want your password te be a mixture of(The maximum is 3): ")
    UserWordInput.append(word); n += 1
    if n == 3:
        break

    choice = input("Would you like to enter another word? Type 'yes' if you do, and 'no' if you dont: ")

    if choice.casefold() == 'no':
        break
    if choice.casefold() == 'yes':
        continue
    else:
        print ("Sorry, you have typed a wrong input, your input has been counted as 'yes'")
    continue
    

#Removes all commas/brackets/apostraphes
WordConnector = ""
VariableForList=(WordConnector.join(UserWordInput))
#Replacing words with symbols/numbers
VariableForList = VariableForList.replace('i', "!")
VariableForList = VariableForList.replace('a', "@")
VariableForList = VariableForList.replace('o', "0")
VariableForList = VariableForList.replace('q', "9")
VariableForList = VariableForList.replace('e', "£")
VariableForList = VariableForList.replace('u', "U")

#joining numbers to end and start of password
print ("The password you have created is:", VariableForList)



stdoutOrigin=sys.stdout 
sys.stdout = open("Password Saver.txt", "w")
sys.stdout.close()
sys.stdout=stdoutOrigin