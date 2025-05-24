import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = Label(root, text = "Correct text is :", font = ("arial", 20), bg="#dae6f6", fg="#364971")
    cs.place(x = 100, y = 250)
    spell.config(text = right)


heading = Label(root, text="Spelling Checker", font=("Arial", 30, "bold"),
                bg="#bcd4ee", fg="#2c3e50")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30,font=("Arial",25),bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root, text="Check", font=("Arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack()

spell=Label(root, font=("Arial", 20),bg="#dea6f6", fg="#364971")
spell.place(x=350, y=250)


root.mainloop()
