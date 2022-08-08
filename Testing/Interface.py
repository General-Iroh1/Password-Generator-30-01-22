from tkinter import *
import os.path
import os
import shutil
from unittest import TextTestResult
reason = "google"
counter = 1
def back5():
    screen13.destroy()

def randomgenerate1():
    import random
    randomlength = [8,9,10,11,12]
    passlegnth = random.choice(randomlength)
    passlegnth1 = passlegnth
    passlegnth2 = passlegnth
    ranlenplus1 = passlegnth + 1
    a = 1
    while ranlenplus1 > passlegnth:
        if a == 1:
            passlegnth = 1
        passlegnth = passlegnth + 1
        import string
        rletter = string.ascii_letters
        rletter2 = random.choice(rletter)
        if a == 1:
            list4letters = []
        list4letters.append(rletter2)
        if passlegnth == passlegnth1:
            global Varlist4letters
            Varlist4letters = "".join(list4letters)
            Varlist4letters = Varlist4letters.replace('i', "!")
            Varlist4letters = Varlist4letters.replace('I', "1")
            Varlist4letters = Varlist4letters.replace('a', "@")
            Varlist4letters = Varlist4letters.replace('A', "@")
            Varlist4letters = Varlist4letters.replace('o', "0")
            Varlist4letters = Varlist4letters.replace('O', "0")
            Varlist4letters = Varlist4letters.replace('Q', "9")
            Varlist4letters = Varlist4letters.replace('q', "9")
            Varlist4letters = Varlist4letters.replace('e', "E")
            Varlist4letters = Varlist4letters.replace('u', "U")
            Varlist4letters = Varlist4letters.replace('s', "$")
            Varlist4letters = Varlist4letters.replace('S', "$")
            Label(screen13,text="Your password is "+Varlist4letters).pack()
            Label(screen13,text="").pack()
            Button(screen13, text="Copy and paste random password", command=copyandpaste).pack()
        a = a + 1

def copyandpaste():
    screen13.clipboard_clear()
    screen13.clipboard_append(Varlist4letters)

def signup():
    global screen13
    screen13 = Toplevel(screen)
    screen13.title("Register")
    screen13.geometry("400x350")
    Label(screen13, text="Please create an account.").pack()
    Label(screen13, text="User").pack()
    global User
    User = StringVar()
    global Pass
    Pass = StringVar()
    Entry(screen13,textvariable=User).pack()
    Label(screen13,text="Password").pack()
    Entry(screen13,textvariable=Pass).pack()
    Button(screen13,text="Would you like to randomly generate a password?",command=randomgenerate1).pack()
    Button(screen13,text="Create account", command=createuser).pack()
    Button(screen13, text="Back", command= back5).pack()

def delete5():
    screen14.destroy()

def back10():
    screen17.destroy()

def createuser():
    global screen14
    VarUser = User.get()
    VarUser = VarUser + "s Account"
    folderpath = "d:/Applications/Vscode/Password Manager/"+VarUser
    exists2 = os.path.exists(folderpath)
    if exists2 == False:
        screen14 = Toplevel(screen13)
        screen14.title("Success")
        screen14.geometry("200x150")
        Button(screen14, text="OK", command=delete5).pack()
    VarUser = User.get()
    Var4Pass = Pass.get()
    if exists2 == False:
        file = open(VarUser, "w")
        file.write(Var4Pass)
        file.close()
    filepath = "d:/Applications/Vscode/Password Manager/"+VarUser
    global VarUser1
    VarUser1 = VarUser + "s password"
    VarUser = VarUser + "s Account"
    folderpath = "d:/Applications/Vscode/Password Manager/"+VarUser
    exists2 = os.path.exists(folderpath)
    if exists2 == True:
        global screen17
        screen17 = Toplevel(screen13)
        screen17.title("Account already exists")
        screen17.geometry("250x250")
        Label(screen17, text="This account already exists.").pack()
        Button(screen17, text="OK", command=back10).pack()
    if exists2 == False:
        os.makedirs(VarUser)
        folderpath = "d:/Applications/Vscode/Password Manager/"+VarUser
        os.makedirs (VarUser1)
        folderpath1 = "d:/Applications/Vscode/Password Manager/"+VarUser1
        shutil.move(folderpath1,folderpath)
        folderpath1 = "d:/Applications/Vscode/Password Manager/"+VarUser+"/"+VarUser1
        shutil.move(filepath,folderpath1)


def saved():
    screen7 = Toplevel(screen)
    screen7.title("Saved")
    screen7.geometry("50x50")
    Label(screen7,text = "Saved: ").pack()


