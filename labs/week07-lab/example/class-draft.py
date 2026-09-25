"""
2 type of programing

1) structured programming ==> การเขียนโปรแกรมเชิงโครงสร้าง > c, js, python
2) Object-oriented programming (OOP) ==> การเขียนโปรแกรมเชิงวัตถุ > java, c#, python
"""

# วิธีแก้ปัญหา เป็นแค่แนวทาง template แม่แบบ

# วิธีการแก้ปัญหา
class ClassName:
    """Class docstring"""

    #ข้อมูลอะไรบ้างที่ต้องใช้แก้ปัญหา
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value

    #การกระทำ ==> method
    def method_name(self):
        # Instance method
        return something

    def method_name2(self):
        pass

# การสร้างวัตถุจากคลาส ==> เอาคลาสมาใช้
myObj = ClassName(parameters)

# ใช้งานวัตถุจากคลาส
print(myObj.attribute)
resultFromMethod = myObj.method_name()
myObj.method_name2()

myObj2 = ClassName(parameters)
print(myObj2.attribute)
print(myObj2.method_name())
myObj2.method_name2()