#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:38:15 2024

@author: tandyllc
"""

#Question 1: Animal Kingdom Hierarchy
#Create a class hierarchy representing animals in a kingdom. Start with a base class Animal that has
#methods like eat() and sleep(). Derive classes such as Mammal, Bird, Fish, etc. from the Animal class.
#Further derive specific animal classes like Dog, Cat, Eagle, etc., which override base class methods to
#perform actions specific to that animal. Demonstrate polymorphism by writing a function that takes an
#Animal object and calls its eat() method, regardless of the subclass from which it is instantiated