def save():
    filename1 = filename.get()
    password2 = password.get()

    path2 = "d:/Applications/Vscode/Password Manager/"+Var4UserEntry
    os.chdir(path2)
    data = open(filename1, "w")
    data.write(password2)
    data.close()

    saved()

def back4():
    screen6.destroy()

def randomgenerate():
    import random
    randomlength = [8,9,10,11,12]
    passlegnth = random.choice(randomlength)
    passlegnth1 = passlegnth
    passlegnth2 = passlegnth
    ranlenplus1 = passlegnth + 1
    a = 1
    while ranlenplus1 > passlegnth:
        if a == 1:
            passlegnth = 1
        passlegnth = passlegnth + 1
        import string
        rletter = string.ascii_letters
        rletter2 = random.choice(rletter)
        if a == 1:
            list4letters = []
        list4letters.append(rletter2)
        if passlegnth == passlegnth1:
            global Varlist4letters
            Varlist4letters = "".join(list4letters)
            Varlist4letters = Varlist4letters.replace('i', "!")
            Varlist4letters = Varlist4letters.replace('I', "1")
            Varlist4letters = Varlist4letters.replace('a', "@")
            Varlist4letters = Varlist4letters.replace('A', "@")
            Varlist4letters = Varlist4letters.replace('o', "0")
            Varlist4letters = Varlist4letters.replace('O', "0")
            Varlist4letters = Varlist4letters.replace('Q', "9")
            Varlist4letters = Varlist4letters.replace('q', "9")
            Varlist4letters = Varlist4letters.replace('e', "E")
            Varlist4letters = Varlist4letters.replace('u', "U")
            Varlist4letters = Varlist4letters.replace('s', "$")
            Varlist4letters = Varlist4letters.replace('S', "$")
            Label(screen6,text="Your password is "+Varlist4letters).pack()
            Label(screen6,text="").pack()
            Button(screen6, text="Copy and paste", command= copyandpaste1).pack()
        a = a + 1

def copyandpaste1():
    screen6.clipboard_clear()
    screen6.clipboard_append(Varlist4letters)

def createpass():
    global filename
    global screen6
    filename = StringVar()
    global password
    password = StringVar()

    screen6 = Toplevel(screen)
    dir_path = "d:/Applications/Vscode/Password Manager/"+Var4UserEntry
    os.chdir(dir_path)
    screen6.title("Create")
    screen6.geometry("400x350")
    Label(screen6,text = "Please enter a reason for a password: ").pack()
    Entry(screen6,textvariable=filename).pack()
    Label(screen6,text = "").pack()
    Label(screen6,text = "Please enter a password: ").pack()
    Entry(screen6,textvariable=password).pack()
    Button(screen6, text="Create", command=save).pack()
    Label(screen6,text="").pack()
    Button(screen6, text="Back",command=back4).pack()
    Button(screen6,text="Would you like to randomly generate a password?",command=randomgenerate).pack()
    Label(screen6,text="").pack()

def Login_Success():
    session()
def delete3():
    screen3.destroy()

def Password_not_recognised():
    global screen3
    screen3 = Toplevel(screen1)
    screen3.title("Password error")
    screen3.geometry("250x200")
    Label(screen3,text="Wrong password entered.").pack()
    Button(screen3, text = "OK", command=delete3).pack()

def delete4():
    screen4.destroy()

def user_not_found():
    global screen4
    screen4 = Toplevel(screen1)
    screen4.title("User not found")
    screen4.geometry("250x200")
    Label(screen4,text="User not found").pack()
    Button(screen4, text = "OK", command=delete4).pack()
    
def back():
    screen11.destroy()

def back7():
    screen9.destroy()

def back9():
    screen16.destroy()

def viewpass1():
    global screen9
    filename1 = raw_filename.get()
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    path1 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry+"/"+filename1)
    exists1 = os.path.exists(path1)
    if exists1 == False:
        global screen16
        screen16 = Toplevel(screen1)
        screen16.title("Incorrect name")
        screen16.geometry("250x250")
        Label(screen16, text="Sorry, you have typed a wrong name").pack()
        Button(screen16, text="OK", command=back9).pack()
    data = open (filename1, "r")
    data1 = data.read()
    screen9 = Toplevel(screen1)
    screen9.title("Password view")
    screen9.geometry("500x500")
    Label(screen9, text=data1).pack()
    Label(screen9,text="").pack()
    Button(screen9, text="Back", command=back7).pack()


def back1():
    screen8.destroy()

