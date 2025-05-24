import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="black")

heading= Label(root,text="Spelling Checker", font=("Arial",30, "bold"), bg="#dea6f6", fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30,font=("Arial",25),bg="white" border=2)
enter_text.pack()


root.mainloop()
