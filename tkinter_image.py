from tkinter import *
from PIL import ImageTk, Image

root = Tk()

img = Image.open('stand.png')

img_Tk = ImageTk.PhotoImage(img)

img_label = Label(root, image=img_Tk)

img_label.pack()

root.mainloop() 