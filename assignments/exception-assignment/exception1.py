"""
โจทย์ 1: เครื่องคำนวณอย่างปลอดภัย
เขียนโปรแกรมรับตัวเลข 2 จำนวนและตัวดำเนินการ 1 ตัว ได้แก่ + - * / แล้วแสดงผลลัพธ์
โปรแกรมต้องจัดการกรณีต่อไปนี้
- ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข #ValueError
- ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหนือจาก + - * / raise ValueError
- ผู้ใช้พยายามหารด้วยศูนย์ #ZeroDivisionError
- โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย finally

ตัวอย่างผลลัพธ์ที่คาดหวัง

ตัวเลขที่ 1: 10
ตัวเลขที่ 2: 0
เครื่องหมาย (+, -, *, /): /

ไม่สามารถหารด้วยศูนย์ได้
จบการทำงาน

"""

try:
    first = float(input("ตัวเลขที่ 1: "))
    second = float(input("ตัวเลขที่ 2: "))
    Operator = input("เครื่องหมาย (+, -, *, /): ")
    print(" ")
    if Operator == "+":
        print(first + second)
    elif Operator == "-":
        print(first - second)
    elif Operator == "*":
        print(first * second)
    elif Operator == "/":
        print(first / second)
    else:
        raise ValueError("กรุณากรอก Operator ให้ถูกต้อง (+, -, *, /)")
    
except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง {error} ")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")
finally:
    print("จบการทำงาน")
    print(" ")