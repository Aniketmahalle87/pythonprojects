#banking application
from datetime import datetime
import datetime
import time


class Account:
    def __init__(self,account_no,balance = 0):
        self.account_no = account_no
        self.balance = balance
        self.history = [] 
        

    #method 1 (debit)
    def debit(self,amount):
         if amount > self.balance:
            print("Insufficient Balance!")
            self.history.append((datetime.datetime.now(), f"Failed Debit: ₹{amount}"))
         else:
            self.balance -= amount
            print(f"your account is being debited by {amount}, remaining bal {self.balance}")
            self.history.append((datetime.datetime.now(), f"Debited ₹{amount}"))
    
    #metho 2 (credit)
    def credit(self,amount):
        self.balance += amount
        print(f"your account is being credited by {amount}, bal {self.balance}")  
        self.history.append((datetime.datetime.now(), f"Credited ₹{amount}"))

    #method 3 (balance)
    def getbalanced(self):
        print(f"your balance for account {self.account_no} is {self.balance}")
        
    #method 4 (transaction log)
    def view_history(self):
        print(f"\nTransaction History for Account {self.account_no}:")
        for entry in self.history:
            print(f"{entry[0].strftime('%d-%m-%Y %H:%M:%S')} --> {entry[1]}")

#-------------------------------------
#main program
#-------------------------------------

def main():
    #create account with user input
    account_no = int(input("Enter your account number: "))
    initial_balance = float(input("enter initial balance"))

    #create account ob
    account = Account(account_no,initial_balance)
    

    time.sleep(10)
    # Menu loop
    while True:
        print("\n--- Banking Menu ---")
        print("1. Credit Money")
        print("2. Debit Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Enter you choice: ")

        if choice == "1":
            amount = float(input("Enter amount to credit: $"))
            account.credit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to debit: ₹"))
            account.debit(amount)
        elif choice == '3':
            account.getbalanced()
        elif choice == '4':
            account.view_history()
        elif choice == '5':
            print("Thank you for using the Banking App!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
