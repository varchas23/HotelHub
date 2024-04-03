"""
All the functionalities for the home page
"""
import tkinter as tk
from bookingFrame import BookingWindow
from financialFrame import FinancialWindow
from stockInformationFrame import StockInformationWindow
from employeeInformation import EmployeeInformationWindow
from employeeScheduleFrame import EmployeeScheduleWindow

class HomeWindow(tk.Frame):
    def __init__(self, parent, controller):
        """ 
        instead of creating new frames for employee vs manager - we can do 
        a check here when they try to access 
        """
        super().__init__(parent)
        tk.Label(self, text="Home Page").pack(pady=10, padx=10)

        tk.Button(self, text="Finances of Hotel",
                  command=lambda: controller.show_frame(FinancialWindow)).pack()
        tk.Button(self, text="Book a Room",
                  command=lambda: controller.show_frame(BookingWindow)).pack()
        tk.Button(self, text="Stock Information",
                  command=lambda: controller.show_frame(StockInformationWindow)).pack()
        tk.Button(self, text="Employee Information",
                  command=lambda: controller.show_frame(EmployeeInformationWindow)).pack()
        tk.Button(self, text="Employee Schedule",
                  command=lambda: controller.show_frame(EmployeeScheduleWindow)).pack()