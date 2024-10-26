import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "user" and password == "password":
        login_successful(username)
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

def login_successful(username):
    success_window = tk.Toplevel(root)
    success_window.title("Success")
    success_window.geometry("300x100")
    
    success_label = tk.Label(success_window, text=f"Welcome, {username}!", font=("Helvetica", 14))
    success_label.pack(pady=20)
    
    ok_button = tk.Button(success_window, text="OK", command=success_window.destroy)
    ok_button.pack()

def toggle_password():
    # Check the current show value and toggle it
    if password_entry.cget('show') == '*':
        password_entry.config(show='')  # Show plain text
        toggle_button.config(text="Hide Password")
    else:
        password_entry.config(show='*')  # Mask text with '*'
        toggle_button.config(text="Show Password 👁")

def MainWindow():
    global root, username_entry, password_entry, toggle_button
    
    root = tk.Tk()
    root.title("Login Window")
    root.geometry("300x250")
    
    # Username label and entry
    username_label = tk.Label(root, text="Username")
    username_label.pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)
    
    # Password label and entry with `show` option
    password_label = tk.Label(root, text="Password")
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, show="*")  # Initially, mask input characters
    password_entry.pack(pady=5)
    
    # Toggle button to show/hide password
    toggle_button = tk.Button(root, text="Show Password", command=toggle_password)
    toggle_button.pack(pady=5)
    
    # Login button
    login_button = tk.Button(root, text="Login", command=login)
    login_button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    MainWindow()
