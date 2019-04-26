# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:35:10 2017

@author: Inderpreet
"""

def amortization(self,loanAmount,annualInterestRate,numOfYears):
                # Obtain monthly interest rate
                monthlyInterestRate = annualInterestRate/1200
        
                # Compute mortgage 
                monthlyPayment = loanAmount*monthlyInterestRate / \
                    (1 - (pow(1 / (1 + monthlyInterestRate), numOfYears * 12)))
                
                balance = loanAmount
                temp=''
                # Display the header
                print("Payment#\tInterest\tPrincipal\tBalance")
                for i in range(1, numOfYears * 12 + 1):
                    interest = int(monthlyInterestRate * balance * 100) / 100.0
                    principal = int((monthlyPayment - interest) * 100) / 100.0
                    balance = int((balance - principal) * 100) / 100.0
                    temp=temp+(str(i) + "\t\t" + str(interest) + "\t\t" + \
                                                str(principal) + "\t\t" + str(balance))
                    return(temp)
            
            amort_sched.insert(amortization(float(self.loanAmountVar.get()),float(self.annualInterestRateVar.get()), float(self.numberOfYearsVar.get()))