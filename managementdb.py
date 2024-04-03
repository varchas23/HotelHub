import sqlite3

def condb():
    # Connects database to python
    con = sqlite3.connect("managementdb.db")
    cur = con.cursor()

    # Creates table for guests with guest information
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Guests (
            GuestID INT PRIMARY KEY,
            Name TEXT,
            DOB DATE,
            Address TEXT,
            Email TEXT,
            CreditCardInfo VARCHAR(19),
            NumberOfGuests INT,
            RoomNumber INT,
            CheckInDate DATE,
            CheckOutDate DATE,
            SpecialRequests TEXT
    );
    """)

    # Creates table for employees
    cur.execute("""
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

    # Inserts employees to Employees table
    cur.execute("""INSERT INTO 'Employees' ('Name', 'JoiningDate', 'Username', 'Password', 'Email', 'PhoneNumber', 'Department', 'EmergencyNumber') VALUES 
                ('Larry Brien', '2022-10-03', 'brien3', 'treehouse1', 'larrybrien@gmail.com', '1234567890', 'Housekeeping', '2345678901');
                """)

    # Commits changes to database
    con.commit()

    # Closes the cursor and connection
    cur.close()
    con.close()