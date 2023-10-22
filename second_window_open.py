from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New Window Open")

def open():
    global my_img
    top = Toplevel()
    top.title("new_windows")
    my_img= ImageTk.PhotoImage(Image.open("images/fish/bignosefish.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy)


btn=Button(root, text="open-image", command=open).pack()


mainloop()