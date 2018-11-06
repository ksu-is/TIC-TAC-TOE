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

    #If button text is empty, and click is true (player 1, or X), put an X in the button
    if buttons["text"] == " " and click == True:
        buttons["text"] == "X"
        click = False

    #If button text is empty, and click is false (player 2, or O), put an O in the button and change 
    #to player 1 turns (click = true)
    if buttons["text"] == " " and click == False:
        buttons["text"] == "O"
        click = True

    elif (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or 
          button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or 
          button7["text"] == "X" and button8["text"] == "X" and button8["text"]                                                                              )

