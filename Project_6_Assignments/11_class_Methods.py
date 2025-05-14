# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

# Hint: Use the @classmethod decorator to mark the method as a class method.

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")

book1 = Book()
book2 = Book()

Book.increment_book_count()

book3 = Book()
Book.increment_book_count()

# Output:
# Total books: 2
# Total books: 3