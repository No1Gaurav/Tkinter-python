# UTK = using tkinter



import tkinter as tk
import mysql.connector as p
from tkinter import messagebox as ms



#connecting mysql
a=p.connect(host='localhost' , user= 'root' , password='123456')
b=a.cursor()
b.execute("SHOW DATABASES LIKE %s", ('password',))
result = b.fetchone()
if result:
    b.execute("use password")
    a.commit()
else:
    # print(f"Database '{database_name}' does not exist.")
     b.execute("create database password;")
     b.execute("use password")
     b.execute("create table passwords(username varchar(20) , password varchar(20))")
     a.commit()



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


    #root.withdraw()
    rootl=tk.Toplevel()
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
    button_bool_username=False
    button_bool_password=False


    # def check_username(en):
    #     check_message()
    
    #     user_name = en.widget.get()
    #     b.execute("select * from passwords;")
    #     c=b.fetchall()
    #     for i in c:
    #         if (user_name == i[0] ):
    #             # check_message()
    #             button_bool_username=True
    #             en.widget.tk_focusNext().focus()
    #             l.append(user_name)
    #             break
    #     else:
    #         message_user()



    #def check_password(ep):
        # check_message()

        # p_word=ep.widget.get()
        # f="select password from passwords where username = %s"
        # b.execute(f,l)
        # c=b.fetchall()
        # for i in c:
        #     if (p_word == i[0]):
        #         check_message()
        #         button_bool_password=True
        #         ep.widget.tk_focusNext().focus()
        #         break
        # else:
        #     message_pass()




        # user_name = en.widget.get()
        # b.execute("select * from passwords;")
        # c=b.fetchall()
        # for i in c:
        #     if (user_name == i[0] ):
        #         global button_bool_username
        #         button_bool_username=True
        #         p_word=ep.get()
        #         if p_word=="":
        #             break
        #         else:
        #             if (p_word == i[1]):
        #                 global button_bool_password
        #                 button_bool_password=True
        #                 #ms.showinfo("Login" , "Login Successfull")

        #             else:
        #                 global button_bool_password
        #                 button_bool_password=False
        #                 message_pass()
        #                 #ms.showerror("Login Failed", "Incorrect username or password")
        #                 break
        #     else:
        #         global button_bool_username
        #         button_bool_username
        #         message_user()
        #         break
        
    


    def check(ens,eps=""):
        
        check_message()
        nonlocal button_bool_username
        nonlocal button_bool_password
        user_name = en.get()
        b.execute("select * from passwords;")
        c=b.fetchall()
        print(c)
        length_of_c=len(c)
        for i in range(length_of_c):
            if (user_name == c[i][0] ):
                # print(user_name)
                check_message()
                button_bool_username=True
                en.tk_focusNext().focus()
                p_word=ep.get()
                if p_word=="":
                    break
                else:
                    if (p_word == c[i][1]):
                        # print(p_word)
                        check_message()
                        button_bool_password=True
                        ep.tk_focusNext().focus()
                        #ms.showinfo("Login" , "Login Successfull")
                        break

                    else:
                        button_bool_password=False
                        message_pass()
                        #ms.showerror("Login Failed", "Incorrect username or password")
                        break
        else:
            button_bool_username=False
            # print(user_name)
            message_user()


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

    def toggle_button_clicked(position_argument):
        toggle_button.invoke()
    
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

        boole=False
        # user_name = en.get()
        # b.execute("select * from passwords;")
        # c=b.fetchall()
        # for i in c:
        #     if (user_name == i[0] ):
        #         p_word=ep.get()
        #         f="select password from passwords where username = %s"
        #         b.execute(f,i[0])
        #         q=b.fetchall()
        #         for j in q:
        #             if (p_word == j[0]):
        #                 # ms1=ms.showinfo("Login" , "Login Successfull")
        #                 boole=True

        #             else:
        #                 # ms.showerror("Login Failed", "Incorrect username or password")
        #                 boole=False
        #     else:
        #         #ms.showerror("Login Failed", "Incorrect username or password")
        #         boole=False

        us=en.get()
        ps=ep.get()
        check(us,ps)
        if button_bool_username == True and button_bool_password == True:
            ms.showinfo("Login" , "Login Successfull")
            rootl.destroy()
        else:
            ms.showerror("Login Failed", "Incorrect username or password")
            pass
    
    def toggle_password():
    # Check the current show value and toggle it
        if ep.cget('show') == '*':
            ep.config(show='')  # Show plain text
        else:
            ep.config(show='*')  # Mask text with '*'






    l1=tk.Label(rootl,  text='Username:' , font=("Arial" , 14))
    l1.place(x=160, y=165)
    l2=tk.Label(rootl, text='Password  :' , font=("Arial" , 14))
    l2.place(x=160 , y=190)





    en = tk.Entry(rootl)
    en.place( x=290,y=170)
    en.bind("<Return>" , check)
    ep = tk.Entry(rootl , show="*")
    ep.place( x=290 , y=200)
    ep.bind("<Return>" , lambda event: check(en,ep))




    toggle_button = tk.Button(rootl, text="👁", command=toggle_password)
    toggle_button.place(x=430 , y=198)
    toggle_button.bind("<Return>" ,toggle_button_clicked)
    button = tk.Button(rootl, text='Login', width=13, border=5  , command=login_successfull)
    button.place(x=230,y=250)
    button.bind("<Return>" ,button_clicked)



