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

        self.cur.execute("""INSERT INTO 'Employees' ('Name', 'JoiningDate', 'Username', 'Password', 'Email', 'PhoneNumber', 'Department', 'EmergencyNumber') VALUES
                ('Larry Brien', '2022-10-03', 'brien3', 'treehouse1', 'larrybrien@gmail.com', '1234567890', 'Housekeeping', '2345678901');
                """)

        # Commits changes to database
        self.con.commit()
        # Closes the cursor and connection
        self.cur.close()
        self.con.close()
    
    """def insert(self, name, joindate, username, password, email, phonenumber, 
               department, emergencynum,):
        self.cur.execute("SELECT * FROM Employees WHERE Name=?", (name,))
        entry = self.cur.fetchone()

        if not entry:
            self.cur.execute("INSERT INTO Employees ('Name', 'JoiningDate', \
                             'Username', 'Password', 'Email', 'PhoneNumber', \
                             'Department', 'EmergencyNumber') VALUES (?, '?', ?, ?, ?, \
                             ?, ?, ?)", (name, joindate, username, password, email, 
                                         phonenumber, department, emergencynum) )"""

    
class FoodStockDatabase:
    def __init__(self) -> None:
        con = sqlite3.connect("managementdb.db")
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Stock (
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
        
