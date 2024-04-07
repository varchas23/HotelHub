"""
Main File for Hotel Hub
Authors: Aleksandra Kalas and Varchas Sharma
CCT211

"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sqlite3, matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from managementdb import GuestDatabase, EmployeeDatabase,StockDatabase, \
    RoomSetupDatabase, ToiletriesStockDatabase, FoodStockDatabase, EmployeeSchedule
from tkinter import messagebox

class LoginWindow(tk.Frame):
        """
        Creates the login window. All users will be able to see this login window
        and use the following login in order to gain access to the HotelHub application.

        Managers login is: 
            username: manager
            password: admin

            Employee login is:
            username: employee
            password: 1234
        """
        def __init__(self, parent, controller) -> None:
            """
            Initializer for the Login Window. This initializer creates the look
            of the frame with all the entries and labels. 
            """
            super().__init__(parent)
            
            self.configure(background="#d2f7df")
            self.controller = controller
            tk.Label(self, text="Hotel Hub", font=(('EuphemiaUCAS 40 bold italic')), 
                     background="#d2f7df").pack()
            #tk.Label(self, text="Login Window").pack(pady=10,padx=10)
            tk.Label(self, text="LOGIN", font=('EuphemiaUCAS 30 bold italic'), 
                     background="#d2f7df").pack(pady=10,padx=10)
            tk.Label(self, text="Username:",font=('EuphemiaUCAS 20 bold italic'), 
                     background="#d2f7df").pack()
            self.username_entry = tk.Entry(self)
            self.username_entry.pack()

            tk.Label(self, text="Password:", font=('EuphemiaUCAS 20 bold italic'),
                     background="#d2f7df").pack()
            self.password_entry = tk.Entry(self, show="*")
            self.password_entry.pack()
           
            tk.Button(self, text="Login", command=self.login).pack(pady=10)
        
        def login(self):
            """
            Controls whether the user will gain access to the system. 
            
            Managers login is: 
            username: manager
            password: admin

            Employee login is:
            username: employee
            password: 1234
            """
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
        self.geometry("1000x600")
        self.frames = {}
        self.configure(background="light green")
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

class HomeWindow(tk.Frame):
    """
    Creates the main home window for HotelHub. From this window, users can access all
    other windows by selecting the corresponding button. 
    
    This page is used as a central navigation page for the user. It should be 
    accessible from each page that the user is on. 
    """
    def __init__(self, parent, controller):
        """ 
        Initializer for the Home Window. This initializer creates the look
        of the frame with all the entries and labels. 

        All buttons will lead the user to a new page. 
        """
        super().__init__(parent)
        tk.Label(self, text="Home Page", font=('EuphemiaUCAS 40 bold italic')).grid(row=0,column=2)

        tk.Button(self, text="Finances of Hotel", font=('EuphemiaUCAS 30 bold italic'),
                   pady=50, command=lambda: 
                   controller.show_frame(FinancialWindow)).grid(row=3, column=0)
        tk.Button(self, text="Book a Room", font=('EuphemiaUCAS 30 bold italic'),
                   pady=50, command=lambda: 
                   controller.show_frame(BookingWindow)).grid(row=5, column=0)
        tk.Button(self, text="Stock Information", font=('EuphemiaUCAS 30 bold italic'),
                   pady=50, command=lambda: 
                   controller.show_frame(StockInformationWindow)).grid(row=3, column=3)
        tk.Button(self, text="Employee Information", font=('EuphemiaUCAS 30 bold italic'), 
                  pady=50, command=lambda: 
                  controller.show_frame(EmployeeInformationWindow)).grid(row=5, column=3)
        tk.Button(self, text="Employee Schedule", font=('EuphemiaUCAS 30 bold italic'),
                  pady=50, command=lambda: 
                  controller.show_frame(EmployeeScheduleWindow)).grid(row=8, column=2)
        tk.Button(self,text="Logout", font=('EuphemiaUCAS 30 bold italic'),
                  command=lambda: 
                  controller.show_frame(LoginWindow)).grid(row=9, column=2)
        
class EmployeeHomeWindow(tk.Frame):
    """
    Creates the employee home window for HotelHub. From this window, employees can 
    access selective windows by selecting the corresponding button. 
    
    This page is used as a central navigation page for the user. It should be 
    accessible from each page that the user is on. 
    """
    def __init__(self, parent, controller):
        """ 
        Initializer for the Employee Home Window. This initializer creates the look
        of the frame with all the entries and labels. 

        All buttons will lead the user to a new page. 
        """
        super().__init__(parent)
        tk.Label(self, text="Home Page").pack(pady=10, padx=10)

        tk.Button(self, text="Book a Room", font=('EuphemiaUCAS 40 bold italic'), 
                  command=lambda: controller.show_frame(BookingWindow)).pack()
        tk.Button(self, text="Stock Information", font=('EuphemiaUCAS 30 bold italic'), 
                  command=lambda: controller.show_frame(StockInformationWindow)).pack()
        tk.Button(self, text="Employee Schedule", font=('EuphemiaUCAS 30 bold italic'), 
                  command=lambda: controller.show_frame(EmployeeScheduleWindow)).pack()
        tk.Button(self,text="Logout", font=('EuphemiaUCAS 30 bold italic'),
                  command=lambda: 
                  controller.show_frame(LoginWindow)).pack()

class BookingWindow(tk.Frame):
    """
    Creates the main booking window for HotelHub. From this window, the manager
    and the employees should be able to create a room booking for a customer which
    will then be saved within the database of customers.
    """
    def __init__(self, parent, controller) -> None:
        """
        Initializer for the Booking Window. This initializer creates the look
        of the frame with all the entries and labels. 

        The information entered into each entry box will be used to create a 
        new entry into the guest database
        """
        super().__init__(parent)

        self.connect()

        # Entries and Labels for Entering Information to Book a Room for a Guest
        tk.Label(self, text="Booking Window", 
                 font=('EuphemiaUCAS 40 bold italic')).grid(row=0)


        # Guest id
        tk.Label(self, text="Guest Id", 
                 font=('EuphemiaUCAS 20 bold italic')).grid(row=1, column=0)
        id_entry = tk.Entry(self)
        id_entry.grid(row=1,column=1)
        
        # Name
        tk.Label(self, text="Guest Name", 
                 font=('EuphemiaUCAS 20 bold italic')).grid(row=2, column=0)
        name_entry = tk.Entry(self)
        name_entry.grid(row=2,column=1)

        # Address
        tk.Label(self, text="Address", 
                 font=('EuphemiaUCAS 20 bold italic')).grid(row=3, column=0)
        address_entry = tk.Entry(self)
        address_entry.grid(row=3,column=1)

        #Credit Card Information
        tk.Label(self, text="Credit Card #", 
                 font=('EuphemiaUCAS 20 bold italic')).grid(row=4, column=0)
        credit_card_entry = tk.Entry(self)
        credit_card_entry.grid(row=4,column=1)

        # Number of guests staying
        tk.Label(self, text="Guest Number", 
                 font=('EuphemiaUCAS 20 bold italic')).grid(row=5, column=0)
        num_guests_entry = tk.Entry(self)
        num_guests_entry.grid(row=5,column=1)

        # Room number
        tk.Label(self, text="Room Number", 
                 font=('EuphemiaUCAS 20 bold italic')).grid(row=6, column=0)
        room_num_entry = tk.Entry(self)
        room_num_entry.grid(row=6,column=1)

        # Bed Selection
        tk.Label(self, text="Bed Selection", 
                 font=('EuphemiaUCAS 20 bold italic')).grid(row=7, column=0)
        bed_entry = tk.Entry(self)
        bed_entry.grid(row=7,column=1)

        #Duration of Stay
        tk.Label(self, text="Check-in", 
                 font=('EuphemiaUCAS 20 bold italic')).grid(row=8, column=0)
        checkin_entry = tk.Entry(self)
        checkin_entry.grid(row=8,column=1)
        tk.Label(self, text="Check-out", 
                 font=('EuphemiaUCAS 20 bold italic')).grid(row=9, column=0)
        checkout_entry = tk.Entry(self)
        checkout_entry.grid(row=9,column=1)


        # Additional Accomodations
        tk.Label(self, text="Other Accomodations", 
                 font=('EuphemiaUCAS 20 bold italic')).grid(row=10, column=0)
        accomodations_entry = tk.Entry(self)
        accomodations_entry.grid(row=10,column=1)

        tk.Button(self, text="Complete Booking", 
                  font=('EuphemiaUCAS 20 bold italic'), command=lambda: self.add_guest(
            id_entry.get(), name_entry.get(), address_entry.get(),credit_card_entry.get(),
            num_guests_entry.get(), room_num_entry.get(), bed_entry.get(), 
            checkin_entry.get(), checkout_entry.get(), accomodations_entry.get())
            ).grid(row=6, column=8)

        # Return to Home Page
        tk.Button(self, text="Home", font=('EuphemiaUCAS 20 bold italic') ,
                  command=lambda: 
                  controller.show_frame(HomeWindow)).grid(row=0, column=18)
        
        tk.Button(self,text="Logout", font=('EuphemiaUCAS 30 bold italic'),
                  command=lambda: 
                  controller.show_frame(LoginWindow)).grid(row=15, column=5)
    
    def connect(self):
        """
        Create and connect the GuestDatabase
        """
        db = GuestDatabase()
        
        #managementdb.condb()
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        con1.close()
    
    def add_guest(self, id, name, address, creditcard, numguests, roomnum, 
               bedselet, checkin, checkout, requests):
        """
        Intake for booking information - this information coming from the entries on 
        the booking window will be added to the database for access.
        """
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        cur1.execute("SELECT * FROM Guests WHERE GuestID=?", (id,))
        entry = cur1.fetchone()

        if not entry:
            cur1.execute("INSERT INTO Guests ('GuestID', 'Name', 'Address', \
                             'CreditCardInfo', 'NumberOfGuests', 'RoomNumber', \
                             'BedSelection', 'CheckInDate', 'CheckOutDate', \
                             'SpecialRequests') VALUES (?, ?, ?, ?, ?, \
                             ?, ?, ?, ?, ?)", (id, name, address, creditcard, numguests, 
                                         roomnum, bedselet, checkin, checkout, requests))
        con1.commit()
    

class FinancialWindow(tk.Frame):
    """
    Creates the financial window for HotelHub. From this window, the manager
    and will be able to view the amount of money the hotel is making through
    a line.
    """
    def __init__(self, parent, controller) -> None:
        """
        Initalizer where data gets extracted for use in the line graphs
        """
        super().__init__(parent)
        # Entries and Labels for Financial Window with Home button
        tk.Label(self, text="Financial Window", 
                 font=('EuphemiaUCAS 40 bold italic')).pack(pady=10,padx=10)
        tk.Button(self, text="Home", font=('EuphemiaUCAS 20 bold italic'),
                  command=lambda: controller.show_frame(HomeWindow)).pack()
        
        # Calls self.connect() to create stock table
        self.connect()
        # Connects to database and implements cursor
        self.con = sqlite3.connect("managementdb.db")
        self.cur = self.con.cursor()

        # Initializes variables
        self.monthsGuests, self.numGuests, self.months_income = [], [], []
        self.income, self.months_expenditure, self.expenditure = [], [], []

        # Executes SQL command to extract data from Guests table
        self.cur.execute("SELECT strftime('%m', CheckInDate) AS Month, \
                         SUM(NumberOfGuests) AS GuestsNumber FROM Guests \
                         GROUP BY strftime('%m', CheckInDate);")
        # Stores data in variable
        incomingGuests = self.cur.fetchall()
        # Splits data in two variables
        for tup in incomingGuests:
            self.monthsGuests.append(int(tup[0]))
            self.numGuests.append(tup[1])

        # Executes SQL command to extract data from Guests table
        self.cur.execute("SELECT strftime('%m', CheckInDate) AS Month, \
                         SUM(NumberOfGuests * 80) AS Income FROM Guests \
                         GROUP BY strftime('%m', CheckInDate);")
        # Stores data in variable
        income_data = self.cur.fetchall()
        # Splits data in two variables
        for tup in income_data:
            self.months_income.append(int(tup[0]))
            self.income.append(tup[1])

        # Executres SQL command to extract data from Stock table
        self.cur.execute("SELECT strftime('%m', PurchaseDate) AS Month, \
                         SUM(Toiletries + Food + RoomSetUp) AS Expenditure FROM Stock \
                         GROUP BY strftime('%m', PurchaseDate);")
        # Stores data in variable
        expenditure_data = self.cur.fetchall()
        # Splits data in two variables
        for tup in expenditure_data:
            self.months_expenditure.append(int(tup[0]))
            self.expenditure.append(tup[1])

        # Closes connection to database
        self.con.close()
        
        # Calls plotGraph method
        self.plotGraph()

        # Logout button
        tk.Button(self,text="Logout", font=('EuphemiaUCAS 30 bold italic'),
                  command=lambda: 
                  controller.show_frame(LoginWindow)).pack()

    def connect(self):
        """
        Create the Stock table in the management database
        """
        db = StockDatabase()

        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        con1.close()
    
    def displayGraph(self, fig1, fig2, fig3):
        """
        Display the graphs for the financial window.
        """
        # Creates frames for each canvas
        frame1 = tk.Frame(self)
        frame1.pack(side="top", fill="both", expand=True)
        frame2 = tk.Frame(self)
        frame2.pack(side="top", fill="both", expand=True)
        frame3 = tk.Frame(self)
        frame3.pack(side="top", fill="both", expand=True)

        # Packs canvas into frames
        canvasGuests = FigureCanvasTkAgg(fig1, master=frame1)
        canvasGuests.draw()
        canvasGuests.get_tk_widget().pack(side="left", fill="both", expand=True)

        canvasIncome = FigureCanvasTkAgg(fig2, master=frame2)
        canvasIncome.draw()
        canvasIncome.get_tk_widget().pack(side="left", fill="both", expand=True)

        canvasExpenditure = FigureCanvasTkAgg(fig3, master=frame3)
        canvasExpenditure.draw()
        canvasExpenditure.get_tk_widget().pack(side="left", fill="both", expand=True)
    
    def plotGraph(self):
        """
        Plot graphs for the financial page. 
        """
        # Creates line graph visualization of incoming guests over a year
        fig1 = plt.figure(figsize=(3, 3))
        plt.plot(self.monthsGuests, self.numGuests, marker='o', color='blue')
        plt.title('View of Incoming Guests Over a Year')
        plt.xlabel('Month')
        plt.ylabel('Number of Guests')
        plt.grid(True)
        plt.xticks(range(1, 13))
        plt.tight_layout()

        # Creates line graph visualization of income created each month
        fig2 = plt.figure(figsize=(3, 3))
        plt.plot(self.months_income, self.income, marker='o', color='green')
        plt.title('View of Income Made Each Month')
        plt.xlabel('Month')
        plt.ylabel('Income ($)')
        plt.grid(True)
        plt.xticks(range(1, 13))
        plt.tight_layout()

        # Creates line graph visualization of purchases for stock each month
        fig3 = plt.figure(figsize=(3, 3))
        plt.plot(self.months_expenditure, self.expenditure, marker='o', color='red')
        plt.title('Money Spent on Purchases for Stock Each Month')
        plt.xlabel('Month')
        plt.ylabel('Expenditure ($)')
        plt.grid(True)
        plt.xticks(range(1, 13))
        plt.tight_layout()

        # Calls displayGraph method
        self.displayGraph(fig1, fig2, fig3)
        

class ToiletriesStockWindow(tk.Frame):
    """
    Creates the toiletries stock information window for HotelHub. From this window, 
    the manager and employees will be able to view the toiletry stock levels of the public
    washrooms, hotel rooms, maids room and staff room of the hotel.

    If a level needs to be restocked then the label for the level will turn red to
    indicate that there is restock required. 
    """
    def __init__(self, parent, controller) -> None:
        """
        Initializer for the toiletries stock window. This initializer creates the look
        of the frame with all the entries and labels. 

        Displays the stock using a table and gets the information from the management
        database.
        """
        super().__init__(parent)
        tk.Label(self, text="Toiletries Stock", 
                 font=('EuphemiaUCAS 40 bold italic')).pack()
        
        self.connect()

        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4","c5" ), 
                                 show='headings')
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="Hotel Level")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Public Washrooms")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="Hotel Rooms")
        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="Maids Room")
        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5", text="Staff Room")
        self.tree.pack()
        self.add_data()
        tk.Button(self, text="Home", font=('EuphemiaUCAS 20 bold italic'),
                  command=lambda: 
                  controller.show_frame(HomeWindow)).pack(side="top", expand=True)
        tk.Button(self, text="Go Back",font=('EuphemiaUCAS 20 bold italic'),
                  command=lambda: 
                  controller.show_frame(StockInformationWindow)).pack(side="top", 
                                                                      expand=True)
        tk.Button(self,text="Logout", font=('EuphemiaUCAS 30 bold italic'),
                  command=lambda: 
                  controller.show_frame(LoginWindow)).pack()
    
    def connect(self):
        """
        Create the Toiletries stock table in the management database
        """
        db = ToiletriesStockDatabase()
        
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        con1.close()
    
    def add_data(self):
        """
        Select all items from Employee table and display them in the table
        """
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        cur1.execute("SELECT * FROM ToiletriesStock")
        rows = cur1.fetchall()    
        for row in rows:
            print(row) 
            self.tree.insert("", tk.END, values=row)           
        con1.close()

class FoodStockWindow(tk.Frame):
    """
    Creates the food stock information window for HotelHub. From this window, 
    the manager and employees will be able to view the food stock levels of the 
    restaurant breakfast, restaurant lunch, restaurant dinner, and mini fridge snacks

    If a level needs to be restocked then the label for the level will turn red to
    indicate that there is restock required. 
    """
    def __init__(self, parent, controller) -> None:
        """
        Initializer for the food stock window. This initializer creates the look
        of the frame with all the entries and labels. 

        Displays the stock using a table and gets the information from the management
        database.
        """
        super().__init__(parent)
        tk.Label(self, text="Food Stock", font=('EuphemiaUCAS 40 bold italic')).pack()
        
        self.connect()
        
        # Setting up table for information about food stock database
        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4","c5" ), 
                                 show='headings')
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="Hotel Level")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Restaurant Breakfast Food")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="Restaurant Lunch Food")
        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="Restaurant Dinner Food")
        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5", text="Mini Fridge Snacks")
        self.tree.pack()

        tk.Button(self, text="Home", font=('EuphemiaUCAS 20 bold italic'),
                  command=lambda: controller.show_frame(HomeWindow)).pack(side="top", 
                                                                          expand=True)
        tk.Button(self, text="Go Back",font=('EuphemiaUCAS 20 bold italic'),
                  command=lambda: 
                  controller.show_frame(StockInformationWindow)).pack(side="top",
                                                                       expand=True)
        tk.Button(self,text="Logout", font=('EuphemiaUCAS 30 bold italic'),
                  command=lambda: 
                  controller.show_frame(LoginWindow)).pack()
        
        self.add_data()

    def connect(self):
        """
        Create the Food stock table in the management database
        """
        db = FoodStockDatabase()
        
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        con1.close()
    
    def add_data(self):
        """
        Select all items from Employee table and display them in the table
        """
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        cur1.execute("SELECT * FROM FoodStock")
        rows = cur1.fetchall()    
        for row in rows:
            print(row) 
            self.tree.insert("", tk.END, values=row)           
        con1.close()

class RoomSetUpWindow(tk.Frame):
    """
    Creates the room set up information window for HotelHub. From this window, 
    the manager and employees will be able to view the rooms which need to be setup on
    various levels such as bedding, washrooms, carpet cleaning, and staff room cleaning.

    If a level needs to be restocked then the label for the level will turn red to
    indicate that there is restock required. 
    """
    def __init__(self, parent, controller) -> None:
        """
        Initializer for the room set up window. This initializer creates the look
        of the frame with all the entries and labels. 

        Displays the room set up using a table and gets the information from the management
        database.
        """
        super().__init__(parent)
        tk.Label(self, text="Room Set Up", font=('EuphemiaUCAS 40 bold italic')).pack()
        tk.Button(self, text="Home", font=('EuphemiaUCAS 20 bold italic'),
                  command=lambda: controller.show_frame(HomeWindow)).pack()
        
        self.connect()

        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4","c5" ),
                                  show='headings')
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="Hotel Level")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Bedding")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="Washroom")
        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="Carpet Clean")
        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5", text="Staff Room")
        self.tree.pack()
        self.add_data()

        tk.Button(self, text="Home", font=('EuphemiaUCAS 20 bold italic'),
                  command=lambda: 
                  controller.show_frame(HomeWindow)).pack(side="top", expand=True)
        tk.Button(self, text="Go Back",font=('EuphemiaUCAS 20 bold italic'),
                  command=lambda: 
                  controller.show_frame(StockInformationWindow)).pack(side="top",
                                                                       expand=True)
        tk.Button(self,text="Logout", font=('EuphemiaUCAS 30 bold italic'),
                  command=lambda: 
                  controller.show_frame(LoginWindow)).pack()
    
    def connect(self):
        """
        Create the Room setup table in the management database
        """
        db = RoomSetupDatabase()
        
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        con1.close()
    
    def add_data(self):
        """
        Select all items from Employee table and display them in the table
        """
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        cur1.execute("SELECT * FROM RoomSetup")
        rows = cur1.fetchall()    
        for row in rows:
            print(row) 
            self.tree.insert("", tk.END, values=row)           
        con1.close()


class StockInformationWindow(tk.Frame):
    """
    Creates the stock information window for HotelHub. 

    From this window, managers will be able to select which stock information they
    would like to view. There are buttons to view each stock: toiletries, food, and rooms
    which require set up.  
    """

    def __init__(self, parent, controller) -> None:
        """
        Initializer for the general stock window. This initializer creates the look
        of the frame with all the entries and labels. 

        Displays buttons which lead to other stock pages. 
        """
        super().__init__(parent)
        tk.Label(self, text="Stock Information", font=('EuphemiaUCAS 40 bold italic')).pack()
        
        # Buttons to lead to other frames for each stock 
        tk.Button(self, text="Toiletries Stock", font=('EuphemiaUCAS 20 bold italic'), 
                  command=lambda:
                   controller.show_frame(ToiletriesStockWindow)).pack()
        tk.Button(self, text="Food Stock", font=('EuphemiaUCAS 20 bold italic'), command=lambda: 
                  controller.show_frame(FoodStockWindow)).pack() 
        tk.Button(self, text="Room Set Up", font=('EuphemiaUCAS 20 bold italic'), 
                  command=lambda: 
                  controller.show_frame(RoomSetUpWindow)).pack()
        
        tk.Button(self, text="Main Menu", font=('EuphemiaUCAS 20 bold italic'), command=lambda: 
                  controller.show_frame(HomeWindow)).pack()
        tk.Button(self,text="Logout", font=('EuphemiaUCAS 30 bold italic'),
                  command=lambda: 
                  controller.show_frame(LoginWindow)).pack()


class EmployeeScheduleWindow(tk.Frame):
    """
    Creates the window for the Employee Schedule. From this page, employees will be able
    to view what employee is placed on the schedule for which day of the week. 

    Employee names will be displayed in a table under the respective day they will be 
    working for that week.
    """
    def __init__(self, parent, controller) -> None:
        """
        Initializer for the employee schedule window. This initializer creates the look
        of the frame with all the entries and labels. 

        Displays the employee scheduel using a table and gets the information from the 
        management database.
        """
        super().__init__(parent)
        tk.Label(self, text="Employee Schedule", 
                 font=('EuphemiaUCAS 40 bold italic')).pack(pady=10,padx=10)
        tk.Button(self, text="Home", font=('EuphemiaUCAS 20 bold italic'), command=lambda:
                  controller.show_frame(HomeWindow)).pack()
        
        self.connect()

        # Creating the table employee information to display
        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5", 
                                               "c6", "c7"), show='headings')
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="Sunday")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Monday")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="Tuesday")
        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="Wednesday")
        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5", text="Thursday")
        self.tree.column("#6", anchor=tk.CENTER)
        self.tree.heading("#6", text="Friday")
        self.tree.column("#7", anchor=tk.CENTER)
        self.tree.heading("#7", text="Saturday")
        self.tree.pack()
        self.getData()
        tk.Button(self,text="Logout", font=('EuphemiaUCAS 30 bold italic'),
                  command=lambda: 
                  controller.show_frame(LoginWindow)).pack()

    def connect(self):
        """
        Create the Employee schedule table in the management database
        """
        db = EmployeeSchedule()
        
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        con1.close()

    def getData(self):
        """
        """
        self.con1 = sqlite3.connect("managementdb.db")
        self.cur1 = self.con1.cursor()
        self.cur1.execute("SELECT Name FROM EmployeeSchedule ORDER BY CASE \
                    WHEN WorkDay = 'Sunday' THEN 1 \
                    WHEN WorkDay = 'Monday' THEN 2 \
                    WHEN WorkDay = 'Tuesday' THEN 3 \
                    WHEN WorkDay = 'Wednesday' THEN 4 \
                    WHEN WorkDay = 'Thursday' THEN 5 \
                    WHEN WorkDay = 'Friday' THEN 6 \
                    WHEN WorkDay = 'Saturday' THEN 7 \
                    ELSE 8 END;")
        rows = self.cur1.fetchall()
        for row in rows:
            print(row) 
            self.tree.insert("", tk.END, values=row) 
        self.con1.close()


class EmployeeInformationWindow(tk.Frame):
    """
    Creates the window for the Employee Information. From this page, managers will be
    able to view all information about their employees. This page is not accessible
    by all employees. 

    Employee information will be displayed in a table. 
    """
    def __init__(self, parent, controller) -> None:
        """
        Initializer for the employee information window. This initializer creates the look
        of the frame with all the entries and labels. 

        Displays the employee information using a table and gets the information from the 
        management database.
        """
        super().__init__(parent)

        tk.Label(self, text="Employee Information", 
                 font=('EuphemiaUCAS 40 bold italic')).pack(pady=10,padx=10)
        tk.Button(self, text="Home", font=('EuphemiaUCAS 20 bold italic'), command=lambda: 
                  controller.show_frame(HomeWindow)).pack()
        
        self.connect() 
        h = tk.Scrollbar(self, orient='horizontal')
        h.pack(side="bottom", fill='x')
        # Creating the table employee information to display
        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5", 
                                               "c6", "c7", "c8"), show='headings', xscrollcommand=h.set)
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="Name")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Joining Date")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="Username")
        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="Password")
        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5", text="Email")
        self.tree.column("#6", anchor=tk.CENTER)
        self.tree.heading("#6", text="PhoneNumber")
        self.tree.column("#7", anchor=tk.CENTER)
        self.tree.heading("#7", text="Emergency Number")
        self.tree.column("#8", anchor=tk.CENTER)
        self.tree.heading("#8", text="Department")
        self.tree.pack()
        self.add_data()
        

        tk.Button(self,text="Logout", font=('EuphemiaUCAS 30 bold italic'),
                  command=lambda: 
                  controller.show_frame(LoginWindow)).pack()

    def connect(self):
        """
        Create the Employee table in the management database
        """
        db = EmployeeDatabase()
        
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        con1.close()

    def add_data(self):
        """
        Select all items from Employee table and display them in the table
        """
        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        cur1.execute("SELECT * FROM Employees")
        rows = cur1.fetchall()    
        for row in rows:
            print(row) 
            self.tree.insert("", tk.END, values=row)           
        con1.close()
    

if __name__ == "__main__":
    app = HotelHub()
    app.mainloop()