"""
CCT211: HotelHub - Aleksandra Kalas, Varchas Sharma
All the functionalities for the home page
"""
import tkinter as tk

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
        tk.Label(self, text="Home Page").pack(pady=10, padx=10)

        tk.Button(self, text="Finances of Hotel", font= ('Helvetica 20 bold italic'), 
                  command=lambda: controller.show_frame(FinancialWindow)).pack()
        tk.Button(self, text="Book a Room", font= ('Helvetica 20 bold italic'), 
                  command=lambda: controller.show_frame(BookingWindow)).pack()
        tk.Button(self, text="Stock Information", font= ('Helvetica 20 bold italic'), 
                  command=lambda: controller.show_frame(StockInformationWindow)).pack()
        tk.Button(self, text="Employee Information", font= ('Helvetica 20 bold italic'), 
                  command=lambda: controller.show_frame(EmployeeInformationWindow)).pack()
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

        # Entries and Labels for Entering Information to Book a Room for a Guest
        tk.Label(self, text="Booking Window").grid(row=0)

        # Name
        tk.Label(self, text="First Name").grid(row=1, column=0)
        first_name_entry = tk.Entry(self).grid(row=1,column=1)
        tk.Label(self, text="Last Name").grid(row=2, column=0)
        last_name_entry = tk.Entry(self).grid(row=2,column=1)

        # Address
        tk.Label(self, text="Address").grid(row=3, column=0)
        address_entry = tk.Entry(self).grid(row=3,column=1)

        #Credit Card Information
        tk.Label(self, text="Credit Card #").grid(row=4, column=0)
        credit_card_entry = tk.Entry(self).grid(row=4,column=1)

        # Number of guests staying
        tk.Label(self, text="Guest Number").grid(row=5, column=0)
        num_guests_entry = tk.Entry(self).grid(row=5,column=1)
        
        #Duration of Stay
        tk.Label(self, text="Guest Number").grid(row=6, column=0)
        num_guests_entry = tk.Entry(self).grid(row=6,column=1)

        # Bed Selection
        tk.Label(self, text="Bed Selection").grid(row=7, column=0)
        radio1 = tk.Radiobutton(self, text="Two Queens", value=1).grid(row=7, column=1)
        radio2 = tk.Radiobutton(self, text="One King", value=2).grid(row=7, column=2)

        # Additional Accomodations
        tk.Label(self, text="Other Accomodations").grid(row=8, column=0)
        accomodations_entry = tk.Entry(self).grid(row=8,column=1)

        # Return to Home Page
        tk.Button(self, text="Home", 
                  command=lambda: 
                  controller.show_frame(HomeWindow)).grid(row=9)
        #tk.Button(self, text="Home").pack()
    

class FinancialWindow(tk.Frame):
    """
    """
    def __init__(self, parent, controller) -> None:
        """
        """
        super().__init__(parent)
        tk.Label(self, text="Financial Window").pack(pady=10,padx=10)
        tk.Button(self, text="Home", 
                  command=lambda: controller.show_frame(HomeWindow)).pack()

class ToiletriesStockWindow(tk.Frame):
    """
    """
    def __init__(self, parent, controller) -> None:
        """
        """
        super().__init__(parent)
        tk.Label(self, text="Toiletries Stock").grid(row=0, column=0)
        tk.Button(self, text="Home", 
                  command=lambda: controller.show_frame(HomeWindow)).grid(row=8, column=0)

class FoodStockWindow(tk.Frame):
    """
    """
    def __init__(self, parent, controller) -> None:
        """
        """
        super().__init__(parent)
        tk.Label(self, text="Food Stock").grid(row=0, column=0)
        tk.Button(self, text="Home", 
                  command=lambda: controller.show_frame(HomeWindow)).grid(row=8, column=0)

class RoomSetUpWindow(tk.Frame):
    """
    """
    def __init__(self, parent, controller) -> None:
        """
        """
        super().__init__(parent)
        tk.Label(self, text="Room Set Up").grid(row=0, column=0)
        tk.Button(self, text="Home", 
                  command=lambda: controller.show_frame(HomeWindow)).grid(row=8, column=0)


class StockInformationWindow(tk.Frame):
    """
    
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
        #tk.Button(self, text="Home").pack()

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
        #tk.Button(self, text="Home").pack()