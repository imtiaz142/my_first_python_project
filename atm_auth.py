accounts = {}

print("🏦 Welcome to Python ATM")
print("1. Create New Account")
print("2. Login to Existing Account")

choice = input("Choose option 1 or 2: ")

if choice == "1":
    acc_no = int(input("Please Enter your account number: "))
    
    if acc_no in accounts:
        print("❌ This account number is already assigned.")
    else:
        name = input("Please Enter your name: ")
        pin = int(input("Please Enter your PIN number: "))
        balance = float(input("Please Enter your balance: "))
        
        accounts[acc_no] = {
            "name": name,
            "pin": pin,
            "balance": balance
        }
        print("✅ Account created successfully!")

elif choice == "2":
    acc_no = int(input("Please Enter your account number: "))
    
    if acc_no in accounts:
        pin = int(input("Enter your PIN: "))
        
        if accounts[acc_no]["pin"] == pin:
            print("✅ Login successful!")
            # You can add transaction menu here
        else:
            print("❌ Incorrect PIN.")
    else:
        print("❌ Account not found.")

else:
    print("❌ Input a valid number.")
