# UTK = using tkinter



# name=input('Enter Your First Name:')
# print("Hint:My First Name")
# password=input('Enter password:')
# if password=="Gaurav":
#     if name=="Deepali":
#         print("Welcome Chintu Didi")
#     elif name=="Vivek":
#         print("Welcome Bhaiya")
#     elif name=="Sangita":
#         print("Welcome Mummy")
#     elif name=="Khyati":
#         print("Welcome Mola Didi")
#     else:
#         print("Welcome",name)
# else:
#     print("Wrong password, Aap mera naam nahi jaante?")


import tkinter as tk
import mysql.connector as p





#connecting mysql
a=p.connect(host='localhost' , user= 'root' , password='123456' , database="password")
b=a.cursor()



l=[]



#making window
root = tk.Tk()

root.title('Password')

w = 600
h = 500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.resizable(False , False)



iu=tk.Label(root , text="Invalid Username!!!!" , font=("Arial" , 14))
ip=tk.Label(root , text="Wrong Password!!!!" , font=("Arial" , 14))

# def clear():
#     for f in root.winfo_children():
#         f.destroy()



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




l1=tk.Label(root,  text='Username:' , font=("Arial" , 14))
l1.place(x=160, y=165)
l2=tk.Label(root, text='Password  :' , font=("Arial" , 14))
l2.place(x=160 , y=190)





en = tk.Entry(root)
en.place( x=290,y=170)
en.bind("<Return>" , check_username )
ep = tk.Entry(root)
ep.place( x=290 , y=200)
ep.bind("<Return>" , check_password)






button = tk.Button(root, text='Stop', width=13, border=5  , command=root.destroy)
button.place(x=230,y=250)






root.mainloop()
