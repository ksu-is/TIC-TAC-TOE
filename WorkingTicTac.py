from tkinter import *
from tkinter import messagebox
window =Tk()



window.title("Welcome to Tommy  and Brandon's Tic Tac Toe Game")
window.geometry("550x300")

lbl=Label(window,text="TIC,TAC,TOE Game",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="Player 1 is: X",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Player 2 is: 0",font=('Helvetica','10'))
lbl.grid(row=2,column=0)

turn = 2  #For first person turn

def clicked1():
    global turn
    if btn1["text"]== " ":  #For getting the text of a button
        if turn==1:
            turn =2
            btn1["text"]="X"
        elif turn==2:
            turn=1
            btn1["text"]="O"
        check()   
def clicked2():
    global turn
    if btn2["text"]== " ":
        if turn==1:
            turn =2
            btn2["text"]="X"
        elif turn==2:
            turn=1
            btn2["text"]="O"
        check()  
def clicked3():
    global turn
    if btn3["text"]== " ":
        if turn==1:
            turn =2
            btn3["text"]="X"
        elif turn==2:
            turn=1
            btn3["text"]="O"
        check()
def clicked4():
    global turn
    if btn4["text"]== " ":
        if turn==1:
            turn =2
            btn4["text"]="X"
        elif turn==2:
            turn=1
            btn4["text"]="O"
        check()
def clicked5():
    global turn
    if btn5["text"]== " ":
        if turn==1:
            turn =2
            btn5["text"]="X"
        elif turn==2:
            turn=1
            btn5["text"]="O"
        check()
def clicked6():
    global turn
    if btn6["text"]== " ":
        if turn==1:
            turn =2
            btn6["text"]="X"
        elif turn==2:
            turn=1
            btn6["text"]="O"
        check()
def clicked7():
    global turn
    if btn7["text"]== " ":
        if turn==1:
            turn =2
            btn7["text"]="X"
        elif turn==2:
            turn=1
            btn7["text"]="O"
        check()
def clicked8():
    global turn
    if btn8["text"]== " ":
        if turn==1:
            turn =2
            btn8["text"]="X"
        elif turn==2:
            turn=1
            btn8["text"]="O"
        check()
def clicked9():
    global turn
    if btn9["text"]== " ":
        if turn==1:
            turn =2
            btn9["text"]="X"
        elif turn==2:
            turn=1
            btn9["text"]="O"
        check()

def clicked10():
    global turn
    if btn10["text"] == " ":
        if turn==1:
            turn = 2
            btn10["text"] = "X"
        elif turn==2:
            turn = 1
            btn10["text"] = "O"
        check()

def clicked11():
    global turn
    if btn11["text"] == " ":
        if turn==1:
            turn = 2
            btn11["text"] = "X"
        elif turn==2:
            turn = 1
            btn11["text"] = "O"
        check()

def clicked12():
    global turn
    if btn12["text"] == " ":
        if turn==1:
            turn = 2
            btn12["text"] = "X"
        elif turn==2:
            turn = 1
            btn12["text"] = "O"
        check()

def clicked13():
    global turn
    if btn13["text"] == " ":
        if turn==1:
            turn = 2
            btn13["text"] = "X"
        elif turn==2:
            turn = 1
            btn13["text"] = "O"
        check()

def clicked14():
    global turn
    if btn14["text"] == " ":
        if turn==1:
            turn = 2
            btn14["text"] = "X"
        elif turn==2:
            turn = 1
            btn14["text"] = "O"
        check()

def clicked15():
    global turn
    if btn15["text"] == " ":
        if turn==1:
            turn = 2
            btn15["text"] = "X"
        elif turn==2:
            turn = 1
            btn15["text"] = "O"
        check()

def clicked16():
    global turn
    if btn16["text"] == " ":
        if turn==1:
            turn = 2
            btn16["text"] = "X"
        elif turn==2:
            turn = 1
            btn16["text"] = "O"
        check()
flag=1
def check():
    global flag
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    b10 = btn10["text"]
    b11 = btn11["text"]
    b12 = btn12["text"]
    b13 = btn13["text"]
    b14 = btn14["text"]
    b15 = btn15["text"]
    b16 = btn16["text"]

    flag=flag+1
    if b1 == b2 and b1 == b3 and b1 == b4 and b1 == 'O' or b1 == b2 and b1 == b3 and b1 == b4 and b1=='X':
        win(btn1["text"])
    if b4 == b5 and b4==b6 and b4=='O' or b4==b5 and b4==b6 and b4=='X':
        win(btn4["text"])
    if b7==b8 and b7==b9 and b7=='O' or b7==b8 and b7==b9 and b7=='X':
        win(btn7["text"])
    if b1==b4 and b1==b7 and b1=='O' or b1==b4 and b1==b7 and b1=='X':
        win(btn1["text"])
    if b2==b5 and b2==b8 and b2=='O' or b2==b5 and b2==b8 and b2=='X':
        win(btn2["text"])
    if b3==b6 and b3==b9 and b3=='O' or b3==b6 and b3==b9 and b3=='X':
        win(btn3["text"])
    if b1==b5 and b1==b9 and b1=='O' or b1==b5 and b1==b9 and b1=='X':
        win(btn1["text"])
    if b7==b5 and b7==b3 and b7=='O' or b7==b5 and b7==b3 and b7=='X':
        win(btn7["text"])
    if flag ==10:
        messagebox.showinfo("Tie", "Match Tied!!! Try Again :)")
        window.destroy()

def win(player):
    ans = "Game Complete " + player + " wins. \n Thanks for playing our Game - Thomas and Brandon "
    messagebox.showinfo("Congratulations", ans)
    window.destroy() #used to close the program

btn1 = Button(window, text=" ", bg= "black", fg="yellow",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn1.grid(column=1, row=1)

btn2 = Button(window, text=" ", bg= "yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn2.grid(column=2, row=1)

btn3 = Button(window, text=" ", bg= "black", fg="yellow",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn3.grid(column=3, row=1)

btn4 = Button(window, text=" ", bg= "yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
btn4.grid(column=4, row=1)

btn5 = Button(window, text=" ", bg= "black", fg="yellow",width=3,height=1,font=('Helvetica','20'),command=clicked5)
btn5.grid(column=1, row=2)

btn6 = Button(window, text=" ", bg= "yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
btn6.grid(column=2, row=2)

btn7 = Button(window, text=" ", bg= "black", fg="yellow",width=3,height=1,font=('Helvetica','20'),command=clicked7)
btn7.grid(column=3, row=2)

btn8 = Button(window, text=" ", bg= "yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
btn8.grid(column=4, row=2)

btn9 = Button(window, text=" ", bg= "black", fg="yellow",width=3,height=1,font=('Helvetica','20'),command=clicked9)
btn9.grid(column=1, row=3)

btn10 = Button(window, text=" ",bg="yellow", fg="yellow", width=3, height=1,font=('Helvetica','20'),command=clicked10)
btn10.grid(column=2, row = 3)

btn11 = Button(window, text=" ",bg="yellow", fg="yellow", width=3, height=1,font=('Helvetica','20'),command=clicked10)
btn11.grid(column=3, row = 3)

btn12 = Button(window, text=" ",bg="yellow", fg="yellow", width=3, height=1,font=('Helvetica','20'),command=clicked10)
btn12.grid(column=4, row = 3)

btn13 = Button(window, text=" ",bg="yellow", fg="yellow", width=3, height=1,font=('Helvetica','20'),command=clicked10)
btn13.grid(column=1, row = 4)

btn14 = Button(window, text=" ",bg="yellow", fg="yellow", width=3, height=1,font=('Helvetica','20'),command=clicked10)
btn14.grid(column=2, row = 4)

btn15 = Button(window, text=" ",bg="yellow", fg="yellow", width=3, height=1,font=('Helvetica','20'),command=clicked10)
btn15.grid(column=3, row = 4)

btn16 = Button(window, text=" ",bg="yellow", fg="yellow", width=3, height=1,font=('Helvetica','20'),command=clicked10)
btn16.grid(column=4, row = 4)

window.mainloop()