#Circle Calculator
"""
Pi = 3.14159

radius = float(input("Enter radius:"))

area = Pi * radius ** 2
circumference = 2 * Pi * radius
print("Area:",area,"\nCircumference:",circumference)
"""
#Time Converter
"""
second_input = int(input("Enter second: "))
hour = int(second_input / 3600)
minute = int((second_input % 3600) / 60)
second = int(second_input % 60)

print(hour, "hour", minute, "minute", second, "second")
"""
#Compound Interest Calculator
"""
P = float(input("Enter principal:"))
r = float(input("Enter rate:"))
t = float(input("Enter time:"))
A = P * (1 + r/100) ** t
print("Future Value:",A)
"""
#BMI Calculator
#find in quiz
#Grade Average
"""
Score = [int(input("Enter score test1:")),
         int(input("Enter score test2:")),
         int(input("Enter score test3:"))]
Average = (Score[0] + Score[1] + Score[2])/3
print("Average Scores:",round(Average,2))
"""