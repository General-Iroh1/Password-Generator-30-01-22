from cryptography.fernet import Fernet
from tkinter import *
import os.path
import os
import shutil
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
    Label(screen13,text="").pack()
    Button(screen13,text="Would you like to randomly generate a password?",command=randomgenerate1).pack()
    Label(screen13,text="").pack()
    Button(screen13,text="Create account", command=createuser).pack()
    Label(screen13,text="").pack()
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
        screen14 = Toplevel(screen)
        screen14.title("Success")
        screen14.geometry("200x150")
        Label(screen14, text = "Success!").pack()
        Label(screen14, text="").pack()
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

def back4():
    screen6.destroy()
    session()

def createpass():
    screen5.destroy()
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
    Label(screen6,text="").pack()
    Button(screen6, text="Create", command=save).pack()
    Label(screen6,text="").pack()
    Button(screen6, text="Back",command=back4).pack()
    Label(screen6,text="").pack()
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
    screen19.destroy()
    session()


def back11():
    screen18.destroy()
    viewpass()

def copy1():
    screen18.clipboard_clear()
    screen18.clipboard_append(filename1)
def copy3():
    screen36.clipboard_clear()
    screen36.clipboard_append(data3)
def copy2():
    screen36.clipboard_clear()
    screen36.clipboard_append(data13)
def copy4():
    screen35.clipboard_clear()
    screen35.clipboard_append(data10)
def copy5():
    screen34.clipboard_clear()
    screen34.clipboard_append(data11)
def copy6():
    screen33.clipboard_clear()
    screen33.clipboard_append(data12)

def viewpass2():
    global screen18
    global filename1
    filename1 = raw_filename.get()
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    screen18 = Toplevel(screen)
    screen18.title("Password view")
    screen18.geometry("500x500")
    file1 = open(res1x, "w+")
    data6 = file1.read()
    Label(screen18, text=data6).pack()
    Label(screen18,text="").pack()
    Button(screen18, text="Copy", command=copy1).pack()
    Label(screen18,text="").pack()
    Button(screen18, text="Back", command=back11).pack()
    Label(screen18, text="")
    Button(screen18, text="Quit", command=leave1).pack()


def viewpass2x2():
    global screen37
    global filename1
    filename1 = raw_filename.get()
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    screen37 = Toplevel(screen)
    screen37.title("Password view")
    screen37.geometry("500x500")
    file1 = open(res2x, "w+")
    file1.write(data13)
    Label(screen37, text=data13).pack()
    Label(screen37,text="").pack()
    Button(screen37, text="Copy", command=copy1).pack()
    Label(screen37,text="").pack()
    Button(screen37, text="Back", command=back22).pack()
    Label(screen37, text="")
    Button(screen37, text="Quit", command=leave1).pack()

def back22():
    screen37.destroy()
    viewpass()


def viewpass2x3():
    global screen36
    global filename1
    filename1 = raw_filename.get()
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    screen36 = Toplevel(screen)
    screen36.title("Password view")
    screen36.geometry("500x500")
    file1 = open(res3x, "w")
    file1.write(data3)
    Label(screen36, text=data3).pack()
    Label(screen36,text="").pack()
    Button(screen36, text="Copy", command=copy1).pack()
    Label(screen36,text="").pack()
    Button(screen36, text="Back", command=back21).pack()
    Label(screen36, text="")
    Button(screen36, text="Quit", command=quit).pack()

def back21():
    screen36.destroy()
    viewpass()


def viewpass2x4():
    global screen35
    global filename1
    filename1 = raw_filename.get()
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    screen35 = Toplevel(screen)
    screen35.title("Password view")
    screen35.geometry("500x500")
    file1 = open(res4x, "w+")
    file1.write(data10)
    Label(screen35, text=data10).pack()
    Label(screen35,text="").pack()
    Button(screen35, text="Copy", command=copy1).pack()
    Label(screen35,text="").pack()
    Button(screen35, text="Back", command=back20).pack()
    Label(screen35, text="")
    Button(screen35, text="Quit", command=quit).pack()

def back20():
    screen35.destroy()
    viewpass()


def viewpass2x5():
    global screen34
    global filename1
    filename1 = raw_filename.get()
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    screen34 = Toplevel(screen)
    screen34.title("Password view")
    screen34.geometry("500x500")
    file1 = open(res5x, "w+")
    file1.write(data11)
    Label(screen34, text=data11).pack()
    Label(screen34,text="").pack()
    Button(screen34, text="Copy", command=copy1).pack()
    Label(screen34,text="").pack()
    Button(screen34, text="Back", command=back19).pack()
    Label(screen34, text="")
    Button(screen34, text="Quit", command=quit).pack()

