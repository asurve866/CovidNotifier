from tkinter import *
from tkinter import messagebox

import pymysql
import requests
from PIL import ImageTk


class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1280x823+100+50")
        self.root.resizable(False,False)
        #For Background Image
        self.bg = ImageTk.PhotoImage(file="images/F1.large.jpg")
        self.bg_image = Label(self.root,image = self.bg)
        self.bg_image.place(x=0,y=0,relwidth= 1,relheight= 1)

        #Login Frame
        frame_login = Frame(self.root,bg="white")

        frame_login.place(x = 150,y = 150 , height = 500,width = 700)

        title = Label(frame_login,text="Login",font = ("Impact",36,"bold"),fg = "#d77337",bg = "white").place(x = 90,y = 30)

        lbl_email = Label(frame_login,text="Email",font=("Goudy old style",20,"bold"),fg = "#d25d17",bg = "white").place(x = 100 , y = 150)
        self.txt_email = Entry(frame_login,font=("times new roman",20),bg = "lightgrey")
        self.txt_email.place(x = 100 , y = 190)


        lbl_password = Label(frame_login, text="Password", font=("Goudy old style", 20, "bold"), fg="#d25d17",bg="white").place(x=100, y=250)
        self.txt_password = Entry(frame_login, font=("times new roman", 20), bg="lightgrey")
        self.txt_password.place(x=100, y=290)

        login_btn = Button(frame_login,text="Login",font=("Goudy old style",20,"bold"),command = self.login,fg="white",bg = "#d77337").place(x = 100 ,y = 350,width = 120)

        register_btn = Button(frame_login,text = "Register Here",font=("times new roman",20),command = self.register_window,fg = "#d77337").place(x = 250,y = 350,width = 150)

    # def init_database(self):
    #     url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india_timeline"
    #
    #     headers = {
    #         'x-rapidapi-key': "605b4b32f7mshb0549da9ead0686p1256bfjsn9320046492fe",
    #         'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    #     }
    #
    #     response = requests.request("GET", url, headers=headers).json()
    #
    #     for each in response['state_wise']:
    #         print(each)





    def register_window(self):
        self.root.destroy()
        import register

    def clear(self):
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)

    def login(self):
        if self.txt_email == "" or self.txt_password == "":
            messagebox.showerror("Error","Please Fill All Area's",parent = self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="Vruddhi@9",database="data")
                cur = con.cursor()
                cur.execute("select * from user where email = %s and password = %s",(self.txt_email.get(),self.txt_password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Email and Password",parent = self.root)
                    self.clear()
                else:
                    messagebox.showinfo("Success","Welcome",parent = self.root)
                    con.close()
                    self.clear()

            except EXCEPTION as e:
                messagebox.showerror("Error",f"The error is :{str(e)}",parent = self.root)

root = Tk()
obj = Login(root)
root.mainloop()