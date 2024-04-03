""" 
Main File for Hotel Hub
Authors: Aleksandra Kalas and Varchas Sharma
CCT211
"""
import tkinter as tk
from tkinter import messagebox
from bookingFrame import BookingWindow
from financialFrame import FinancialWindow
from stockInformationFrame import StockInformationWindow
from employeeInformation import EmployeeInformationWindow
from employeeScheduleFrame import EmployeeScheduleWindow
from homePageFrame import HomeWindow



class HotelHub(tk.Tk):
    """
    This is the login page the HotelHub application. 
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization function for the 
        """
        super().__init__(*args, **kwargs)
        self.title("HotelHub")
        self.geometry("1000x500")
        
        self.login_frame = tk.Frame(self)
        self.login_frame.pack(padx=10, pady=10)
        tk.Label(self.login_frame, text="LOGIN").grid(row=0, column=1)
        tk.Label(self.login_frame, text="Username:").grid(row=1, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=1, column=1)

        tk.Label(self.login_frame, text="Password:").grid(row=2, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=2, column=1)

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=3, columnspan=2)

        self.title("Hotel Management System")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomeWindow, BookingWindow):  # Add all frames
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        
    
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "manager" and password == "admin":
            messagebox.showinfo("Login Success", "Welcome, Manager!")
            # Make call for manager home page
            self.show_frame(HomeWindow)

        elif username == "employee" and password == "1234":
            messagebox.showinfo("Login Success", "Welcome, Employee!")
            # Make call for employee home page
            self.show_frame(HomeWindow)

        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

if __name__ == "__main__":
    app = HotelHub()
    app.mainloop()