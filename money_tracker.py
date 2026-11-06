transactions = []
balance = 0

while True:
    print("\n--- Daily Expense Tracker ---")
    print("1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        amount = float(input("Enter income amount:"))
        balance+=amount
        transaction = {"type": "Income", "amount": amount }
        transactions.append(transaction)
        print("income amount is successfully add")
        
    elif choice == "2":
        amount = float(input("Entter expense amount:"))
        if amount <= balance:
            balance -= amount
        
            transaction = {"type":"Expense","amount":amount}
            transactions.append(transaction)
            print("expense amount is successfully added")
        else:
            print("Insufficient balance!")
        
    elif choice == "4":
        if len(transactions) == 0:
            print("no transactions")
        else :
            for item in transactions:
                print("Type:",item["type"])
                print("Amount",item["amount"])
                print()
            
    elif choice == "3" :
        print("Your balance is ",balance)
        
    elif choice == "5":
        print("Thank you for using this money tracker!")
        break
    else:
        print("Invalid choice. you should choose (1-5)")
        
        
        