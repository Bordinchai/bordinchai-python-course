
"""
1.รับค่าtext จากผู้ใช้งาน
2.รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
3.แสดงผลจำนวนของอักขระในข้อความ text
"""

"""
ตัวอย่างหน้าจอ
Insert your text: Boonchoo Jitnupong
Character to find: o
5 letters 'o' found in 'Boonchoo Jitnupong'
"""

print("\n=== ITERATING THROUGH STRING ===")
UserText = input("Insert your text: ")
Letter = input("Character to find: ")

count = 0
for letter in UserText:
    if letter == Letter:
        count += 1
print(f"{count} letters '{Letter}' found in '{UserText}'")

