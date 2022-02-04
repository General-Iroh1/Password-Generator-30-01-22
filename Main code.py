#while loop
UserWordInput = []
i = 0
while i < 3:
    word = input("Enter A Word you want your password te be a mixture of(The maximum is 3): ")
    UserWordInput.append(word)
    

    choice = input("Would you like to enter another word? Press y if you do, and n if you dont: ")
    if choice.casefold() == 'n':
        break
    if choice.casefold() == 'y':
        i += 1
    else:
        print ("Sorry, you have typed a wrong input. The Password you have generated so far is: ")
        break

#Removes all commas/brackets/apostraphes
WordConnector = ""
VariableForList=(WordConnector.join(UserWordInput[:: -1]))
#Replacing words with symbols/numbers
VariableForList = VariableForList.replace('i', "!")
VariableForList = VariableForList.replace('a', "@")
VariableForList = VariableForList.replace('o', "0")
VariableForList = VariableForList.replace('q', "9")
VariableForList = VariableForList.replace('e', "£")
VariableForList = VariableForList.replace('u', "ⓤ")
#joining numbers to end and start of password
WordJoin="11"
VariableforJoining = VariableForList.join(WordJoin)
print (VariableforJoining)

