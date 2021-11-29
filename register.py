from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

import pymysql
class Register :
    def __init__(self,root):
        self.root = root
        self.root.title("COVID NOTIFIER Window")
        self.root.geometry("1280x823+0+0")
        self.root.resizable(False,False)
        self.root.config(bg="white")

        #Inserting Image
        self.bg = ImageTk.PhotoImage(file="images/F1.large.jpg")
        bg = Label(self.root,image = self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Message Image
        img=Image.open("images/img_2.png")
        resize_image3=img.resize((400,300))
        self.left = ImageTk.PhotoImage(resize_image3)
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        #Register Frame
        frame1 = Frame(self.root,bg="white")
        frame1.place(x=500,y=100,width=700,height=500)

        title = Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="#33ABF9").place(x=50,y = 30)

    #--------------------------------------------------------------------------------------------------------------------------------
        f_name = Label(frame1,text="First Name",font=("times new roman",12,"bold"),bg="white",fg="#33ABF9").place(x = 50,y = 100)
        self.txt_fname = Entry(frame1,font=("times new roman",12),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width = 250)


        l_name = Label(frame1, text="Last Name", font=("times new roman", 12, "bold"), bg="white", fg="#33ABF9").place(x=320, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 12), bg="lightgrey")
        self.txt_lname.place(x=320, y=130, width=250)
        #----------------------------------------------------------------------------------------------------------------------

        contact = Label(frame1, text="Contact No.", font=("times new roman", 12, "bold"), bg="white", fg="#33ABF9").place(x=50, y=160)
        self.txt_contact = Entry(frame1, font=("times new roman", 12), bg="lightgrey")
        self.txt_contact.place(x=50, y=190, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 12, "bold"), bg="white", fg="#33ABF9").place(x=320, y=160)
        self.txt_email = Entry(frame1, font=("times new roman", 12), bg="lightgrey")
        self.txt_email.place(x=320, y=190, width=250)

        #---------------------------------------------------------------------------------------------------------------------

        question = Label(frame1, text="Security Question", font=("times new roman", 12, "bold"), bg="white", fg="#33ABF9").place(x=50, y=220)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 12),state="readonly",justify="center")
        self.cmb_quest['values'] = ("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50, y=250, width=250)
        self.cmb_quest.current(0)


        answer = Label(frame1, text="Answer", font=("times new roman", 12, "bold"), bg="white", fg="#33ABF9").place(x=320,y=220)
        self.txt_answer = Entry(frame1, font=("times new roman", 12), bg="lightgrey")
        self.txt_answer.place(x=320, y=250, width=250)

    #-------------------------------------------------------------------------------------------------------------------------------

        password = Label(frame1, text="Password", font=("times new roman", 12, "bold"), bg="white", fg="#33ABF9").place(x=50, y=290)
        self.txt_password = Entry(frame1, font=("times new roman", 12), bg="lightgrey")
        self.txt_password.place(x=50, y=320, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 12, "bold"), bg="white", fg="#33ABF9").place(x=320, y=290)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 12), bg="lightgrey")
        self.txt_cpassword.place(x=320, y=320, width=250)

    #-------------------------------------------------------------------------------------------------------------------------------
        self.var_chk = IntVar()
        chk = Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue = 1,offvalue = 0,bg = "white",font = ("times new roman",12)).place(x = 50 , y =350)
        #Register Button Image
        image=Image.open("images/img_3.png")
        resize_image=image.resize((300,100))
        self.btn_img = ImageTk.PhotoImage(resize_image)

        #Sign In Button Image
        img2=Image.open("images/img_4.png")
        sign_in_button=img2.resize((250,75))
        self.sign_in=ImageTk.PhotoImage(sign_in_button)

        btn_register= Button(frame1,image = self.btn_img,bd = 0,cursor = "hand2",command = self.register_data).place(x = 50 ,y = 370)

        btn_login = Button(self.root,image=self.sign_in,command = self.login_window,cursor="hand2", bd=0).place(x=150, y=520)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)


    def login_window(self):
        self.root.destroy()
        import login

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.txt_answer.get() == ""or self.cmb_quest.get() == "Select" or self.txt_password.get() == "" or self.txt_cpassword.get() == "" :
            messagebox.showerror("Error" , "All Fields Are Required" ,parent = self.root)

        elif self.txt_password.get() != self.txt_cpassword.get() :
            messagebox.showerror("Error","Password & Confirm Password should be Same",parent = self.root)

        elif self.var_chk.get() == 0:
            messagebox.showerror("Error" , "Please Agree our Terms & Conditions",parent = self.root)
        else:
            #database query
            # create database data; //To create a database
            # create table user(id varchar(20) ,f_name varchar(50),l_name varchar(50) , contact varchar(10),email varchar(100) , question varchar(100),answer varchar(50),password varchar(20));

            try :
                con = pymysql.connect(host="localhost",user="root",password="Vruddhi@9",database="data") # change according to your database
                cur = con.cursor()
                cur.execute("select * from user where email=%s",self.txt_email.get())
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exists,Please try with another email",parent=self.root)

                else:
                    cur.execute(
                                    "insert into user (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.cmb_quest.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get()
                                    )
                                )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfull",parent=self.root)
                    self.clear()

            except EXCEPTION as e:
                messagebox.showerror("Error","Error ,Please Try Again",parent = self.root)
                print(e)

root = Tk()
obj = Register(root)
root.mainloop()
