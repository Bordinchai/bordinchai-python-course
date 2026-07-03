#Circle Calculate

import math

radius = float(input("Enter radius: "))

Area = math.pi * pow(radius,2)
Circumference = 2 * math.pi * radius
print("Area:",Area,
      "\nCircumference:",Circumference)

#Time Coverter

total_second = int(input("Enter total seconds: "))

hour = total_second // 3600
minute = int((total_second % 3600) / 60)
second = (total_second % 60)

print(hour,"hours",
      minute,"minutes",
      second,"seconds")

#Shopping Calculator

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

subtotal = item_price * quantity
discount_amount = (discount_percent/100) * subtotal
price = subtotal - discount_amount
tax = price * (tax_percent/100)
total = price + tax
print("Final Total: ", total)
