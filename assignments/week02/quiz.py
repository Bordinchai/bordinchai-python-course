"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""

#BMI Calculater

weight = float(input("Enter Weight(kg):"))
height = float(input("Enter Height(meter):"))
Bmi = weight / (height ** 2)

print(round(Bmi,1))

if Bmi >= 30:
    print("Obese")
elif Bmi < 30:
    print("Overweight")
elif Bmi < 25:
    print("Normalweight")
else:
    print("Underweight")

"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

#Currency Converter

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