# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 08:52:16 2017

@author: Inderpreet
"""

from tkinter import * # Import tkinter
    
class LoanCalculator:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Loan Calculator") # Set title
        
        Label(window, text = "Annual Interest Rate").grid(row = 1, 
            column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2, 
            column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 3, 
            column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 4, 
            column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 5, 
            column = 1, sticky = W)
        
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, 
            justify = RIGHT).grid(row = 1, column = 2)
        
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, 
            justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, 
            justify = RIGHT).grid(row = 3, column = 2)
        
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable = 
            self.monthlyPaymentVar).grid(row = 4, column = 2, 
                sticky = E)
        
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable = 
            self.totalPaymentVar).grid(row = 5, 
                column = 2, sticky = E)
        btComputePayment = Button(window, text = "Compute Payment", 
            command = self.computePayment).grid(
                row = 6, column = 2, sticky = E)
        try:
            window.mainloop() # Create an event loop

        except ValueError:
                error_vars=validate()
                print("Invalid input.",error_vars,"must be numbers")
            
        def validate():
            s=""
            try: float(annualInterestRateVar)
            except ValueError:  s=s+"Annual Interest Rate "
            try: float(numberOfYearsVar)
            except ValueError: s=s+ "Number of Years "
            try: float(loanAmountVar)
            except ValueError:s=s+"Loan Amount "
            return s
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), 
            float(self.annualInterestRateVar.get()) / 1200, 
            int(self.numberOfYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
        
    def getMonthlyPayment(self,
            loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1
           - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;

LoanCalculator()  # Create GUI 