import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import mysql.connector as mysql
from tkinter import messagebox as ms
import sys
import os
import traceback



# Add error logging
def log_error(error):
    with open('error_log.txt', 'a') as f:
        f.write(f"Error: {str(error)}\n")
        f.write(traceback.format_exc())

try:
    def init_db():
        try:
            conn = mysql.connect(
                host='localhost',
                user='root',
                password="123456",
                database='password'
            )
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS passwords
                     (username VARCHAR(255) PRIMARY KEY, password VARCHAR(255))''')
            conn.commit()
            return conn, c
        except mysql.Error as e:
            log_error(e)
            ms.showerror("Error", f"MySQL Error: {str(e)}")
            return None, None
    a = init_db()[0]
    b = init_db()[1]

    def MainWindow():
        custom_font = font.Font(family="Helvetica", size=20, weight="bold", slant="italic")
        custom_font2 = font.Font(family="Helvetica", size=10, weight="bold", slant="italic")

        l3=tk.Label(root , text="HELLO!! Welcome to my first Project" , font=custom_font)
        l3.place(x=80 , y=100)
        l4=tk.Label(root , text="Choose One" , font=custom_font)
        l4.place(x=210 , y=160)

        loginbutton=tk.Button(root , text="Login" , padx=10, pady=10, borderwidth=5, relief="raised" , command=login , fg="#aa5151" , font= custom_font2)
        loginbutton.place(x=210 , y=250)
        signupbutton=tk.Button(root , text="Signup", padx=10, pady=10, borderwidth=5 , relief="raised", command=signup , fg="#aa5151" , font=custom_font2)
        signupbutton.place(x=300,y=250)

    def login():
        rootl=tk.Toplevel()
        rootl.title("Login Page")
        wl = 600
        hl = 500
        wsl = rootl.winfo_screenwidth()
        hsl = rootl.winfo_screenheight()
        xl = (wsl/2) - (wl/2)
        yl = (hsl/2) - (hl/2)
        rootl.geometry('%dx%d+%d+%d' % (wl, hl, xl, yl))

        l=[]
        iu=tk.Label(rootl , text="Invalid Username!!!!" , font=("Arial" , 14))
        ip=tk.Label(rootl , text="Wrong Password!!!!" , font=("Arial" , 14))
        button_bool_username=False
        button_bool_password=False

        def check(ens,eps=""):
            check_message()
            nonlocal button_bool_username
            nonlocal button_bool_password
            user_name = en.get()

            b.execute("SELECT password FROM passwords WHERE username=%s", (user_name,))

            result = b.fetchone()
            
            if result:
                button_bool_username = True
                check_message()
                en.tk_focusNext().focus()
                p_word = ep.get()
                
                if p_word == "":
                    return
                elif p_word == result[0]:
                    check_message()
                    button_bool_password = True
                    ep.tk_focusNext().focus()
                else:
                    button_bool_password = False
                    message_pass()
            else:
                button_bool_username = False
                message_user()

        def message_user():
            iu.place(x=200 , y=280)

        def message_pass():
            ip.place(x=200 , y=280)

        def check_message(): 
            if (iu.winfo_exists()):
                iu.place_forget()
            if (ip.winfo_exists()):
                ip.place_forget()

        def button_clicked(position_argument):
            button.invoke()

        def toggle_button_clicked(position_argument):
            toggle_button.invoke()
        
        def login_successfull():
            us=en.get()
            ps=ep.get()
            check(us,ps)
            if button_bool_username == True and button_bool_password == True:
                ms.showinfo("Login" , "Login Successfull")
                rootl.destroy()
            else:
                ms.showerror("Login Failed", "Incorrect username or password")
        
        def toggle_password():
            if ep.cget('show') == '*':
                ep.config(show='')
            else:
                ep.config(show='*')

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
        roots = tk.Toplevel()
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
            for i in c:
                if i[0]==user_name1:
                    message_user1()
                    return 0
            if (user_name1 != '' ):
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
                iu1.place_forget()
            if (ip1.winfo_exists()):
                ip1.place_forget()
            if (icp1.winfo_exists()):
                icp1.place_forget()
            if (iup1.winfo_exists()):
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
            if len(listS) == 0:
                return
            valid_password(ep)
            valid_confirm_password(ecp)
            if len(listS)==2:
                f1='INSERT INTO passwords (username, password) VALUES (%s, %s)'
                b.execute(f1, listS)
                a.commit()
                ms.showinfo("Success", "Account created successfully!")
                print('Record Inserted Successfully')
                roots.destroy()
                login()
            else:
                print("Invalid Username or Password")
        
        def toggle_password():
            if ep.cget('show') == '*':
                ep.config(show='')
            else:
                ep.config(show='*')
        
        def toggle_confirm_password():
            if ecp.cget('show') == '*':
                ecp.config(show='')
            else:
                ecp.config(show='*')

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

    root = tk.Tk()
    root.title('Welcome')
    w = 600
    h = 500
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    bg_image = Image.open("D:\Gaurav\Tkinter-python\g_image.png")  # Replace with your image path
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    root.config(background="#fff")
    root.resizable(False , False)

    MainWindow()
    root.mainloop()
except Exception as e:
    log_error(e)
    ms.showerror("Error", f"Startup Error: {str(e)}")