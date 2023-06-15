'''
Write a Library class with no_of_books and books 
as two instance variables. Write a program to create a 
library from this Library class and show how you can print all books,
 add a book and get the number of books using different methods. 
 Show that your program doesnt persist the books after the program is stopped!'''

from typing import Any


class Library:
    '''This class creates the instance that hold book names and number of books names its holding'''
    def __init__(self) -> None:
        self.no_of_books = 0
        self.books = []

    @property
    def get_no_of_books(self):
        return self.no_of_books

    @property    
    def get_books(self):
        return self.books

    @get_no_of_books.setter
    def set_no_of_books(self,n):
        self.no_of_books += n
    
    @get_books.setter
    def set_book(self,books=[]):
        if len(books) == 0:
            pass
        else:
            self.books.extend(i for i in books)
            self.set_no_of_books = len(books)
        print(self.books)

    @staticmethod
    def add_book():
        global lst
        global choise
        while choise == "Y":
            bn = input("\nEnter book name : ").capitalize()
            
            lst.append(bn)
            choise = input("\n Do you want to add a book: ").upper()

    def __call__(cls):
        print(help(cls))


    

if __name__ == '__main__':
    lib = Library()
    lib()
    
    lst =[]
    
    choise = input("\n Do you want to add a book: ").upper()
    Library.add_book()

    lib.set_book = lst
    lst.clear()
    print("\nBooks in library are : ", lib.get_books)
    print(f"Number of books in Library are : {lib.get_no_of_books}")
    print(f"Number of books in Library are : {len(lib.get_books)}")
    if len(lib.get_books) == lib.get_no_of_books:
        print("All books are accounted")
    else:
        print("Some books are missing")
    
    choise = input("\n Do you want to add a book: ").upper()
    Library.add_book()

    lib.set_book = lst
    print("\nBooks in library are : ", lib.get_books)
    print(f"Number of books in Library are : {lib.get_no_of_books}")
    print(f"Number of books in Library are : {len(lib.get_books)}")
    if len(lib.get_books) == lib.get_no_of_books:
        print("All books are accounted")
    else:
        print("Some books are missing")