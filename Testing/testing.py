import shutil
from os.path import join
countcomparison3 = 98
countcomparison1 = 1
countcomparison2 = 8
countcomparison3 = 98
Count = 99
SpecialCharacters = 99
SymbolCountComparison3 = 100
SymbolCountComparison1 = 1
SymbolCountComparison2 = 8
SymbolCountComparison4 = 1
reason = input("Why would you like to use this password?\n")
file = open(reason+".txt", "a")
if countcomparison1 < Count < countcomparison2 or Count == countcomparison2 and SpecialCharacters > SymbolCountComparison1:
    file.write("\tThis password is - Weak\n")
    file.write("\tThe length of this password is: "+ str(Count)+ " characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters) + "\n")
    f = open(reason+".txt", "a")
    txt = ".txt"
    reason = reason + txt
    src = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', reason )
    des = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', 'Password file folder')
    f.write("")
    f.close()
    shutil.move(src, des)
    quit()
elif countcomparison1 < Count < countcomparison2:
    file.write("\tThis password is - Slightly less than weak\n")
    file.write("\tThe length of this password is: "+ str(Count)+ " characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters) + "\n")
    f = open(reason+".txt", "a")
    txt = ".txt"
    reason = reason + txt
    src = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', reason )
    des = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', 'Password file folder')
    f.write("")
    f.close()
    shutil.move(src, des)
    quit()
if countcomparison2 < Count < countcomparison3 and SpecialCharacters > SymbolCountComparison2 or Count == countcomparison2 and SpecialCharacters > SymbolCountComparison2:
    file.write("\tThis password is - Average\n")
    file.write("\tThe length of this password is: "+ str(Count)+ " characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters) + "\n")    
    f = open(reason+".txt", "a")
    txt = ".txt"
    reason = reason + txt
    src = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', reason )
    des = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', 'Password file folder')
    f.write("")
    f.close()
    shutil.move(src, des)
    quit()
elif countcomparison2 < Count < countcomparison3 or Count == countcomparison2:
    file.write("\tThis password is - Slightly less than average\n")
    file.write("\tThe length of this password is: "+ str(Count)+ " characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters) + "\n")
    f = open(reason+".txt", "a")
    txt = ".txt"
    reason = reason + txt
    src = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', reason )
    des = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', 'Password file folder')
    f.write("")
    f.close()
    shutil.move(src, des)
    quit()
if Count > countcomparison3 and SpecialCharacters > SymbolCountComparison3 or SpecialCharacters == SymbolCountComparison3 or Count == countcomparison3 and SpecialCharacters > SymbolCountComparison3 or SpecialCharacters == SymbolCountComparison3:
    file.write("\tThis password is - Strong\n")
    file.write("\tThe length of this password is: "+str(Count) +" characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters)+ "\n")
    f = open(reason+".txt", "a")
    txt = ".txt"
    reason = reason + txt
    src = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', reason )
    des = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', 'Password file folder')
    f.write("")
    f.close()
    shutil.move(src, des)
    quit()
elif Count > countcomparison3 or Count == countcomparison3:
    file.write("\tThis password is - Slightly less than strong\n")
    file.write("\tThe length of this password is: "+str(Count) +" characters long\n")
    file.write("\tThe amount of special characters in your password is: "+ str(SpecialCharacters)+ "\n")

    txt = ".txt"
    reason = reason + txt
    src = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', reason )
    des = join('c:/', 'Python Practice/', 'Password-Generator-30-01-22/', 'Password file folder')
    import os
    file.close()
    folderpath = "c:/Python Practice/Password-Generator-30-01-22/Password file folder/"+reason
    f2delete = "c:/Python Practice/Password-Generator-30-01-22/"+reason
    FileInFolder = os.path.exists(folderpath)
    if FileInFolder == True:
        os.remove(f2delete)
        quit()
    shutil.move(src, des)
