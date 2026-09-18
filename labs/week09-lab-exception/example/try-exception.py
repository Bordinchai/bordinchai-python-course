#ERROR

#ValueError Exception
try:
    age = int(input("กรอกอายุ: "))
    print(f"ปีหน้าคุณอายุ {age + 1} ปี")
except ValueError:
    print("กรุณากรอกอายุเป็นตัวเลขจำนวนเต็ม เช่น 20")

#ZeroDivisionException
try:
    numerator = float(input("กรอกตัวตั้ง: "))
    denominator = float(input("กรอกตัวหาร: "))

    result = numerator / denominator
    print(f"ผลลัพท์ = {result}")
except ZeroDivisionError:
    print(f"ไม่สามารถหารด้วยศูนย์ได้")
except ValueError:
    print(f"กรุณากรอกตัวเลขให้ถูกต้อง")

#FileNotFoundException
try:
    filename = input("ชื่อไฟล์: ")

    with open(filename, "r", encoding = "utf-8") as file:
        content = file.read()

    print("เนื้อหาในไฟล์")
    print(content)
except FileNotFoundError:
    print(f"ไม่พบไฟล์ชื่อ: {filename}")

except PermissionError:
    print(f"ไม่มีสิทธิ์เข้าถึงไฟล์นี้")

#raise ใช้สำหรับ ส่งให้ Python สร้าง exception ขึ้นเอง เมื่อข้อมูลหรือสถานการณ์ไม่เป็นไปตาม
#แม้คำสั่งนั้นจะไม่ผิดไวยกรณ์และ Python ยังทำงานต่อได้ตามปกติก็ตาม

try:
    score = float(input("กรอกคะแนน 0-100: "))

    if not 0 <= score <= 100:
        raise ValueError("คะแนนต้องอยู่ระหว่าง 0 ถึง 100")
    
except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง: {error}")

else:
    print(f"บันทึกคะแนน: {score} เรียบร้อย")

finally:
    print("จบการตรวจสอบคะแนน")


    