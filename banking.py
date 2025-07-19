def menu(accounts, acc_num):
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Logout")
        d = int(input("Enter your choice: "))

        if d == 1:
            amt = int(input("Enter deposit amount: "))
            accounts[acc_num] += amt
            print("Deposited. New balance:", accounts[acc_num])

        elif d == 2:
            amt = int(input("Enter withdrawal amount: "))
            if accounts[acc_num] >= amt:
                accounts[acc_num] -= amt
                print("Withdrawn. New balance:", accounts[acc_num])
            else:
                print("Insufficient balance.")

        elif d == 3:
            to_acc = input("Enter receiver account number: ")
            amt = int(input("Enter amount to transfer: "))
            if to_acc in accounts:
                if accounts[acc_num] >= amt:
                    accounts[acc_num] -= amt
                    accounts[to_acc] += amt
                    print("Transferred successfully.")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid receiver account.")

        elif d == 4:
            print("Your balance is:", accounts[acc_num])

        elif d == 5:
            print("Logged out.")
            break

        else:
            print("Invalid option. Try again.")


# Correct dictionary format
accounts = {
    "101": 1000,
    "102": 2000,
    "103": 3000,
    "104": 4000
}

while True:
    print("\n----BANK MANAGEMENT SYSTEM---")
    acc_input = input("Enter account number (0 to exit): ")
    if acc_input == "0":
        print("Exiting the system.")
        break
    elif acc_input in accounts:
        menu(accounts, acc_input)
    else:
        print("Invalid account number.")
