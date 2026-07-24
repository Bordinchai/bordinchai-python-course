print("Choose your currency to convert")
print("THB to US type:1")
print("US to THB type:2")
choice = int(input("Enter:"))
if(choice == 1):
    THB = float(input("Enter amount:"))
    USD = THB / 35.5
    print("Total:",round(USD,2))
elif(choice == 2):
    USD = float(input("Enter amount:"))
    THB = USD * 35.5
    print("Total:",round(THB,2))
else:
    print("Please Choose 1 or 2")