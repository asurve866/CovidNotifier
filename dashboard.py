from tkinter import *
from PIL import ImageTk

class Dashboard:
    def __init__(self,root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1280x823+100+50")
        self.root.resizable(False,False)

        self.bg = PIL.ImageTk.PhotoImage(file ="images/F1.large.jpg")
        self.bg_image = Label(self.root, image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(self.root, bg = "white")
        frame1.place(x = 50,y = 50,width = 1100 , height = 700)

        lbl_state = Label(frame1,text = "States",font = ("times new roman",20,"bold"),bg = "white").place(x = 70 , y = 30)





root = Tk()
obj = Dashboard(root)
root.mainloop()

