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
        
    def area(self, radius):
        area = 3.1415 * radius**2
        return print(f"The area of this circle is {area}")
    
    def perimeter(self, radius):
        circumference = 3.1415 * 2 * radius
        return print(f"The circumference of this circle is {circumference}")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self, length, width):
        area = length * width
        return print(f"The area of this rectangle is {area}")
    
    def perimeter(self, length, width):
        perimeter = length*2 + width*2
        return print(f"The perimeter of this rectangle is {perimeter}")
    
class Triangle(Shape):
    
    
    

        
    
    