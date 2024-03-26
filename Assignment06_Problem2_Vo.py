#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:35:54 2024

@author: tandyllc
"""

"""
Design a base class called Shape with methods area() and perimeter() which will be overridden by
derived classes Circle, Rectangle, and Triangle. Each subclass should have attributes specific to the
details required to calculate the area and perimeter. Create a list of shapes and iterate over it, printing out
the area and perimeter of each shape, demonstrating polymorphism.
"""

class Shape():
    def __init__(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        area = 3.1415 * self.radius**2
        return print(f"The area of this circle is {area}")
    
    def perimeter(self):
        circumference = 3.1415 * 2 * self.radius
        return print(f"The circumference of this circle is {circumference}")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length * self.width
        return print(f"The area of this rectangle is {area}")
    
    def perimeter(self):
        perimeter = self.length*2 + self.width*2
        return print(f"The perimeter of this rectangle is {perimeter}")
    
class Triangle(Shape):
    def __init__(self):
        pass
    
    def area(self, base, perpendicular):
        if base > 0 and perpendicular > 0:
            try:
                area = 0.5 * float(base) * float(perpendicular)
            except:
                 print("Invalid inputs for triangle")   
            return print(f"The area of this triange is {area}")
        else:
            print("Invalid input for triangle.")
    
    def perimeter(self, side1, side2, side3):
        perimeter = side1 + side2 + side3
        return print(f"The perimeter of this triangle is {perimeter}")

# =============================================
def main():
    triangle1 = Triangle()
    rectangle1 = Rectangle(4, 9)
    circle1 = Circle(4)
    
    triangle1.area(3, 8)
    triangle1.perimeter(3, 4, 5)
    circle1.perimeter()
    circle1.area()
    rectangle1.area()
    rectangle1.perimeter()
 
# =============================================
main()

    
    

        
    
    