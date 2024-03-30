""" 
Main File for Hotel Hub
Authors: Aleksandra Kalas and Varchas Sharma
CCT211
"""
import tkinter as tk
from tkinter import messagebox

class HotelHub:
    """
    This is the login page the HotelHub application. 
    """
    def __init__(self, root) -> None:
        """
        Initialization function for the 
        """
        self.root = root
        self.root.title("HotelHub")
        
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, columnspan=2)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "manager" and password == "admin":
            messagebox.showinfo("Login Success", "Welcome, Manager!")
            # Make call for manager home page

        elif username == "employee" and password == "1234":
            messagebox.showinfo("Login Success", "Welcome, Employee!")
            # Make call for employee home page

        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    hotelHub = HotelHub(root)
    root.mainloop()