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

        # Inserts guest to database table
        cur.execute("""
        INSERT INTO Guests ('Name', 'Address', 'CreditCardInfo', 'NumberOfGuests', 'RoomNumber', 'BedSelection', 'CheckInDate', 'CheckOutDate') VALUES \
                    ('Kobe Bryant', '333 Stonehenge Way', '4510-2430-2098-0000', 2, 1, '2 Queen', '2008-11-11', '2008-11-14')
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
          '1234567890', 'Manager', '2945648231')]
        
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
            WorkDay TEXT,
            FOREIGN KEY (Name) REFERENCES Employees(Name)
        );
        """)
        cur.execute("INSERT INTO 'EmployeeSchedule' ('Name', 'WorkDay') VALUES \
                    ('Larry Brien', 'Monday');")
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
        
