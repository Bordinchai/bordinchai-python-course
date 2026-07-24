weight = float(input("Enter Weight(kg):"))
height = float(input("Enter Height(meter):"))
if height > 0 and weight > 0:

    Bmi = weight / (height ** 2)

    print(round(Bmi,1))

    if Bmi > 30:
        print("Obese")
    elif Bmi > 25:
        print("Overweight")
    elif Bmi > 18.5:
        print("Normalweight")
    elif Bmi > 0:
        print("Underweight")
    else:
        print("Something went wrong about weight or height")
else:
    print("Something went wrong about weight or height")