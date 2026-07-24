# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

if age >= 60:
    print("Senior")
elif age >= 20:
    print("Adult")
elif age >= 13:
    print("Teenager")
elif age >= 0:
    print("Child")
else:
    print("Error your input not correct")



# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if(choice == "1"):
            print(25*"=","Check Balance",25*"=")
            print(29*" ",balance)
            print(65*"=")
        elif(choice == "2"):
            print(25*"=","Withdraw",25*"=")
            Withdraw = float(input("Enter amount: "))
            while Withdraw > balance:
                Withdraw = float(input("Enter amount again: "))
            balance = balance - Withdraw
            print(29*" ","Balance you left: ",balance)
            print(65*"=")
        elif(choice == "3"):
            print(25*"=","Deposit",25*"=")
            Deposit = float(input("Enter amount: "))
            while Deposit <= 0:
                Deposit = float(input("Enter amount again: "))
            balance = balance + Deposit
            print(20*" ","Balance you left: ",balance)
            print(65*"=")
        elif(choice == "4"):
            print("Good Bye")
            break
        else:
            print("Please enter Choice again!!")
            
        
else:
    print("Invalid PIN")
