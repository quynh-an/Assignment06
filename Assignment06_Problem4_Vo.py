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
        print(f"Title: {self.title}")
        print(f"Subject: {self.subject}")
        print(f"Location: {self.location}")

    def check_out(self):
        pass
        
    def return_item(self):
        pass
    
class Book(LibraryItem):
    BookinStock = {}
    def __init__(self, title, author, ISBN, subject, quantity, location):
        super().__init__(title, subject, location)
        self.author = author
        self.ISBN = ISBN
        self.quantity = quantity
        Book.BookinStock[self.title] = quantity

        
    def check_out(self):
        if self.title in Book.BookinStock.keys() and Book.BookinStock[self.title] > 0:
            Book.BookinStock[self.title] = Book.BookinStock[self.title] - 1
            print(f"You have checked out {self.title} from the Library.")
        else:
            print(f"{self.title} is not available for checkout.")
    
    def return_item(self):
        if self.title in Book.BookinStock.keys():
            Book.BookinStock[self.title] = Book.BookinStock[self.title] + 1
            print(f"You have returned {self.title} to the Library.")
        else:
            print(f"{self.title} may not belong in this library.")

class DVD(LibraryItem):
    DVDinStock = {}
    def __init__(self, title, director, genre, run_time, subject, location):
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
    JournalinStock = {}
    def __init__(self, title, volume, issue_number, subject, location):
        super().__init__(title, subject, location)
        self.volume = volume
        self.issue_number = issue_number
        Journal.JournalinStock[(self.title, self.volume, self.issue_number)] = self

        
    def check_out(self):
        if (self.title, self.volume, self.issue_number) in Journal.JournalinStock:
            Journal.JournalinStock[(self.title, self.volume, self.issue_number)] = self
            print(f"You have checked out {self.title}, Volume {self.volume}, Issue {self.issue_number}.")
        else:
            print(f"{self.title} (Volume {self.volume}, Issue {self.issue_number}) is not available for checkout.")

        
    def return_item(self):
        Journal.JournalinStock[(self.title, self.volume, self.issue_number)] = self
        print(f"You have returned {self.title} (Volume {self.volume}, Issue {self.issue_number}) to the Library.")

    
class LibraryCatalog():
    catalog = []
    
    def get_details(self):
        print(f"Title: {self.title}")
        print(f"Subject: {self.subject}")
        print(f"Location: {self.location}")
        
    def add_item(self, item):
        LibraryCatalog.catalog.append(item)
    
    def remove_item(self, item):
        if item in LibraryCatalog.catalog:
            LibraryCatalog.catalog.remove(item)
        else:
            print(f"{self.item} is not in the catalog to be removed.")
            
    def find_item_by_title(self, title):
        for book in Book.BookinStock.keys():
            if book.replace(" ", "").lower() == title.replace(" ", "").lower():
                book = eval(title.replace(" ", "").lower())
                book.get_details()
                break
        for dvd, value in DVD.DVDinStock.items():
            if dvd.replace(" ", "").lower() == title.replace(" ", "").lower():
                dvd = eval(title.replace(" ", "").lower())
                dvd.get_details()
                break
        for journal, value in Journal.JournalinStock.items():
            if journal[0].replace(" ", "").lower() == title.replace(" ", "").lower():
                value.get_details()
                break

    def check_out_item(self, title):
        self.add_item(title)
        for book in Book.BookinStock.keys():
            if book.replace(" ", "").lower() == title.replace(" ", "").lower():
                book = eval(title.replace(" ", "").lower())
                book.check_out()
                break
        for dvd, value in DVD.DVDinStock.items():
            if dvd.replace(" ", "").lower() == title.replace(" ", "").lower():
                dvd = eval(title.replace(" ", "").lower())
                dvd.check_out()
                break
        for journal, value in Journal.JournalinStock.items():
            if journal[0].replace(" ", "").lower() == title.replace(" ", "").lower():
                volume = input(f"Which volume of this journal ({title})? ")
                issue = input("Which issue of this volume of the journal? ")
                if journal[1] == int(volume) and journal[2] == int(issue):
                    value.check_out()
                    break
                else:
                    print("We don't have that in our catalog.")
                
    def return_item(self, title):
        for book in Book.BookinStock.keys():
            if book.replace(" ", "").lower() == title.replace(" ", "").lower():
                book = eval(title.replace(" ", "").lower())
                book.return_item()
                break
        for dvd, value in DVD.DVDinStock.items():
            if dvd.replace(" ", "").lower() == title.replace(" ", "").lower():
                dvd = eval(title.replace(" ", "").lower())
                dvd.return_item()
                break
        for journal, value in Journal.JournalinStock.items():
            if journal[0].replace(" ", "").lower() == title.replace(" ", "").lower():
                volume = input(f"Which volume of this journal ({title}) ")
                issue = input("Which issue of this volume of the journal? ")
                if journal[1] == int(volume) and journal[2] == int(issue):
                    value.return_item()
                    break
                else:
                    break
        