def signup():

    # problems :-
                #  1. agar enter nhi dba rahe to list append nhi ho rahi or fir agar confirm password me enter dba rahe hai to wo bol raha hai ki list index is out of range
                # 2. button clicked me sirf invoke rakho and command me sql queries chlao
                # 3. password and con_password don't match hone ke baad agar password change kar rahe hai or same password confirm password me daal rahe hai to wo fir bhi don't match dikha raha hai because we didn't use pop function
                # 4. login me bhi dikkat hai jab hum saari values tab tab karke daal rahe hai


    # root.destroy()
    roots = tk.Toplevel()  # Changed from tk.Tk()
    roots.title("SignUp Page")
    ws = 600
    hs = 500
    wss = roots.winfo_screenwidth()
    hss = roots.winfo_screenheight()
    xs = (wss/2) - (ws/2)
    ys = (hss/2) - (hs/2)
    roots.geometry('%dx%d+%d+%d' % (ws, hs, xs, ys))
    roots.resizable(False , False)

    listS=[]
    iu1=tk.Label(roots , text="Username Exists!!!!" , font=("Arial" , 14))
    ip1=tk.Label(roots , text="Password doesn't contain a special character!!!!" , font=("Arial" , 14))
    iup1=tk.Label(roots , text="Invalid Username or Password!!!!" , font=("Arial" , 14))
    icp1=tk.Label(roots , text="Password Don't match!!!!" , font=("Arial" , 14))

    def valid_username(enq):
        
        check_message1()
    
        user_name1 = en.get()
        b.execute("select username from passwords;")
        c=b.fetchall()
        # print(c)
        for i in c:
            if i[0]==user_name1:
                message_user1()
                return 0
        if (user_name1 != '' ):
            # check_message()
            if listS:
                listS.clear()
                listS.append(user_name1)
            else:
                listS.append(user_name1)
            en.tk_focusNext().focus()
        else:
            message_userpass1()
    
    def valid_password(epq):
        
        check_message1()
        
        password1=ep.get()
        if not any(char in password1 for char in '*@!#$%^&()+'):
            message_pass1()
        elif (password1 != ''):
            ep.tk_focusNext().focus()
            listS.append(password1)
        else:
            message_userpass1()
    
    def valid_confirm_password(ecpq):

        nonlocal listS        
        check_message1()
        if len(listS)!=2:
            valid_password(ep)
            if len(listS)!=2:
                return 0
        
        con_password=ecp.get()
        if(con_password == listS[1]):
            ecp.tk_focusNext().focus()
        else:
            print(listS)
            listS.pop() 
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
        if (iup1.winfo_exists()):
            # ip.destroy() This will remove the ip widget from the code for that particular run.
            iup1.place_forget()
    
    def message_user1():
        iu1.place(x=200 , y=300)
    
    def message_pass1():
        ip1.place(x=100 , y=300)

    def message_con_password():
        print(listS)
        icp1.place(x=200 , y=300)
    def message_userpass1():
        iup1.place(x=200 , y=300)
    
    def button_clicked1(positional_argument1):
        button.invoke()
    
    def toggle_password_clicked(position_argument):
        toggle_password_button.invoke()
    
    def toggle_confirm_password_clicked(position_argument):
        toggle_confirm_password_button.invoke()
    def signup_successfull():

        nonlocal listS
        valid_username(en)
        if len(listS) == 0:  # Username already exists case
            return
        valid_password(ep)
        valid_confirm_password(ecp)
        if len(listS)==2:
            f1='insert into passwords values(%s,%s)'
            # "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
            b.execute(f1,listS)
            a.commit()
            ms.showinfo("Success", "Account created successfully!")  # Add success message
            print('Record Inserted Successfully')
            roots.destroy()  # Close signup window after successful registration
            login()  # Open login window automatically
        else:
            print("Invalid Username or Password")
    
    def toggle_password():
    # Check the current show value and toggle it
        if ep.cget('show') == '*':
            ep.config(show='')  # Show plain text
        else:
            ep.config(show='*')  # Mask text with '*'
    
    def toggle_confirm_password():
    # Check the current show value and toggle it
        if ecp.cget('show') == '*':
            ecp.config(show='')  # Show plain text
        else:
            ecp.config(show='*')  # Mask text with '*'

    l1=tk.Label(roots , text="Username:" , font=("Arial" , 14))
    l1.place(x=166 , y=165)
    l2=tk.Label(roots , text= "Password:" , font=("Arial" , 14))
    l2.place(x=170 , y=190)
    l3=tk.Label(roots , text="Confirm Password:" , font=("Arial" , 14))
    l3.place(x=99 , y=215)



    en = tk.Entry(roots)
    en.place( x=290,y=170)
    en.bind("<Return>" , valid_username )
    ep = tk.Entry(roots , show="*")
    ep.place( x=290 , y=200)
    ep.bind("<Return>" , valid_password)
    ecp = tk.Entry(roots , show="*")
    ecp.place( x=290 , y=230)
    ecp.bind("<Return>" , valid_confirm_password)


    toggle_password_button = tk.Button(roots, text="👁", command=toggle_password)
    toggle_password_button.place(x=420 , y=195)
    toggle_password_button.bind("<Return>" ,toggle_password_clicked)
    toggle_confirm_password_button = tk.Button(roots, text="👁", command=toggle_confirm_password)
    toggle_confirm_password_button.place(x=420 , y=225)
    toggle_confirm_password_button.bind("<Return>" ,toggle_confirm_password_clicked)
    button = tk.Button(roots, text='SignUp', width=13, border=5  , command=signup_successfull)
    button.place(x=230,y=260)
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
