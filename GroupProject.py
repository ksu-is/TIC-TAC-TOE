#Code reference  https://www.youtube.com/watch?v=RuYg_D_ppYk

#Import all tkinter functionalities for manipulating the GUI
from tkinter import *

#Import box that will show up
import tkinter.messagebox

gui = Tk()

gui.title("Brandon and Tommy's Tic, Tac, Toe Game")

clicker = True

def checker(buttons):
    global clicked
    clicker = True

    #If button text is empty, and click is true (player 1, or X), put an X in the button
    if buttons["text"] == " " and clicker == True:
        buttons["text"] == "X"
        click = False

    #If button text is empty, and click is false (player 2, or O), put an O in the button and change 
    #to player 1 turns (click = true)
    if buttons["text"] == " " and clicker == False:
        buttons["text"] == "O"
        clicker = True

        #Checks win condition for X horiontally
    elif (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or 
          button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or 
          button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
          
          #Checks win condition for X diagnally
          button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or 
          button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
          
          #Checks win condition for X veritcally
          button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
          button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
          button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):

            tkinter.messagebox.showinfo("The Winner is X (player 1)!")

    #Checks win condition for O horiontally
    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or 
          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or 
          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
          
          #Checks win condition for O diagnally
          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or 
          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
          
          #Checks win condition for O veritcally
          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):

            tkinter.messagebox.showinfo("The Winner is O (player 2)!")
                
    
buttons = StringVar()

button1 = Button(gui, text = "", font= "Times 26 bold", height = 4, width = 8, command=lambda:checker(button1))                                                           
button1.grid(row = 1, column = 0, sticky = S+N+E+W)

button2 = Button(gui, text = "", font= "Times 26 bold", height = 4, width = 8, command=lambda:checker(button2))
button2.grid(row = 1, column = 1, sticky = S+N+E+W)

button3 = Button(gui, text = "", font= "Times 26 bold", height = 4, width = 8, command=lambda:checker(button3))
button3.grid(row = 1, column = 2, sticky = S+N+E+W)

button4 = Button(gui, text = "", font= "Times 26 bold", height = 4, width = 8, command=lambda:checker(button4))
button4.grid(row = 2, column = 0, sticky = S+N+E+W)

button5 = Button(gui, text = "", font= "Times 26 bold", height = 4, width = 8, command=lambda:checker(button5))
button5.grid(row = 2, column = 1, sticky = S+N+E+W)

button6 = Button(gui, text = "", font= "Times 26 bold", height = 4, width = 8, command=lambda:checker(button6))
button6.grid(row = 2, column = 2, sticky = S+N+E+W)

button7 = Button(gui, text = "", font= "Times 26 bold", height = 4, width = 8, command=lambda:checker(button7))
button7.grid(row = 3, column = 0, sticky = S+N+E+W)

button8 = Button(gui, text = "", font= "Times 26 bold", height = 4, width = 8, command=lambda:checker(button8))
button4.grid(row = 3, column = 1, sticky = S+N+E+W)

button9 = Button(gui, text = "", font= "Times 26 bold", height = 4, width = 8, command=lambda:checker(button9))
button9.grid(row = 3, column = 2, sticky = S+N+E+W)

gui.mainloop()