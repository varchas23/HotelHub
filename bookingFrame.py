"""
All the functionalities for the hotel booking page
"""
import tkinter as tk
#from financialFrame import FinancialWindow
#from stockInformationFrame import StockInformationWindow
#from employeeInformation import EmployeeInformationWindow
#from employeeScheduleFrame import EmployeeScheduleWindow
#from homePageFrame import HomeWindow

class BookingWindow(tk.Frame):
    """
    """
    def __init__(self, parent, controller) -> None:
        """
        """
        super().__init__(parent)
        tk.Label(self, text="Booking Window").pack(pady=10,padx=10)
       # tk.Button(self, text="Home", command=lambda: controller.show_frame(HomeWindow)).pack()
        tk.Button(self, text="Home").pack()