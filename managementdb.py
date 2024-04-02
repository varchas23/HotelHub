import sqlite3

def condb():
    # Connects database to python
    con = sqlite3.connect("managementdb.db")
    cur = con.cursor()

    # Creates table for guests with guest information
    cur.execute("""
    CREATE TABLE Guests (
        GuestID INT PRIMARY KEY AUTO_INCREMENT,
        Name TEXT,
        DOB DATE,
        Address VARCHAR(255)
        CreditCardInfo VARCHAR(19)
        NumberOfGuests INT
        RoomNumber INT FOREIGN KEY REFERENCES (insert booking table)
        CheckInDate DATE
        CheckOutDate DATE
        SpecialRequests TEXT
    )
    """)