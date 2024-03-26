#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:38:15 2024

@author: tandyllc
"""

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
        
    def sleep(self):
        print("I sleep in the nighttime.")
        
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
        
    def sleep(self):
        print("I sometimes just take naps throughout the day.")
        
class Fish(Animal):
    def gills(self):
        print("I have gills.")
        
    def water(self):
        print("I live in the water.")
        
    def blood(self):
        print("I am cold-blooded.")
        
    def eat(self):
        print("I eat plankton, algae, and more")
        
class FlyingFish(Fish):
    def water(self):
        print("I can glide out of the water away from predators.")
    
    def tail(self):
        print("I have a forked tail.")
    
    def eat(self):
        print("I eat plankton and small crustaceans.")

class Reptile(Animal):
    def scales(self):
        print("I have scales all over my body.")
        
    def blood(self):
        print("I am cold-blooded.")
    
    def eat(self):
        print("I eat a lot of things from insects and frogs to fishes and other reptiles.")

class Snake(Reptile):
    def scales(self):
        print("My scales on my belly are elongated to help me climb.")
    
    def ears(self):
        print("I have no ear holes.")
        
    def eat(self):
        print("I eat birds, lizards, rats, squirrels, and more.")
    
    def sleep(self):
        print("I sleep during the night and day.")
    
class Amphibian(Animal):
    def skin(self):
        print("I have moist skin.")
    
    def living(self):
        print("I can be in both water and on land.")
    
    def eat(self):
        print("I can eat bugs, slugs, snails, and so many more.")

class Frog(Amphibian):
    def skin(self):
        print("My skin is slimy, and sometimes, it can be poisonous.")
    
    def eat(self):
        print("I eat flies, moths, slugs, worms, and more!")
        
    def sleep(self):
        print("I sleep during the night usually.")

# =======================================
# Calling methods

treefrog = Frog()
treefrog.eat()
treefrog.sleep()

boa = Snake()
boa.eat()
boa.sleep()
boa.ears()

bobby = FlyingFish()
bobby.water()
bobby.eat()

spot = Dog()
spot.eat()
spot.sleep()
spot.skincover()

happyfeet = Penguin()
happyfeet.wings()
happyfeet.eat()
happyfeet.sleep()
