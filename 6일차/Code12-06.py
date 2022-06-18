from tkinter import *

window = Tk()
window.geometry("600x600")

photo = PhotoImage(file ='../수업자료/pet01.gif')

paper = Label(window, image=photo)
paper.pack(expand=1, anchor = CENTER)
window.mainloop()
