#A bank financial system for bank and credit unions

#SavingsAccount class 
class Savings_Acoount:
    def __init__(self, account_number, interest_rate, account_balance):
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.account_balance = account_balance
        
    def display(self):
        print('*** Savings Account ***')
        print('    ---------------  ')
        print('Account Number is: '+self.account_number)
        print('Interest Rate is: '+str(self.interest_rate))
        print('Account Balance is: '+str(self.account_balance))
        print('\n')
        
              
#Cerificaeofdeposit class       
class Certificate_of_Deposit_Account:
    def __init__(self, account_number, interest_rate, account_balance, account_maturity_date):
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.account_balance = account_balance
        self.account_maturity_date = account_maturity_date
    
    def display(self):
        print('*** Certificate of Deposit ***')
        print('    ----------------------  ')
        print('Account Number is: '+self.account_number)
        print('Interest Rate is: ' +str(self.interest_rate))
        print('Account Balance is: '+str(self.account_balance))
        print('Account Maturity Date is: '+self.account_maturity_date)
        print('\n')
            
        
#Display all Data for both savingsAccount and certificateofDeposit
print('------------------------------------------------------------')
account = input('Enter your Account Number for Savings Account: ')
interest = float(input('Enter your Interest Rate for Savings Account: '))
balance = float(input('Enter your Account Balance for Savings Account: '))
saving = Savings_Acoount(account, interest, balance)
print('------------------------------------------------------------')

print('\n')
    
print('------------------------------------------------------------')
account = input('Enter your Account Number for CD: ')
interest = float(input('Enter your Interest Rate for CD: '))
balance = float(input('Enter your Account Balance for CD: '))
matuityDate = input('Enter the Account Maturity Date for CD: ')
CD = Certificate_of_Deposit_Account(account, interest, balance, matuityDate)
print('------------------------------------------------------------')
print('\n')
        
        
#Object declaration
saving.display()
CD.display()     
    