"""
เขียนโปรแกรมตรวจสอบความแข็งแรงของ Password
นิยาม strong password คือ ยาวมากกว่า 8 ตัว, มีอักขระ @ 1 ตัว, มีตัวเลข, มีตัวอักษร

ตัวอย่าง
Insert your password: Boonchoo
Your password is not strong!

Insert your password: Test@123
Your password is strong!
"""

UserPassword = input("Insert your password: ")

has_valid_length = len(UserPassword) >= 8 
has_one_at = UserPassword.count('@') == 1 
has_digit = any(char.isdigit() for char in UserPassword)
has_alpha = any(char.isalpha() for char in UserPassword)

if has_valid_length and has_one_at and has_digit and has_alpha:
    print("Your password is strong!")
else:
    print("Your password is not strong!")