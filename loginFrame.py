""" 
Main File for Hotel Hub
Authors: Aleksandra Kalas and Varchas Sharma
CCT211
"""
import tkinter as tk
from tkinter import messagebox
from homePageFrame import HomeWindow, BookingWindow, FinancialWindow, \
    StockInformationWindow, EmployeeInformationWindow, EmployeeScheduleWindow, \
        FoodStockWindow, RoomSetUpWindow, ToiletriesStockWindow
    

class LoginWindow(tk.Frame):
        """
        """
        def __init__(self, parent, controller) -> None:
            """
            """
            super().__init__(parent)
            self.controller = controller
            tk.Label(self, text="Login Window").pack(pady=10,padx=10)
            # tk.Button(self, text="Home", command=lambda: controller.show_frame(HomeWindow)).pack()
            tk.Label(self, text="LOGIN").pack(pady=10,padx=10)
            tk.Label(self, text="Username:").pack()
            self.username_entry = tk.Entry(self)
            self.username_entry.pack()

            tk.Label(self, text="Password:").pack()
            self.password_entry = tk.Entry(self, show="*")
            self.password_entry.pack()
           
            tk.Button(self, text="Login", command=self.login).pack()
        
        def login(self):
            username = self.username_entry.get()
            password = self.password_entry.get()
        
            if username == "manager" and password == "admin":
                messagebox.showinfo("Login Success", "Welcome, Manager!")
                # Make call for manager home page
                #self.show_frame(HomeWindow)
                self.controller.show_frame(HomeWindow)

            elif username == "employee" and password == "1234":
                messagebox.showinfo("Login Success", "Welcome, Employee!")
                # Make call for employee home page
                self.controller.show_frame(HomeWindow)

            else:
                messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")  

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
        self.frames = {}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        for F in (HomeWindow, BookingWindow, LoginWindow, FinancialWindow, 
                  StockInformationWindow, EmployeeInformationWindow, 
                  EmployeeScheduleWindow, FoodStockWindow, ToiletriesStockWindow,
                    RoomSetUpWindow ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(LoginWindow)
        #tk.Button(self, text="Login", command=self.show_frame(LoginWindow)).pack()
        """tk.Label(self, text="LOGIN").pack(pady=10,padx=10)
        tk.Label(self, text="Username:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()"""

        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = HotelHub()
    app.mainloop()