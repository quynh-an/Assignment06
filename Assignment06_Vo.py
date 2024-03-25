#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:25:04 2024

@author: tandyllc
"""

# Library Management System
# Create class LibraryItem as parent class
# Initialize with title, subject, location in library
# Create methods check_out() and return_item() and get_details()
# Book is a child class
# DVD is a child class
# Journal is a child class
# Library Catalog will be a class with all of them with the methods add_item, remove_item, find_item_by_title, check_out, and return_item

class LibraryItem:
    def __init__(self, title, subject, location):
        self.title = title
        self.subject = subject
        self.location = location
        
    def get_details(self):
        print(f"{self}:")
        print(f"Title: {self.title}")
        print(f"Subject: {self.subject}")
        print(f"Location: {self.location}")

    def check_out(self):
        pass
        
    def return_item(self):
        pass
    
class Book(LibraryItem):
    inStock = []
    def __init__(self, title, author, ISBN, subject, location):
        super().__init__(title, subject, location)
        self.author = author
        self.ISBN = ISBN
        Book.inStock.append(self.title)

        
    def check_out(self):
        if self.title in Book.inStock:
            Book.inStock.remove(self.title)
            print(f"You have checked out {self.title} from the Library.")
        else:
            print(f"{self.title} is not available for checkout.")
    
    def return_item(self):
        if self.title not in Book.inStock:
            Book.inStock.append(self.title)
            print(f"You have returned {self.title} to the Library.")
        else:
            print(f"{self.title} is already in stock.")
            
    def print_in_stock(cls):
        print("Books in stock:")
        for book in cls.inStock:
            print(book.title)

class DVD(LibraryItem):
    inStock = []
    def __init__(self, title, subject, location):
        super().__init__(title, subject, location)
        self.inStock.append(self.title)
        
class Journal(LibraryItem):
    inStock = []
    def __init__(self, title, subject, location):
        super().__init__(title, subject, location)
        self.inStock.append(self.title)
    
# ==========================================
def main():
    LittleWomen = Book("Little Women", "Louisa May Alcott", 10000001, "Coming of Age", "Fiction")
    LittleWomen.check_out()
    LittleWomen.return_item()
    
main()