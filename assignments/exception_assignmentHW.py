def deposit(money):
    if money <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    else:
        global Balance
        Balance += money
        return Balance

try:
    Balance = 1000.00
    print(f"\nยอดเงินเริ่มต้น: {Balance} บาท")
    Deposit = float(input("กรอกจำนวนเงินที่ต้องการฝาก: "))
    deposit(Deposit)
    print(f"\nฝากเงินสำเร็จ")
    print(f"ยอดเงินคงเหลือ: {Balance} บาท")
except ValueError as error:
    print(f"\nเกิดข้อผิดพลาด: {error}")
finally:
    print("สิ้นสุดการฝากเงิน\n")