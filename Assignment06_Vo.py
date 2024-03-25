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
    BookinStock = []
    def __init__(self, title, author, ISBN, subject, location):
        super().__init__(title, subject, location)
        self.author = author
        self.ISBN = ISBN
        Book.BookinStock.append(self.title)

        
    def check_out(self):
        if self.title in Book.BookinStock:
            Book.BookinStock.remove(self.title)
            print(f"You have checked out {self.title} from the Library.")
        else:
            print(f"{self.title} is not available for checkout.")
    
    def return_item(self):
        if self.title not in Book.BookinStock:
            Book.BookinStock.append(self.title)
            print(f"You have returned {self.title} to the Library.")
        else:
            print(f"{self.title} is already in stock.")

class DVD(LibraryItem):
    DVDinStock = {}
    def __init__(self, title, director, genre, subject, location):
        super().__init__(title, subject, location)
        self. director = director
        self.genre = genre
        if self.title not in DVD.DVDinStock.keys():
            DVD.DVDinStock.update({self.title:1})
        else:
            num_movies = DVD.DVDinStock.get(self.title) + 1
            DVD.DVDinStock.setdefault(self.title, num_movies)
    
    def check_out(self):
        if self.title in DVD.DVDinStock.keys():
            num_movies = DVD.DVDinStock.get(self.title) - 1
            DVD.DVDinStock.update({self.title:num_movies})
            print(f"You have checked out {self.title} from the Library. Please make sure you return the DVD with its case.")
        else:
            print(f"{self.title} is not held by this library for checkout.")
    
    def return_item(self):
        num_movies = DVD.DVDinStock.get(self.title) + 1
        DVD.DVDinStock.update({self.title:num_movies})
        print(f"{self.title} has been returned to the library movie collection.")
        
class Journal(LibraryItem):
    JournalinStock = []
    def __init__(self, title, volume, issue_number, subject, location):
        super().__init__(title, subject, location)
        self.volume = volume
        self.issue_number = issue_number
        self.JournalinStock.append(list(self.title, self.volume, self.issue_number))
    
   # def check_out(self):
        
# ==========================================
# Create library of Books, DVD, and Movies
littlewomen = Book("Little Women", "Louisa May Alcott", 10000001, "Coming of Age", "Fiction")
    
# ==========================================
def main():
    print(Book.BookinStock)
    item_type = input("Enter which you want to check out (book, DVD, or journal): ").lower()
    book_name = input("Enter the name of the book you want to check out: ")
    if item_type == "book":
        for book in Book.BookinStock:
            if book.lower() == book_name.lower():
                book = eval(book_name.replace(" ", "").lower())
                book.check_out()
                break
            if book.replace(" ", "").lower() == book_name.lower():
                book = eval(book_name.replace(" ", "").lower())
                book.check_out()
                break
            else:
                print("The library does not hold a book by that name.")
    else:
        print("Book not found or cannot be checked out.")
    
    
    # Book methods
    #LittleWomen = Book("Little Women", "Louisa May Alcott", 10000001, "Coming of Age", "Fiction")
    #LittleWomen.check_out()
   # LittleWomen.return_item()
    
    # DVD methods
   # Barbie = DVD("Barbie", "Greta Gerwig", "Comedy", "Fantasy Comedy", "Movies Shelf 1")
   # print(DVD.DVDinStock)
   # Barbie.check_out()
   # print(DVD.DVDinStock)
   # Barbie.return_item()
   # print(DVD.DVDinStock)
   # Dune.check_out()
    
    # Journal Methods
    
main()