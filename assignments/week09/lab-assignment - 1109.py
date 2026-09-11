def calculate_unit(unit):
    t1 = t2 = t3 = t4 = total = 0.00
    if unit > 200:
        t1 += (unit-200)*4.00
        unit = 200
    if unit > 100:
        t2 += (unit-100)*3.50
        unit = 100
    if unit > 50:
        t3 += (unit-50)*3.00
        unit = 50
    if unit > 0:
        t4 += unit*2.50
    total = t1 + t2 + t3 + t4
    if t4 > 0:
        print(f"\n1-50 หน่วย: {t4:.2f} บาท")
    if t3 > 0:
        print(f"51-100 หน่วย: {t3:.2f} บาท")
    if t2 > 0:
        print(f"101-200 หน่วย: {t2:.2f} บาท")
    if t1 > 0:
        print(f">200 หน่วย: {t1:.2f} บาท")
    return total

while True:
    print(f"{'='*4} โปรแกรมคำนวณค่าไฟฟ้า {'='*4}")
    print('1. คำนวณค่าไฟ')
    print('2. ออกจากโปรแกรม')
    choice = int(input("เลือกเมนู: "))
    if choice == 1:
        while True:
            unit = int(input("\nกรอกจำนวนหน่วยไฟฟ้า: "))
            if unit >= 0:
                break
        cost = calculate_unit(unit) + 25.00
        print(f"ค่าบริการ: 25.00 บาท")
        print(f"รวมค่าไฟทั้งสิ้น: {cost} บาท")
    elif choice == 2:
        break
    else: print("Error please choose again")