# ==========================================
# Create library of Books, DVD, and Movies
littlewomen = Book("Little Women", "Louisa May Alcott", 10000001, "Coming of Age", 3, "Fiction")
animalfarm = Book("Animal Farm", "George Orwell", 10000002, "Political Satire", 4, "Fiction")
barbie = DVD("Barbie", "Greta Gerwig", "Comedy", 155, "Fantasy Comedy", "Movies Shelf 1")
dune = DVD("Dune", "Denis Villeneuve", "Fantasy", 114, "Dystopian Fantasy", "Movies Shelf 1")
bioscience20232 = Journal("BioScience", 2023, 2, "Biology", "Academic Journals")
amjpsych20197 = Journal("American Journal of Psychology", 2019, 7, "Psychology", "Academic Journals")
# ==========================================
def main():
    print("The library currently has these books:")
    print(Book.BookinStock)
    print(" ")
    print("The library currently has these movies:")
    print(DVD.DVDinStock)
    print(" ")
    print("The library currently has these journals. We only hold one of each Journal/Volume/Issue: ")
    journals = []
    for journal in Journal.JournalinStock.keys():
        journals.append(journal)
    print(journals)
    print(" ")
    check_out_or_not = input("Enter the word 'checkout' to initiate a checkout: ")
    if check_out_or_not.replace(" ", "").lower() == "checkout":
    # CHECKING OUT ITEMS
        item_type = input("Enter which you want to check out (book, DVD, or journal): ").lower()
        if item_type == "book":
            book_name = input("Enter the name of the book you want to check out: ")
            for book in Book.BookinStock.keys():
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
        elif item_type == "dvd":
            dvd_name = input("Enter the name of the DVD you want to check out: ")
            for key in DVD.DBVDinStock.keys():
                if key.replace(" ","").lower() == dvd_name.replace(" ", "").lower():
                    dvd = eval(dvd_name)
                    dvd.check_out()
                    break
        elif item_type == "journal":
            journal_name = input("Enter the name of the journal you want to check out: ")
            journal_volume = int(input("Enter the volume (year) of the journal you want to check out: "))
            journal_issue = int(input("Enter the issue of the journal volume you want to check out: "))
            for key, value in Journal.JournalinStock.items():
                if ( 
                    key[0].replace(" ", "").lower() == journal_name.replace(" ", "").lower()
                    and key[1] == int(journal_volume)
                    and key[2] == int(journal_issue)
                ):
                    value.check_out()           
                    break
                else:
                    print(f"{journal_name}, Volume {journal_volume}, Issue {journal_issue} is not available at this library.")
        else:
            print("Item not found in library or cannot be checked out.")
    else:
        print("Thanks for your patronage to this library!")
    
    # RETURNING ITEMS
    return_or_not = input("Enter the word 'return' to initiate a library item return: ")
    if return_or_not.lower() == "return":
        item_type = input("Enter which you want to return (book, DVD, or journal): ").lower()
        if item_type == "book":
            book_name = input("Enter the name of the book you want to return: ")
            for book in Book.BookinStock.keys():
                if book.replace(" ", "").lower() == book_name.replace(" ", "").lower():
                    book = eval(book_name.replace(" ", "").lower())
                    book.return_item()
                    break
                else:
                    print("This item might not be from our library.")
                    break
        elif item_type == "dvd":
            dvd_name = input("Enter the name of the DVD you want to check out: ")
            for dvd in DVD.DVDinStock.keys():
                if dvd.replace(" ", "").lower() == dvd_name.replace(" ", "").lower():
                    print("1")
                    dvd = eval(dvd_name.replace(" ", "").lower())
                    dvd.return_item()
                    break
                else:
                    print("This item might not be from our library.")
                    break
        elif item_type == "journal":
            journal_name = input("Enter the name of the journal you want to check out: ")
            journal_volume = int(input("Enter the volume (year) of the journal you want to check out: "))
            journal_issue = int(input("Enter the issue of the journal volume you want to check out: "))
            for key, value in Journal.JournalinStock.items():
                if ( 
                    key[0].replace(" ", "").lower() == journal_name.replace(" ", "").lower()
                    and key[1] == int(journal_volume)
                    and key[2] == int(journal_issue)
                ):
                    value.return_item()           
                    break
                else:
                    print("We do not hold that journal's volume and issue. No need to return.")
                    break
    else:
        print("Thanks for coming to the library! See you again soon!")    

# ========================================================= 
def catalog_function():
    library = LibraryCatalog()
    search_item = LibraryCatalog()
    print("Adding The Stranger")
    library.add_item("The Stranger")
    print(library.catalog)
    print("Removing The Stranger")
    library.remove_item("The Stranger")
    print(library.catalog)
    search_item.find_item_by_title("Little Women")
    search_item.find_item_by_title("Dune")
    search_item.find_item_by_title("BioScience")
    print(" ")
    to_check_out = LibraryCatalog()
    to_check_out.check_out_item("Animal Farm")
    to_check_out.check_out_item("Barbie")
    to_check_out.check_out_item("American Journal of Psychology")
    print(" ")
    print(Book.BookinStock)
    print(DVD.DVDinStock)
    to_return = LibraryCatalog()
    to_return.return_item("Animal Farm")
    to_return.return_item("Barbie")
    to_return.return_item("American Journal of Psychology")
    print(Book.BookinStock)
    print(DVD.DVDinStock)
    print(Journal.JournalinStock)
    
# ========================================================= 
main()

catalog_function()

