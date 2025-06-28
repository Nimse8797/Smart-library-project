
# 📚 Library Management System (OOP-Based in Python)

This is a simple object-oriented Python project that simulates a **Library Management System**. It allows managing **printed books** and **ebooks**, borrowing/returning books, and tracking users and their borrowed books.

---

## 🚀 Features

- Add and remove books from the library  
- Different types of books: `Printed_books` and `Ebook`  
- Borrow and return functionality with proper status tracking  
- User class to track borrowing activity  
- Display all available and borrowed books

---

 📁 Classes Overview

### `Book` (Base Class)
- **Attributes**: `title`, `author`, `book_id`, `borrowed`
- **Methods**: 
  - `borrow()`: Marks the book as borrowed if not already.
  - `return_book()`: Returns the book.

### `Printed_books` (Inherits from `Book`)
- Additional Attribute: `pages`

### `Ebook` (Inherits from `Book`)
- Additional Attribute: `file_size`

### `User`
- Attributes: `name`, `user_id`, `borrowed_books`  
- Methods:
  - `borrow_book(book)`: Borrows a book if available.
  - `return_book(book)`: Returns the book if it was borrowed by the user.

### `Library`
- Attributes: `books` (list of all books in the library)  
- Methods:
  - `add_book(book)`: Adds a new book to the library.
  - `remove_book(book)`: Removes a book from the library.
  - `list_books()`: Lists all books with their status (Available/Borrowed)

---
🧪 Example Usage

```python
library = Library()

book1 = Printed_books("Wise And Otherwise", "Sudha Murthy", 1, 248)
book2 = Ebook("Monk Who Sold His Ferrari", "Robin Sharma", 2, "5MB")

library.add_book(book1)
library.add_book(book2)

user = User("Vaishnavi", 116)

library.list_books()

user.borrow_book(book1)
library.list_books()

user.return_book(book1)
library.list_books()
```

---
✅ Output Preview

```
Wise And Otherwise is added to the library
MonK Who sold his ferrari is added to the library
Available books
1: Wise And Otherwise by Sudha Murthy - Available
2: MonK Who sold his ferrari by Robin Sharma - Available
116 borrowed Wise And Otherwise
Available books
1: Wise And Otherwise by Sudha Murthy - Borrowed
2: MonK Who sold his ferrari by Robin Sharma - Available
Vaishnavi returned Wise And Otherwise
Available books
1: Wise And Otherwise by Sudha Murthy - Available
2: MonK Who sold his ferrari by Robin Sharma - Available
```

---

💡 How to Run

1. Make sure you have Python installed (`>=3.x`)
2. Copy the code into a `.py` file (e.g., `library_system.py`)
3. Run it using your terminal or any Python IDE:

```bash
python library_system.py
```

---

📌 Future Enhancements

- Add a `search_book()` method by title or author
- Implement due dates or borrowing limits
- Store library and user data in files or databases
- Build a GUI using Tkinter or a web interface using Flask/Django
