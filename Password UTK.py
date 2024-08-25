# UTK = using tkinter



import tkinter as tk
import mysql.connector as p
from tkinter import messagebox as ms




#connecting mysql
a=p.connect(host='localhost' , user= 'root' , password='123456' , database="password")
b=a.cursor()



def MainWindow():
    l3=tk.Label(root , text="HELLO!! Welcome to my first Project" , font=("Arial" , 20))
    l3.place(x=80 , y=100)
    l4=tk.Label(root , text="Choose One" , font=("Arial" , 20))
    l4.place(x=210 , y=160)
    
    loginbutton=tk.Button(root , text="Login" , border=10 , command=login , background="green" )
    loginbutton.place(x=210 , y=250)
    signupbutton=tk.Button(root , text="Signup", border=10 , command=signup)
    signupbutton.place(x=300,y=250)



def login():


    root.withdraw()
    rootl=tk.Tk()
    rootl.title("Login Page")
    wl = 600
    hl = 500
    wsl = rootl.winfo_screenwidth()
    hsl = rootl.winfo_screenheight()
    xl = (wsl/2) - (wl/2)
    yl = (hsl/2) - (hl/2)
    rootl.geometry('%dx%d+%d+%d' % (wl, hl, xl, yl))
    # rootl.resizable(False , False)

    l=[]
    iu=tk.Label(rootl , text="Invalid Username!!!!" , font=("Arial" , 14))
    ip=tk.Label(rootl , text="Wrong Password!!!!" , font=("Arial" , 14))


    def check_username(en):
        check_message()
    
        user_name = en.widget.get()
        b.execute("select * from passwords;")
        c=b.fetchall()
        for i in c:
            if (user_name == i[0] ):
                # check_message()
                en.widget.tk_focusNext().focus()
                l.append(user_name)
                break
        else:
            message_user()



    def check_password(ep):
        # check_message()

        p_word=ep.widget.get()
        f="select password from passwords where username = %s"
        b.execute(f,l)
        c=b.fetchall()
        for i in c:
            if (p_word == i[0]):
                check_message()
                ep.widget.tk_focusNext().focus()
                break
        else:
            message_pass()


    def message_user():
        iu.place(x=200 , y=280)


    def message_pass():
        ip.place(x=200 , y=280)


    def check_message(): 
        if (iu.winfo_exists()):
            # iu.destroy() This will remove the iu widget from the code for that particular run.
            iu.place_forget()
        if (ip.winfo_exists()):
            # ip.destroy() This will remove the ip widget from the code for that particular run.
            ip.place_forget()
        

    def button_clicked(position_argument):
        button.invoke()
    
    def login_successfull():
        
        # rootl.destroy()
        # rootls=tk.Tk()
        # rootls.title("Login Successfull")
        # success_window=tk.Toplevel(rootl)
        # success_window.title("Login Successful !!!")
        # success_window.geometry("300x200")
        # la1=tk.Label(success_window , text="Login Successfull!!!" )
        # la1.pack(pady=20)
        # button_exit=tk.Button(success_window , text="Exit" , command=success_window.destroy)
        # button_exit.pack()

        ms1=ms.showinfo("Login" , "Login Successfull")





    l1=tk.Label(rootl,  text='Username:' , font=("Arial" , 14))
    l1.place(x=160, y=165)
    l2=tk.Label(rootl, text='Password  :' , font=("Arial" , 14))
    l2.place(x=160 , y=190)





    en = tk.Entry(rootl)
    en.place( x=290,y=170)
    en.bind("<Return>" , check_username )
    ep = tk.Entry(rootl , show="*")
    ep.place( x=290 , y=200)
    ep.bind("<Return>" , check_password)





    button = tk.Button(rootl, text='Login', width=13, border=5  , command=login_successfull)
    button.place(x=230,y=250)
    button.bind("<Return>" ,button_clicked)



def signup():


    root.destroy()
    roots=tk.Tk()
    roots.title("SignUp Page")
    ws = 600
    hs = 500
    wss = roots.winfo_screenwidth()
    hss = roots.winfo_screenheight()
    xs = (wss/2) - (ws/2)
    ys = (hss/2) - (hs/2)
    roots.geometry('%dx%d+%d+%d' % (ws, hs, xs, ys))
    roots.resizable(False , False)

    list2=[]
    iu1=tk.Label(roots , text="Invalid Username!!!!" , font=("Arial" , 14))
    ip1=tk.Label(roots , text="Invalid Password!!!!" , font=("Arial" , 14))
    icp1=tk.Label(roots , text="Password Don't match!!!!" , font=("Arial" , 14))

    def valid_username(en):
        
        check_message1()
    
        user_name1 = en.widget.get()
        if (user_name1 != '' ):
            # check_message()
            en.widget.tk_focusNext().focus()
            list2.append(user_name1)
        else:
            message_user1()
    
    def valid_password(ep):
        
        check_message1()
        
        password1=ep.widget.get()
        if (password1 != ''):
            ep.widget.tk_focusNext().focus()
            list2.append(password1)
        else:
            message_pass1()
    
    def valid_confirm_password(ecp):
        
        check_message1()
        
        con_password=ecp.widget.get()
        if(con_password == list2[1]):
            ecp.widget.tk_focusNext().focus()
        else:
            # list2.pop()
            message_con_password()
    
    def check_message1():
        if (iu1.winfo_exists()):
            # iu.destroy() This will remove the iu widget from the code for that particular run.
            iu1.place_forget()
        if (ip1.winfo_exists()):
            # ip.destroy() This will remove the ip widget from the code for that particular run.
            ip1.place_forget()
        if (icp1.winfo_exists()):
            # ip.destroy() This will remove the ip widget from the code for that particular run.
            icp1.place_forget()
    
    def message_user1():
        iu1.place(x=200 , y=300)
    
    def message_pass1():
        ip1.place(x=200 , y=300)

    def message_con_password():
        icp1.place(x=200 , y=300)
    
    def button_clicked1(positional_argument1):
        f1='insert into passwords values("%s","%s")'
        b.execute(f1,list2)
        a.commit()
        print('Record Inserted Successfully')
        button.invoke()

    l1=tk.Label(roots , text="Username:" , font=("Arial" , 14))
    l1.place(x=166 , y=165)
    l2=tk.Label(roots , text= "Password:" , font=("Arial" , 14))
    l2.place(x=170 , y=190)
    l3=tk.Label(roots , text="Confirm Password:" , font=("Arial" , 14))
    l3.place(x=99 , y=215)



    en = tk.Entry(roots)
    en.place( x=290,y=170)
    en.bind("<Return>" , valid_username )
    ep = tk.Entry(roots)
    ep.place( x=290 , y=200)
    ep.bind("<Return>" , valid_password)
    ecp = tk.Entry(roots)
    ecp.place( x=290 , y=230)
    ecp.bind("<Return>" , valid_confirm_password)



    button = tk.Button(roots, text='SignUp', width=13, border=5  , command=roots.destroy)
    button.place(x=230,y=250)
    button.bind("<Return>" ,button_clicked1)


#making window
root = tk.Tk()

root.title('Welcome')

w = 600
h = 500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.config(background="#fff")

root.resizable(False , False)





#login()
#signup()
MainWindow()







root.mainloop()