def back19():
    screen34.destroy()
    viewpass()


def viewpass2x6():
    global screen33
    global filename1
    filename1 = raw_filename.get()
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    screen33 = Toplevel(screen)
    screen33.title("Password view")
    screen33.geometry("500x500")
    file1 = open(res6x, "w+")
    file1.write(data12)
    Label(screen33, text=data12).pack()
    Label(screen33,text="").pack()
    Button(screen33, text="Copy", command=copy1).pack()
    Label(screen33,text="").pack()
    Button(screen33, text="Back", command=back18).pack()
    Label(screen33, text="")
    Button(screen33, text="Quit", command=quit).pack()

def back18():
    screen33.destroy()
    viewpass()

def viewpass1():
    screen8.destroy()
    screen21.destroy()
    global path0
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    global data3
    data = open(res1x, "r+")
    data3 = data.read()
    viewpass2()

def viewpass1x2():
    screen8.destroy()
    screen22.destroy()
    global path0
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    data = open (res2x, "r+")
    global data13
    data13 = data.read()
    viewpass2x2()

def viewpass1x3():
    screen8.destroy()
    screen24.destroy()
    data = open (res3x, "r")
    global data3
    data3 = data.read()
    viewpass2x3()

def viewpass1x4():
    screen8.destroy()
    screen25.destroy()
    global path0
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    data = open (res4x, "r+")
    global data10
    data10 = data.read()
    viewpass2x4()

def viewpass1x5():
    screen8.destroy()
    screen26.destroy()
    global path0
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    data = open (res5x, "r+")
    global data11
    data11 = data.read()
    viewpass2x5()

def back24():
    viewpass()

def viewpass1x6():
    screen8.destroy()
    screen27.destroy()
    data = open (res1x, "r+")
    global data12
    data12 = data.read()
    viewpass2x6()

def back23():
    viewpass()

def back1():
    screen8.destroy()
    session()
    
def res1():
    global screen21
    screen21 = Toplevel(screen)
    screen21.geometry("300x300")
    screen21.title("View")
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    filename3 = res1x
    file1 = open(filename3, "r")
    global f1r
    f1r =file1.read()
    viewpass1()

def res2():
    global screen22
    screen22 = Toplevel(screen)
    screen22.geometry("300x300")
    screen22.title("View")
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    filename3 = res2x
    file1 = open(filename3, "r")
    global f1r
    f1r =file1.read()
    viewpass1x2()

def res3():
    global screen24
    screen24 = Toplevel(screen)
    screen24.geometry("300x300")
    screen24.title("View")
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    filename3 = res3x
    file1 = open(filename3, "r")
    global f1r
    f1r =file1.read()
    viewpass1x3()

def res4():
    global screen25
    screen25 = Toplevel(screen)
    screen25.geometry("300x300")
    screen25.title("View")
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    filename3 = res4x
    file1 = open(filename3, "r")
    global f1r
    f1r =file1.read()
    viewpass1x4()

def res5():
    global screen26
    screen26 = Toplevel(screen)
    screen26.geometry("300x300")
    screen26.title("View")
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    filename3 = res5x
    file1 = open(filename3, "r")
    global f1r
    f1r =file1.read()
    viewpass1x5()

def res6():
    global screen27
    screen27 = Toplevel(screen)
    screen27.geometry("300x300")
    screen27.title("View")
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    filename3 = res6x
    file1 = open(filename3, "r")
    global f1r
    f1r =file1.read()
    viewpass1x6()



def viewpass():
    global screen8
    screen5.destroy()
    screen8 = Toplevel(screen)
    screen8.title("Password view")
    screen8.geometry("500x500")
    from os import walk
    res = []
    dir_path = "d:/Applications/Vscode/Password Manager/"+Var4UserEntry
    for (dir_path, dir_names, file_names) in walk(dir_path):
            res.extend(file_names)
    global res1x
    global res2x
    global res3x
    global res4x
    global res5x
    global res6x
    res1x = res[0]
    res2x = res[1]
    res3x = res[2]
    res4x = res[3]
    res5x = res[4]
    res6x = res[5]
    Label(screen8, text="Please select one of these files below(type it in the box).").pack()
    Button(screen8,text=res1x,command=res1).pack()
    Button(screen8,text=res2x,command=res2).pack()
    Button(screen8,text=res3x,command=res3).pack()
    Button(screen8,text=res4x,command=res4).pack()
    Button(screen8,text=res5x,command=res5).pack()
    Button(screen8,text=res6x,command=res6).pack()
    global raw_filename
    raw_filename = StringVar()
    Entry(screen8, textvariable=raw_filename).pack()
    Label(screen8,text="").pack()
    Button(screen8,command=viewpass1, text = "OK").pack()
    Label(screen8,text="").pack()
    Button(screen8, text="Back",command=back1).pack()

