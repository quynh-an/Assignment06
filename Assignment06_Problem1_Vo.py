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

class Animal:
    def eat(self):
        print("This animal eats.")
        pass
    
    def sleep(self):
        print("This animal sleeps")
        pass
    
class Mammal(Animal):
    def skincover(self):
        print("Mammals do not have bare skin.")
        
    def eat(self):
        print("I eat many foods.")
        
    def blood():
        print("I am warm-blooded.")
        
class Dog(Mammal):
    def skincover(self):
        print("I have fur.")
        
    def eat(self):
        print("I eat dog food and lots of other human food. But no chocolate!")
        
class Bird(Animal):
    def wings(self):
        print("I have wings.")
        
    def eat(self):
        print("I can be an omnivore, herbivore, or carnivore.")
        
class Penguin(Bird):
    def wings(self):
        print("I have wings but I cannot fly.")
        
    def eat(self):
        print("I eat fish and squids.")
        
class Fish(Animal):
    def gills(self):
        print("I have gills.")
        
    def water(self):
        print("I live in the water.")
        
    def blood(self):
        print("I am cold-blooded.")
        
    def eat(self):
        print
        
class FlyingFish(Fish):
    def water(self):
        print("I can glide out of the water away from predators.")
    
    def tail(self):
        print("I have a forked tail.")

class Reptile(Animal):
    def scales(self):
        print("I have scales all over my body.")
        
    def blood(self):
        print("I am cold-blooded.")

class Snake(Reptile):
    def scales(self):
        print("My scales on my belly are elongated to help me climb.")
    
    def ears(self):
        print("I have no ear holes.")
    
class Amphibian(Animal):
    def skin(self):
        print("I have moist skin.")
    
    def living(self):
        print("I can be in both water and on land.")

class Frog(Amphibian):
    def skin(self):
        print("My skin is slimy, and sometimes, it can be poisonous.")