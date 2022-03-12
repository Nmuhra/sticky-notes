from tkinter.filedialog import*
import tkinter as tk

canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("Notes")
canvas.config(bg = "yellow")
top = Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = "nw")

b1 = Button(canvas, text="Open", bg = "lightblue")
b1.pack(in_ = top, side=LEFT)

b2 = Button(canvas, text="save", bg = "lightblue")
b2.pack(in_ = top, side=LEFT)

canvas.mainloop()
