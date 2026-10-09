"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle():
    def __init__(self, width, length):
        self.__width = width
        self.__length = length
    def getArea(self):
        return f"Area: {self.__width * self.__length}"
    def getPerimeter(self):
        return f"Perimeter: {(self.__width * 2) + (self.__length * 2)}"
    def isSquare(self):
        if self.__width == self.__length:
            return True
        else:
            return False

rec = Rectangle(5, 3)
print(f"{rec.getArea()}\n{rec.getPerimeter()}\n{rec.isSquare()}")
rec2 = Rectangle(5, 5)
print(f"{rec2.getArea()}\n{rec2.getPerimeter()}\n{rec2.isSquare()}") 

"""

Can't use
rec.__width = 20
rec.__length = 30

output:
Error

"""