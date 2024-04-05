""" 
Main File for Hotel Hub
Authors: Aleksandra Kalas and Varchas Sharma
CCT211
"""
import tkinter as tk
from tkinter import messagebox
from homePageFrame import HomeWindow, BookingWindow, FinancialWindow, \
    StockInformationWindow, EmployeeInformationWindow, EmployeeScheduleWindow, \
        FoodStockWindow, RoomSetUpWindow, ToiletriesStockWindow, EmployeeHomeWindow
    

class LoginWindow(tk.Frame):
        """
        """
        def __init__(self, parent, controller) -> None:
            """
            """
            super().__init__(parent)
            self.controller = controller
            tk.Label(self, text="Login Window").pack(pady=10,padx=10)
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
                self.controller.show_frame(EmployeeHomeWindow)

            else:
                messagebox.showerror("Login Failed", "Invalid credentials.\
                                      Please try again.")  

class HotelHub(tk.Tk):
    """
    The application HotelHub.

    In this application, managers and employees will be able to access varying 
    functionalities.

    Managers: will have access to all functionalities - Booking Window, Financial Window
            Stock Information Window (Food Stock, Toiletries Stock, Room Set Up), 
            Employee Information Window, and Employee Schedule Window 
    Employees: will have acces to the following functionalities - Booking Window,
            Stock Information Window (Food Stock, Toiletries Stock, Room Set Up), and 
            Employee Schedule Window
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization function for the HotelHub application.

        Creation of all frames to swap through - starting with the Login Window. 
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
                    RoomSetUpWindow, EmployeeHomeWindow ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(LoginWindow)

        
    def show_frame(self, page_name):
        """
        Function to display the page which is given to the users screen. 
        """
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = HotelHub()
    app.mainloop()