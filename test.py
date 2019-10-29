from tkinter import *


def clicked():
    label["text"] = entry.get()


def onclick():
    pass


root = Tk()

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

button = Button(master=root, text='Vertrektijden laden', command=clicked)
button.pack(pady=10)

text = Text(root)
text.insert(INSERT, "Dummy tekst " )
split("/n")
text.insert(END, "Op 2 regels")
text.pack()


button = Button(master=root, text='Terug naar Hoofdscherm', command=clicked)
button.pack(pady=10)


root.mainloop()