def viewpass():
    global screen8
    screen8 = Toplevel(screen1)
    screen8.title("Password view")
    screen8.geometry("500x500")
    from os import walk
    res = []
    dir_path = "d:/Applications/Vscode/Password Manager/"+Var4UserEntry
    for (dir_path, dir_names, file_names) in walk(dir_path):
        res.extend(file_names)
        break
    Label(screen8, text="Please select one of these files below(type it in the box).").pack()
    Var4res = "\n".join(res)
    Label(screen8,text=Var4res).pack()
    global raw_filename
    raw_filename = StringVar()
    Entry(screen8, textvariable=raw_filename).pack()
    Button(screen8,command=viewpass1, text = "OK").pack()
    Label(screen8,text="").pack()
    Button(screen8, text="Back",command=back1).pack()

def back2():
    screen10.destroy()

def deletepass():
    global screen10
    screen10 = Toplevel(screen1)
    screen10.title("Password view")
    screen10.geometry("500x500")
    from os import walk
    res = []
    dir_path = "d:/Applications/Vscode/Password Manager/"+Var4UserEntry
    for (dir_path, dir_names, file_names) in walk(dir_path):
        res.extend(file_names)
        break
    Label(screen10, text="Please select one of the files below to delete (type it in the box).").pack()
    Var4res1 = "\n".join(res)
    Label(screen10,text=Var4res1).pack()
    global raw_filename1
    raw_filename1 = StringVar()
    Entry(screen10, textvariable=raw_filename1).pack()
    Button(screen10,command=deletepass1, text = "OK").pack()
    Label(screen10,text="").pack()
    Button(screen10, text="Back",command=back2).pack()

def back3():
    screen11.destroy()

def back8():
    screen15.destroy()

def deletepass1():
    global screen11
    filename2 = raw_filename1.get()
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    path1 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry+"/"+filename2)
    exists1 = os.path.exists(path1)
    if exists1 == False:
        global screen15
        screen15 = Toplevel(screen1)
        screen15.title("Incorrect name")
        screen15.geometry("250x250")
        Label(screen15, text="Sorry, you have typed a wrong name").pack()
        Button(screen15, text="OK", command=back8).pack()
    os.remove(filename2)
    screen11 = Toplevel(screen1)
    screen11.title("Password view")
    screen11.geometry("500x500")
    Label(screen11, text=filename2+" removed").pack()
    Label(screen11,text="").pack()
    Button(screen11, text="Back", command=back).pack()


def session():
    screen5 = Toplevel(screen1)
    screen5.title("Password options")
    screen5.geometry("400x400")
    Label(screen5, text="Feel free to view any passwords.").pack()
    Button(screen5,text = "Create password", command=createpass).pack()
    Button(screen5,text = "View Passwords", command=viewpass).pack()
    Button(screen5,text="Delete a password", command= deletepass ).pack()



def Success():
    global User

    User = Username.get()
    Pass = Password.get()
    global username1
    global password1
    username1 = Username.get()
    password1 = Password.get()
    global Var4UserEntry
    Var4UserEntry = User_Entry.get()
    global Var4UserEntry2
    Var4UserEntry2 =  Var4UserEntry
    Var4UserEntry = Var4UserEntry + "s Account"
    Exist = os.path.exists("d:/Applications/Vscode/Password Manager/"+Var4UserEntry+"/"+Var4UserEntry2+"s password")
    global path
    path = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry+"/"+Var4UserEntry2+"s password")
    if Exist == True:
        os.chdir(path)
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            Login_Success()
        else:
            Password_not_recognised()
    if Exist == False:
        user_not_found()

def passwordview():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title(reason)
    screen1.geometry("400x350")
    
    global Username
    global Password

    Username = StringVar()
    Password = StringVar()

    global User_Entry
    global Pass_Entry

    Label(screen1, text = "Enter username & password below:").pack()
    Label(screen1, text = "Username * ").pack()
    User_Entry =Entry(screen1, textvariable=Username)
    User_Entry.pack()
    Label(screen1, text = "Password * ").pack()
    Pass_Entry =Entry(screen1, textvariable=Password)
    Pass_Entry.pack()
    Button(screen1, text="Confirm", width = 10, height = 1, command =Success).pack()
    Label(screen1, text = "").pack()
    Button(screen1, text="Back", command= back6).pack()

def back6():
    screen1.destroy()


def mainscreen():
    global screen
    screen = Tk()
    screen.geometry("400x350")
    screen.title("Password Manager")
    Label(text = "Please sign in.", width= "30", height= "2", bg = "grey", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", width= "30", height= "2",command = passwordview).pack()
    Label(text = "").pack()
    Button(text="Register", width="30", height="2",command= signup).pack()
    screen.mainloop()


mainscreen()