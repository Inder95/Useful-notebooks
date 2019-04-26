
from tkinter import * # Import tkinter
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import simpledialog
import locale
    
class LoanCalculator:
    def __init__(self):
        #locale module helps your code to set country specific parameters like currency and time
        locale.setlocale(locale.LC_ALL, '' )
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
                row = 6, column = 1, sticky = E)
        btSaveLoanToFile=Button(window, text = "Save Loan To File", 
            command = self.save_to_file).grid(
                row = 6, column = 2, sticky = E)
        
        #Here we are attaching a text widget with scroll option to our Tkinter object.
        #scrolledtext.ScrolledText is an inbuilt function in Tkinter for creating such an object
        self.amort_sched=scrolledtext.ScrolledText(master=window)
        self.amort_sched.grid(row = 8, columnspan =4)
        
        
        
        window.mainloop() # Create an event loop
            
    
    def computePayment(self):
        
        # I am using a try except block to check for invalid input. When we try
        #an invalid input into float it raises ValueError. This happens when calculating monthly
        #payment. Hence I check this function for ValueError exception
        try:        
            monthlyPayment = self.getMonthlyPayment(
                float(self.loanAmountVar.get()), 
                float(self.annualInterestRateVar.get()) / 1200, 
                int(self.numberOfYearsVar.get()))
            self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
            totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
                                        * int(self.numberOfYearsVar.get())
            self.totalPaymentVar.set(format(totalPayment, '10.2f'))
            
            # Obtain monthly interest rate
            monthlyInterestRate = float(self.annualInterestRateVar.get())/1200.0
        
            # Compute mortgage 
            monthlyPayment = float(self.loanAmountVar.get())*monthlyInterestRate / \
            (1 - (pow(1 / (1 + monthlyInterestRate), float(self.numberOfYearsVar.get()) * 12)))
                
            balance = float(self.loanAmountVar.get())
            
            # Display the header
            temp="Payment#\t\tInterest\t\tPrincipal\t\tBalance\n"
            for i in range(1, int(self.numberOfYearsVar.get()) * 12 + 1):
                interest = float(monthlyInterestRate * balance * 100.0) / 100.0
                principal = float((monthlyPayment - interest) * 100.0) / 100.0
                balance = float((balance - principal) * 100.0) / 100.0
                temp=temp+(str(i) + "\t\t" + locale.currency(interest) + "\t\t" + \
                           locale.currency(principal)+ "\t\t" + locale.currency(balance)+"\n")
                #See here how the use of locale simplifies the job of formatting the string.
                #Otherwise we had to specify $ and the decimal point for every number
        
            self.amort_sched.insert(END,temp)
        
        
        except ValueError:
            s=''
            try: float(self.loanAmountVar.get())
            except ValueError: s=s+"Loan Amount "
            try: float(self.annualInterestRateVar.get())
            except ValueError: s=s+" Annual Interest Rate "
            try: float(self.numberOfYearsVar.get())
            except ValueError: s=s+"Number of years"
            s=s+" must be numbers"
            messagebox.showerror("Invalid input",s)

  
    def getMonthlyPayment(self,
            loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1
           - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;
    
    def save_to_file(self):
        #Here I am using tkinter's inbuilt function askstring to ask for the name of the file.
        # Also notice in the __init__ function how this is attached to Save To File button.
        # The rest of the eercise is simple writing to a text file.
        filename=simpledialog.askstring("Loan Recepient","Enter the name of the loan recipient")
        file=open(filename+".txt",'w')
        file.write("Loan Document for "+str(filename)+"\n")
        file.write("*"*25+"\n")
        file.write("Loan Amount: "+ locale.currency(float(self.loanAmountVar.get()))+"\t")
        file.write("Interest Rate: "+self.annualInterestRateVar.get()+"%\t")
        file.write("Nbr Years: "+self.numberOfYearsVar.get()+"\n")        
        file.write("Monthly payment: "+locale.currency(float(self.monthlyPaymentVar.get()))+"\t")
        file.write("Total Payment: "+locale.currency(float(self.totalPaymentVar.get()))+"\n\n")
        file.write("Amortization Schedule\n")       
        file.write(self.amort_sched.get(1.0,END))
        file.close()
LoanCalculator()  # Create GUI 