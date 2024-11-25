def bank_management_system():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    balance = 20000

    while True:
        print("\nChoose an option:")
        print("1. Credit")
        print("2. Debit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter the amount to credit: "))
            balance += amount
            print("New balance:", balance)

        elif choice == 2:
            amount = float(input("Enter the amount to debit: "))
            if amount <= balance:
                balance -= amount
                print("New balance:", balance)
            else:
                print("Insufficient balance.")

        else:
            print("Invalid choice.")

        print("\nDo you want to continue? (yes/no)")
        if input().lower() != "yes":
            break

bank_management_system()