#this is an app used for tracking personal expenses.
"""
Developing a personal expenses tracker that allows
user to add,
view expense
total expense
deletion of expense
and exit
"""

#greetings
print("Welcome to personal expense tracker application!")

#importing libraries/dependencies
import os
import csv
from datetime import datetime
import time

#creating def for adding expense now.

def add_expenses(description,amount):
    
    #will open file first and then add the record
        with open('personal_expense.csv','a',newline="") as file:
            line = csv.writer(file)
            line.writerow([description,amount,datetime.now().strftime("%d/%m/%Y, %H:%M")])
    
        print("expense has been added successfully!")

        
#creating def for viewwing the expense now.

def veiw_expenses():
    if os.path.exists('personal_expense.csv'):
        with  open('personal_expense.csv','r') as file:
            content = csv.reader(file)
            for expense in content:
                print(f"Expense_Name:{expense[0]}, Amount: {expense[1]}, Date: {expense[2]}")
    else:
        print("File not found!")

#creating def for total amount expense.

def total_amount():
    total_amount = 0
    
    with open('personal_expense.csv','r') as file:
        content = csv.reader(file)
        for expense in content:
            try:
                amount = float(expense[1].strip())
                total_amount += amount #here we are adding the amount coloumn
            except ValueError:
                print(f"Invalid amount in row: {expense}. Skipping...")

    print(f"Total Amount Spent: {total_amount}")

            
def expense_delete(expensename):
    
     # Read the entire content of the file into a list
    with open('personal_expense.csv', 'r') as file:
            content = list(csv.reader(file))  # Convert the csv.reader object into a list

    # Filter out the expense to be deleted
    update_content =  [expense for expense in content if expense[0] != expensename]

     # Check if anything was deleted
    if len(update_content)==len(content):
        print(f"No expense found with the name '{expensename}'.")
    else:
        with open('personal_expense.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(update_content)
        print(f"Expense '{expensename}' has been deleted.")
    

#creating main function:

def main():
    while True:
        time.sleep(3)
        print('***********************')
        print("\n1.Add Expense")
        print("2.View Expense")
        print("3.Total Amount")
        print("4.To delete the expense")
        print("5.Exit")

        choice = int(input("\nChoose the correct choice: "))

        if choice == 1:
            description = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            add_expenses(description,amount)

        elif choice == 2:
            print("Your Monthly expenses are below: ")
            veiw_expenses()

        elif choice == 3:
            print("Your monthly total expense: ")
            total_amount()

        elif choice == 4:
            expensename = input("Enter the name of the expense you wanted to delete: ")
            expense_delete(expensename)
        
        elif choice == 5:
            print("Thanks for adding expense!")
            break

        else:
            print("Invalid choice, Plese choose the correct choice!")

if __name__ == '__main__':
    main()

