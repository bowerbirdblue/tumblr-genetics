'''IMPORTING PACKAGAGES'''
import Bio as bio # imports biopython
from Bio import Blast as blast # from biopython, import BLAST
from Bio.Blast import NCBIWWW # from biopython BLAST, import NCBIWWW
from Bio.Seq import Seq as seq # from biopython Seq, import Seq
import tkinter as tk # imports tkinter
from tkinter import scrolledtext as scr
from tkinter import ttk # from tkinter, imports ttk
from tkinter import messagebox # from tkinter, imports messagebox
import datetime as dt # imports datetime
import re # imports regex
'''BIOPYTHON SETTINGS'''
blast.email = "levihrpender@gmail.com" # sets blast email variable (required by NCBI)
'''TKINTER SETTINGS'''
root = tk.Tk() # creates Tk root widget (window)
root.title("So anyway, I started BLASTing") # sets title of tkinter window
root.geometry('800x700') # sets initial size of tkinter window
'''CLEARS MY_BLAST'''
open("my_blast.xml", "w").close
#
font =("Autour One")
'''CREATES FRAMES FOR TKINTER WINDOW'''
leftFrame = tk.Frame(root, width=400, height=300, relief="raised", borderwidth=5) # creates text entry frame
leftFrame.place(anchor="nw", x=0, y=0, width=400, height=300) # places text entry frame (top left)

subFrame = tk.Frame(root, width=200, height=50, relief="sunken", borderwidth=5) # creates submit button frame
subFrame.place(anchor="nw", x=0, y=300, width=200, height=40) # places submit button frame (middle left, under leftFrame)

rightFrame = tk.Frame(root, width=400, height=350, relief="raised", borderwidth=5) # creates (currently) empty frame
rightFrame.place(anchor="nw", x=400, y=0, width=400, height=350) # places frame (top right)
'''
VARIABLES
'''

'''
DATE TIME FUNCTION
-
    - gets current date and time
'''
def dID():
    dateID = dt.datetime.now() # gets current datetime
    #print(dateID)
'''
REGEX FUNCTION
-
    - preforms regex
'''
def regex(search):
   global mySeq
   expression = re.compile(r'[actg]')
   findall = expression.findall(search)
   mySeq = seq(''.join(findall))
   print(mySeq)
'''
POST-SUBMIT WIDGETS FUNCTION
-
    - creates widgets that should only appear after a submission
''' 
def submitWidgets():
    tk.Label(rightFrame, text="Text entered:", font=(font, 17), relief="groove").pack(side="top", anchor="w")
    tk.Label(rightFrame, text=preText, font=(font, 15), width=1, height=1).pack(side="top", anchor="w", fill="both", expand=1)
    print(f"Submitted Text:{preText}")
    tk.Label(rightFrame, text="Regex results:", font=(font, 17), relief="groove").pack(side="top", anchor="w")
    tk.Label(rightFrame, text=mySeq, font=(font, 15), width=1, height=1).pack(side="top", anchor="w", fill="both", expand=1)
    print(f"Regex Results:{mySeq}")
    

'''
BLAST FUNCTION
'''
def blasting():
    try:
        BLASTit = blast.qblast(program = "blastn", database = "nt", sequence = mySeq)
        messagebox.showinfo(message="Yay!")
    except:
        print("Aw.")
    with open ("my_blast.xml", "wb") as out_stream:
            out_stream.write(BLASTit.read())
    BLASTit.close()
    result_stream = open("my_blast.xml", "rb")
    blast_record = blast.read(result_stream)
    hit = blast_record[0]
    org = hit.target.description
    print(f"Closest Match: {org}")
    tk.Label(rightFrame, text=org, font=(font, 15)).pack(side="top",anchor="w")
'''
SUBMISSION FUNCTION
-
    - submits text entered into text entry box
    - calls regex function using afformentioned text
    - clears text box
    - clears my_blast
    
'''
def submitFunc():
    global preText
    open("my_blast.xml", "w").close
    preText = textInput.get("1.0","end-1c")
    regex(preText)
    submitWidgets()
    textInput.delete("1.0", "end")   
    blasting()

'''
APP WINDOW FUNCTION
-
    - makes root resizable
    - calls root main loop
    - creates Tk widgets
    - place widgets in frames in window
'''
def appWin():
    global textInput
    '''LEFT SIDE'''
    root.resizable(True, True) # makes window resizable
    tk.Label(leftFrame, text="Please enter the text\nyou want sequenced here:", font=(font, 17)).pack(side="top") # creates and places label for text entry
    textInput = tk.Text(leftFrame, height=25, width=50, font=(font, 15)) # creates text entry
    textInput.pack(side="bottom", fill="x") # places text entry
    submit = tk.Button(subFrame, font=(font, 17), text="Submit", command=submitFunc) # creates submission button
    submit.pack(fill="both") # places submission button
    '''RIGHT SIDE'''
    
    root.mainloop() # calls Tk main loop 
appWin() # calls appWin