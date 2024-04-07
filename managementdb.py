import sqlite3

class GuestDatabase:
    def __init__(self) -> None:
        con = sqlite3.connect("managementdb.db")
        cur = con.cursor()


        # Creates table for guests with guest information
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Guests (
            GuestID INT PRIMARY KEY,
            Name TEXT,
            Address TEXT,
            CreditCardInfo VARCHAR(19),
            NumberOfGuests INT,
            RoomNumber INT,
            BedSelection TEXT,
            CheckInDate DATE,
            CheckOutDate DATE,
            SpecialRequests TEXT
        );
        """)

        # Commits changes to database
        con.commit()
        # Closes the cursor and connection
        cur.close()
        con.close()
    
class EmployeeDatabase:
    def __init__(self) -> None:
        # Creates table for employees
        self.con = sqlite3.connect("managementdb.db")
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Employees (
            EmployeeID INT PRIMARY KEY,
            Name TEXT,
            JoiningDate Date,
            Username TEXT,
            Password VARCHAR(20),
            Email TEXT,
            PhoneNumber VARCHAR(15),
            Department TEXT,
            EmergencyNumber VARCHAR(15)
        );
        """)

        # Insert many employees into the employee data base at once
        employees = [('01', 'Larry Brien', '2022-10-03', 'brien3', 'treehouse1', 
                      'larrybrien@gmail.com', '1234567890', 'Housekeeping', '2345678901'),
        ('02', 'Stacy Ryan', '2023-10-02', 'ryan4', 'pink34', 'stacyryan@gmail.com', 
         '1234567890', 'Frontdesk', '2945648901'), 
        ('03', 'Joseph Adnan', '2023-10-02', 'adnan3', 'cats46', 'josephadnan@gmail.com',
          '1234567890', 'Manager', '2945648231'),
        ('04', 'Aleksandra Kalas', '2019-11-02', 'kalas4', 'apples3', 'aleksandrakalas@gmail.com',
          '1234567890', 'Assistant', '2935648231'),
        ('05', 'Varchas Sharma', '2019-11-02', 'sharma4', 'oranges5', 'varchassharma@gmail.com',
          '1234567890', 'Assistant', '2935248231'),
        ('06', 'Dylan Hoote', '2022-08-02', 'hoote4', 'apps3', 'dylanhoote@gmail.com',
          '1234567890', 'Janitor', '2935648231')
          ]
        
        for e in employees:
            self.cur.execute("SELECT * FROM Employees WHERE EmployeeID=?", (e[0],))
            entry = self.cur.fetchone()

            if not entry:
                self.cur.execute("INSERT INTO Employees ('EmployeeID', 'Name', \
                                 'JoiningDate', 'Username', 'Password', 'Email',\
                                   'PhoneNumber', 'Department', 'EmergencyNumber') \
                                 VALUES  (?, ?, ?, ?, ?,  ?, ?, ?, ?)", (e[0], e[1], e[2],
                                    e[3], e[4], e[5], e[6], e[7], e[8]))
            self.con.commit()
 
        # Commits changes to database
        self.con.commit()
        # Closes the cursor and connection
        self.cur.close()
        self.con.close()


class EmployeeSchedule:
    def __init__(self) -> None:
        con = sqlite3.connect("managementdb.db")
        cur = con.cursor()
        # Creates table for schedule of employees
        cur.execute("""
        CREATE TABLE IF NOT EXISTS EmployeeSchedule (
            Id INTEGER PRIMARY KEY,
            Name INTEGER,
            WorkDay TEXT
        );
        """)
        cur.execute("INSERT INTO 'EmployeeSchedule' ('Name', 'WorkDay') VALUES \
                    ('Larry Brien', 'Monday');")
        cur.execute("INSERT INTO 'EmployeeSchedule' ('Name', 'WorkDay') VALUES \
                    ('Stacy Ryan', 'Tuesday');")
        cur.execute("INSERT INTO 'EmployeeSchedule' ('Name', 'WorkDay') VALUES \
                    ('Joseph Adnan', 'Friday');")
        # Commits changes to database
        con.commit()
        # Closes the cursor and connection
        cur.close()
        con.close()

    
class StockDatabase:
    def __init__(self) -> None:
        con = sqlite3.connect("managementdb.db")
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Stock (
            PurchaseDate DATE,
            Toiletries INT,
            Food INT,
            RoomSetUp INT
        );
        """)
        # Commits changes to database
        con.commit()
        # Closes the cursor and connection
        cur.close()
        con.close()

class FoodStockDatabase:
    def __init__(self) -> None:
        con = sqlite3.connect("managementdb.db")
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS FoodStock (
            HotelLevel INT,
            BreakfastFood INT,
            LunchFood INT,
            DinnerFood INT,
            MiniFridge INT
        );
        """)

        food_data = [
            (1, 0, 5, 15, 20),
            (2, 35, 36, 20, 25),
            (3, 34, 36, 22, 32),
            (4, 32, 32, 19, 21),
            (5, 31, 26, 13,19)
        ]

        cur.executemany('INSERT into FoodStock (HotelLevel, BreakfastFood, LunchFood, \
                        DinnerFood, MiniFridge) VALUES (?, ?, ?, ?, ?)', food_data)
        # Commits changes to database
        con.commit()
        # Closes the cursor and connection
        cur.close()
        con.close()

class RoomSetupDatabase:
    def __init__(self) -> None:
        con = sqlite3.connect("managementdb.db")
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS RoomSetup (
            HotelLevel INT,
            Bedding INT,
            Washroom INT,
            CarpetClean INT,
            StaffRoom INT
        );
        """)

        roomsetup_data = [
            (1, 0, 5, 15, 3),
            (2, 35, 36, 20, 2),
            (3, 34, 36, 22, 2),
            (4, 32, 32, 19, 2),
            (5, 31, 26, 13, 2)
        ]

        cur.executemany('INSERT into RoomSetup (HotelLevel, Bedding, Washroom, \
                        CarpetClean, StaffRoom) VALUES (?, ?, ?, ?, ?)', roomsetup_data)

        # Commits changes to database
        con.commit()
        # Closes the cursor and connection
        cur.close()
        con.close()

class ToiletriesStockDatabase:
    def __init__(self) -> None:
        con = sqlite3.connect("managementdb.db")
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS ToiletriesStock (
            HotelLevel INT,
            Washrooms INT,
            HotelRooms INT,
            MaidRoom INT,
            StaffRoom INT
        );
        """)

        toiletries_data = [
            (1, 0, 5, 15, 3),
            (2, 35, 36, 20, 2),
            (3, 34, 36, 22, 2),
            (4, 32, 32, 19, 2),
            (5, 31, 26, 13, 2)
        ]

        cur.executemany('INSERT into ToiletriesStock (HotelLevel, Washrooms, HotelRooms, \
                        MaidRoom, StaffRoom) VALUES (?, ?, ?, ?, ?)', toiletries_data)
        # Commits changes to database
        con.commit()
        # Closes the cursor and connection
        cur.close()
        con.close()