def back2():
    screen10.destroy()
    session()

def deletepass():
    screen5.destroy()
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Password delete")
    screen10.geometry("500x500")
    from os import walk
    res = []
    dir_path = "d:/Applications/Vscode/Password Manager/"+Var4UserEntry
    for (dir_path, dir_names, file_names) in walk(dir_path):
        res.extend(file_names)
        break
    res1x1 = res[0]
    res1x2 = res[1]
    res1x3 = res[2]
    res1x4 = res[3]
    res1x5 = res[4]
    res1x6 = res[5]
    Label(screen10, text="Please select one of the files below to delete (type it in the box).").pack()
    Button(screen10,text=res1x1).pack()
    Button(screen10,text=res1x2).pack()
    Button(screen10,text=res1x3).pack()
    Button(screen10,text=res1x4).pack()
    Button(screen10,text=res1x5).pack()
    Button(screen10,text=res1x6).pack()
    global raw_filename1
    raw_filename1 = StringVar()
    Label(screen10,text="").pack()
    Label(screen10,text="").pack()
    Button(screen10, text="Back",command=back2).pack()

def back3():
    screen19.destroy()

def back8():
    screen15.destroy()
    deletepass()

def deletepass1():
    screen5.destroy()
    screen10.destroy()
    global filename2
    filename2 = raw_filename1.get()
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    path1 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry+"/"+filename2)
    exists1 = os.path.exists(path1)
    if exists1 == False:
        global screen15
        screen15 = Toplevel(screen)
        screen15.title("Incorrect name")
        screen15.geometry("250x250")
        Label(screen15, text="Sorry, you have typed a wrong name").pack()
        Button(screen15, text="OK", command=back8).pack()
    data = open(filename1)
    global data1
    data1 = data


def back12():
    screen20.destroy()

def Password_not_recognised1():
    global screen20
    screen20 = Toplevel(screen)
    screen20.geometry("300x300")
    screen20.title("Incorrect")
    Label(screen20, text="Incorrect password")
    Button(screen20, text= "OK", command=back12)
def deletepass2():
    global screen19
    path0 = ("d:/Applications/Vscode/Password Manager/"+Var4UserEntry)
    os.chdir(path0)
    screen19 = Toplevel(screen)
    screen19.title("Password view")
    screen19.geometry("500x500")
    os.remove(filename2)
    Label(screen19, text=filename2+" removed").pack()
    Label(screen19,text="").pack()
    Button(screen19, text="Back", command=back).pack()
    Label(screen19,text="").pack()
    Button(screen19, text="Back", command=quit).pack()

def leave1():
    key = Fernet.generate_key()
    path2 = "d:/Applications/Vscode/Password Manager/"+Var4UserEntry
    os.chdir(path2)
    with open(res2x+".key", 'wb') as filekey:
        filekey.write(key)
    with open(res2x+".key", 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(res2x, 'r') as file:
        original = file.read()
    with open (res2x, "rb") as file1:
        original1 = file1.read()
    encrypted = fernet.encrypt(original1)
    with open(res2x, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    filefororiginal = open(res2x+" Original", "w")
    filefororiginal.write(original)
    filefororiginal.write("\n")
    filefororiginal.write(res2x)

    quit()

def session():
    screen1.destroy()
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Password options")
    screen5.geometry("400x400")
    Label(screen5, text="Feel free to view any passwords.").pack()
    Button(screen5,text = "Create password", command=createpass).pack()
    Label(screen5,text="").pack()
    Button(screen5,text = "View Passwords", command=viewpass).pack()
    Label(screen5,text="").pack()
    Button(screen5,text="Delete a password", command= deletepass).pack()



def Success():
    global User
    User = Username.get()
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
    p1ath = ("D:/Applications/Vscode/Password Manager/As Account")
    p2ath = os.path.exists("D:/Applications/Vscode/Password Manager/As Account/ER")
    p1athE = os.path.exists("d:/Applications/Vscode/Password Manager/"+Var4UserEntry+"/"+"ER Original")
    if Exist == True:
        if p1athE == True:
            os.chdir(p1ath)
            OGfile=open("ER Original", "r")
            OGFRead = OGfile.readlines()
            OGFReadS = OGFRead[1]
            OGfile.close()
            os.chdir(path)
            File=open(OGFReadS , "r")
            print (OGFReadS)

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
    Label(screen1,text="").pack()
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

global all
mainscreen()