class Book:
    def __init__(self,title,author,book_id):
        self.title=title
        self.author=author
        self.book_id=book_id
        self.borrowed=False
   
    def borrow(self):
        if not self.borrowed:
            self.borrowed=True
            return True
        return False
    
    def return_book(self):
        self.borrowed=False

class Printed_books(Book):
        def __init__(self,title,author,book_id,pages):
             super(). __init__(title,author,book_id)
             self.pages=pages


class Ebook(Book):
    def __init__(self,title,author,book_id,file_size):
         super(). __init__(title,author,book_id)
         self.file_size=file_size

class User:
     def __init__(self,name,user_id):
          self.__name= name
          self.user_id=user_id
          self.borrowed_books=[]

     def borrow_book(self, book): 
       if book.borrow():
        self.borrowed_books.append(book)
        print(f"{self.user_id} borrowed {book.title}")  
       else: 
        print(f"{book.title} is already borrowed")  


     def return_book(self,book):
         if book in self.borrowed_books:
             book.return_book()
             self.borrowed_books.remove(book)
             print(f"{self.__name} returned {book.title}")

class Library:
     def __init__(self):
         self.books=[]
         

     def add_book(self,book):
         self.books.append(book)
         print(f"{book.title} is added to the library")

     def remove_book(self,book):
         self.books.remove(book)
         print(f"{book.title} is removed from the library")

     def list_books(self):
        print("Available books")
        for book in self.books:
         status = "Borrowed" if book.borrowed else "Available"
         print(f"{book.book_id}: {book.title} by {book.author} - {status}") 

                 
             
# Example Usage
library = Library()
book1 = Printed_books("Wise And Otherwise", "Sudha Murthy", 1, 248)
book2 = Ebook("MonK Who sold his ferrari", "Robin Sharma", 2, "5MB")

library.add_book(book1)
library.add_book(book2)

user = User("Vaishnavi", 116)
library.list_books()

user.borrow_book(book1)
library.list_books()

user.return_book(book1)
library.list_books()

        