from datetime import datetime

income = []
expense = []

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Report")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter income amount (₹): "))
        purpose = input("Enter purpose (e.g., Salary, Bonus): ")
        date = datetime.now().strftime("%Y-%m-%d")
        income.append((amount, date, purpose))
        print(f"Added ₹{amount} income for '{purpose}' on {date}.")

    elif choice == "2":
        amount = float(input("Enter expense amount (₹): "))
        purpose = input("Enter purpose (e.g., Food, Rent): ")
        date = datetime.now().strftime("%Y-%m-%d")
        expense.append((amount, date, purpose))
        print(f"Added ₹{amount} expense for '{purpose}' on {date}.")

    elif choice == "3":
        total_income = sum(i[0] for i in income)
        total_expense = sum(e[0] for e in expense)
        balance = total_income - total_expense

        print(f"\n--- Report ---")
        print(f"Total Income : ₹{total_income}")
        print(f"Total Expense: ₹{total_expense}")
        print(f"Balance      : ₹{balance}")

        print("\nIncome entries:")
        for amt, dt, purp in income:
            print(f"+ ₹{amt} on {dt} for {purp}")

        print("\nExpense entries:")
        for amt, dt, purp in expense:
            print(f"- ₹{amt} on {dt} for {purp}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")