"""
CCT211: HotelHub - Aleksandra Kalas, Varchas Sharma
All the functionalities for the home page
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sqlite3, matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from managementdb import GuestDatabase, EmployeeDatabase,StockDatabase, \
    RoomSetupDatabase, ToiletriesStockDatabase, FoodStockDatabase
class HomeWindow(tk.Frame):
    """
    Creates the main home window for HotelHub. From this window, users can access all
    other windows by selecting the corresponding button. 
    
    This page is used as a central navigation page for the user. It should be 
    accessible from each page that the user is on. 
    """
    def __init__(self, parent, controller):
        """ 
        
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
        
class EmployeeHomeWindow(tk.Frame):
    def __init__(self, parent, controller):
        """ 
        
        """
        super().__init__(parent)
        tk.Label(self, text="Home Page").pack(pady=10, padx=10)

        tk.Button(self, text="Book a Room", font= ('Helvetica 20 bold italic'), 
                  command=lambda: controller.show_frame(BookingWindow)).pack()
        tk.Button(self, text="Stock Information", font= ('Helvetica 20 bold italic'), 
                  command=lambda: controller.show_frame(StockInformationWindow)).pack()
        tk.Button(self, text="Employee Schedule", font= ('Helvetica 20 bold italic'), 
                  command=lambda: controller.show_frame(EmployeeScheduleWindow)).pack()

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
        tk.Label(self, text="Booking Window").grid(row=0)


        # Guest id
        tk.Label(self, text="Guest Id").grid(row=1, column=0)
        id_entry = tk.Entry(self)
        id_entry.grid(row=1,column=1)
        
        # Name
        tk.Label(self, text="Guest Name").grid(row=2, column=0)
        name_entry = tk.Entry(self)
        name_entry.grid(row=2,column=1)

        # Address
        tk.Label(self, text="Address").grid(row=3, column=0)
        address_entry = tk.Entry(self)
        address_entry.grid(row=3,column=1)

        #Credit Card Information
        tk.Label(self, text="Credit Card #").grid(row=4, column=0)
        credit_card_entry = tk.Entry(self)
        credit_card_entry.grid(row=4,column=1)

        # Number of guests staying
        tk.Label(self, text="Guest Number").grid(row=5, column=0)
        num_guests_entry = tk.Entry(self)
        num_guests_entry.grid(row=5,column=1)

        # Room number
        tk.Label(self, text="Room Number").grid(row=6, column=0)
        room_num_entry = tk.Entry(self)
        room_num_entry.grid(row=6,column=1)

        # Bed Selection
        tk.Label(self, text="Bed Selection").grid(row=7, column=0)
        bed_entry = tk.Entry(self)
        bed_entry.grid(row=7,column=1)

        #Duration of Stay
        tk.Label(self, text="Check-in").grid(row=8, column=0)
        checkin_entry = tk.Entry(self)
        checkin_entry.grid(row=8,column=1)
        tk.Label(self, text="Check-out").grid(row=9, column=0)
        checkout_entry = tk.Entry(self)
        checkout_entry.grid(row=9,column=1)


        # Additional Accomodations
        tk.Label(self, text="Other Accomodations").grid(row=10, column=0)
        accomodations_entry = tk.Entry(self)
        accomodations_entry.grid(row=10,column=1)

        tk.Button(self, text="Complete Booking", command=lambda: self.add_guest(
            id_entry.get(), name_entry.get(), address_entry.get(),credit_card_entry.get(),
            num_guests_entry.get(), room_num_entry.get(), bed_entry.get(), 
            checkin_entry.get(), checkout_entry.get(), accomodations_entry.get())
            ).grid(row=11, column=5)

        # Return to Home Page
        tk.Button(self, text="Home", 
                  command=lambda: 
                  controller.show_frame(HomeWindow)).grid(row=12)
    
    def connect(self):
        """
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
        """
        super().__init__(parent)
        tk.Label(self, text="Financial Window").pack(pady=10,padx=10)
        tk.Button(self, text="Home", 
                  command=lambda: controller.show_frame(HomeWindow)).pack()
        
        self.connect()
        self.con = sqlite3.connect("managementdb.db")
        self.cur = self.con.cursor()

        self.monthsGuests, self.numGuests, self.months_income = [], [], []
        self.income, self.months_expenditure, self.expenditure = [], [], []

        self.cur.execute("SELECT strftime('%m', CheckInDate) AS Month, \
                         COUNT(GuestID) AS GuestsNumber FROM Guests \
                         GROUP BY strftime('%m', CheckInDate);")
        incomingGuests = self.cur.fetchall()
        for tup in incomingGuests:
            self.monthsGuests.append(int(tup[0]))
            self.numGuests.append(tup[1])

        self.cur.execute("SELECT strftime('%m', CheckInDate) AS Month, \
                         SUM(NumberOfGuests * 80) AS Income FROM Guests \
                         GROUP BY strftime('%m', CheckInDate);")
        income_data = self.cur.fetchall()
        for tup in income_data:
            self.months_income.append(int(tup[0]))
            self.income.append(tup[1])

        self.cur.execute("SELECT strftime('%m', PurchaseDate) AS Month, \
                         SUM(Toiletries + Food + RoomSetUp) AS Expenditure FROM Stock \
                         GROUP BY strftime('%m', PurchaseDate);")
        expenditure_data = self.cur.fetchall()
        for tup in expenditure_data:
            self.months_expenditure.append(int(tup[0]))
            self.expenditure.append(tup[1])

        self.con.close()
    
    def connect(self):
        """
        """
        db = StockDatabase()

        con1 = sqlite3.connect("managementdb.db")
        cur1 = con1.cursor()
        con1.close()
    
    def displayGraph(fig1, fig2, fig3):
        """
        Draws the data visualizations on the Financial Window Page
        """
        canvasGuests = FigureCanvasTkAgg(fig1, master=FinancialWindow)
        canvasGuests.draw()
        canvasGuests.get_tk_widget().grid(row=0, column=0)

        canvasIncome = FigureCanvasTkAgg(fig2, master=FinancialWindow())
        canvasIncome.draw()
        canvasIncome.get_tk_widget().grid(row=0, column=1)

        canvasExpenditure = FigureCanvasTkAgg(fig3, master=FinancialWindow)
        canvasExpenditure.draw()
        canvasExpenditure.get_tk_widget().grid(row=1, column=0, columnspan=2)
    
    def plotGraph(self):
        # Creates line graph visualization of incoming guests over a year
        fig1 = plt.figure(figsize=(10, 5))
        plt.plot(self.monthsGuests, self.numGuests, marker='orange', color='blue')
        plt.title('View of Incoming Guests Over a Year')
        plt.xlabel('Month')
        plt.ylabel('Number of Guests')
        plt.grid(True)
        plt.xticks(range(1, 13))  # Assuming months are represented as integers from 1 to 12
        plt.tight_layout()
        plt.show()

        # Creates line graph visualization of income created each month
        fig2 = plt.figure(figsize=(10, 5))
        plt.plot(self.months_income, self.income, marker='orange', color='green')
        plt.title('View of Income Made Each Month')
        plt.xlabel('Month')
        plt.ylabel('Income ($)')
        plt.grid(True)
        plt.xticks(range(1, 13))  # Assuming months are represented as integers from 1 to 12
        plt.tight_layout()
        plt.show()

        # Creates line graph visualization of purchases for stock each month
        fig3 = plt.figure(figsize=(10, 5))
        plt.plot(self.months_expenditure, self.expenditure, marker='orange', color='red')
        plt.title('Money Spent on Purchases for Stock Each Month')
        plt.xlabel('Month')
        plt.ylabel('Expenditure ($)')
        plt.grid(True)
        plt.xticks(range(1, 13))  # Assuming months are represented as integers from 1 to 12
        plt.tight_layout()
        plt.show()

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
        """
        super().__init__(parent)
        tk.Label(self, text="Toiletries Stock").pack()
        tk.Button(self, text="Home", 
                  command=lambda: controller.show_frame(HomeWindow)).pack()
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
    
    def connect(self):
        """
        Create the Employee table in the management database
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
        """
        super().__init__(parent)
        tk.Label(self, text="Food Stock").pack()
        tk.Button(self, text="Home", 
                  command=lambda: controller.show_frame(HomeWindow)).pack()
        
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
        
        self.add_data()

    def connect(self):
        """
        Create the Employee table in the management database
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
        """
        super().__init__(parent)
        tk.Label(self, text="Room Set Up").pack()
        tk.Button(self, text="Home", 
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
    
    def connect(self):
        """
        Create the Employee table in the management database
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
    Creates the stock information window for HotelHub. From this window, the manager
    and the employees should be able to view what stock is available on each floor.
    When there is a low level of stock on a floor the level will be highlighted to 
    indicate to workers that is re-stock required in that area. 
    """

    def __init__(self, parent, controller) -> None:
        """

        """
        super().__init__(parent)
        tk.Label(self, text="Stock Information").grid(row=0, column=0)
        
        # Buttons to lead to other frames for each stock 
        tk.Button(self, text="Toiletries", command=lambda:
                   controller.show_frame(ToiletriesStockWindow)).grid(row=1,column=0)
        tk.Button(self, text="Food", command=lambda: 
                  controller.show_frame(FoodStockWindow)).grid(row=2,column=0) 
        tk.Button(self, text="Room Set Up", command=lambda: 
                  controller.show_frame(RoomSetUpWindow)).grid(row=3,column=0) 
        
        tk.Button(self, text="Home", command=lambda: 
                  controller.show_frame(HomeWindow)).grid(row=4,column=0)


class EmployeeScheduleWindow(tk.Frame):
    """
    """
    def __init__(self, parent, controller) -> None:
        """
        """
        super().__init__(parent)
        tk.Label(self, text="Employee Schedule").pack(pady=10,padx=10)
        tk.Button(self, text="Home", command=lambda:
                  controller.show_frame(HomeWindow)).pack()
        self.con = sqlite3.connect("managementdb.db")
        self.cur = self.con.cursor()
   
    def getData(self):
        self.cur.execute("SELECT Name, WorkDay FROM EmployeeSchedule")
        data = self.cur.fetchall()
        self.con.close()
        return data

    def showSchedule(self):
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for i, day in enumerate(days):
            tk.Label(self, text=day, padx=10, pady=10, borderwidth=1).grid(row=0, column=i, sticky="ew")

        schedule = {day: [] for day in days}
        for workDay, name in self.getData():
            schedule[workDay].append(name)

        for i, day in enumerate(days):
            names = schedule.get(day, [])
            for j, name in enumerate(names, start=1):
                tk.Label(self, text=name, padx=5, pady=5, borderwidth=1).grid(row=j, column=i, sticky="ew")


class EmployeeInformationWindow(tk.Frame):
    """
    """
    def __init__(self, parent, controller) -> None:
        """
        """
        super().__init__(parent)

        tk.Label(self, text="Employee Information").pack(pady=10,padx=10)
        tk.Button(self, text="Home", command=lambda: 
                  controller.show_frame(HomeWindow)).pack()
        
        self.connect() 
        
        # Creating the table employee information to display
        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5", 
                                               "c6", "c7", "c8"), show='headings')
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
        self.tree.heading("#7", text="Department")
        self.tree.column("#8", anchor=tk.CENTER)
        self.tree.heading("#8", text="Emergency Number")
        self.tree.pack()
        self.add_data()

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
    