# File to store the  expense records
File_Name="expense.txt"
# Function to add new expense record in file
def add_expense():
    # Take input from the user
    date=input("Enter the date (DD/MM/YYYY):")
    category=input("Enter the category:")
    amount=input("Enter the amount:")
    # Append the expense record in file
    with open(File_Name ,"a") as f:
        f.write(f"{date},{category},{amount}\n")
        print("Expense is added successfully")
# Function to display all expense records
def view_expense():
    print("\n All Expenses")
    found=False
    # Read and display each expense record
    with open(File_Name,"r") as f:
        for record in f:
            date,category,amount=record.strip().split(",")
            print(f"{date},{category},{amount}\n")
            found=True
    # Notify if no record found
    if not found:
        print("no expense found")
# Search for expense by category
def search_expense():
    category=input("Enter the category:")
    searched=False
    #Search matching category records
    with open(File_Name,"r") as f:
        for record in f:
            date,cat,amount=record.strip().split(",")
            if cat.lower()==category.lower():
                print("\n Expense Found")
                print("Date:",date)
                print("Category:",category)
                print("Amount:",amount )
                searched=True
    # Notify if no matching records if found
    if not searched:
        print("no expense found")
# Delete the expense records matching the specified category
def del_expense():
    category=input("Enter the category:")
    deleted=False
    expense=[]
    # Read all records and exclude the selected category
    with open(File_Name,"r") as f:
        for record in f:
            date,cat,amount=record.strip().split(",")
            if cat.lower()==category.lower():
                deleted=True
                continue
            expense.append(f"{date},{cat},{amount}\n")
    # Update the file with the remaining records
    if deleted:
        with open(File_Name,"w") as f:
            f.writelines(expense)
            print("Expense deleted successfully")
# Calculate and display the total expense amounts
def total_expense():
    total=0
    # Sum of all expense amounts
    with open(File_Name,"r") as f:
        for record in f:
            date,cat,amount=record.strip().split(",")
            total+=int(amount)
    print("Total expense:", total)
# Main Menu
while True:
    # Display the selected options
    print("=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Total Expense")
    print("6. Exit")
    # Read users selection
    choice=int(input("Enter the choice:"))
    # Execute selected operations
    if(choice==1):
        add_expense()
    elif(choice==2):
        view_expense()
    elif(choice==3):
        search_expense()
    elif(choice==4):
        del_expense()
    elif(choice==5):
        total_expense()
    elif(choice==6):
        print("Thank You!")
        break
    else:
        print("Invalid choice!")     

