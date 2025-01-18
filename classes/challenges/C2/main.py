"""
Library
Wizards are having a hard time keeping track of all the books in their library. They need your help to create a library system that will allow them to add, remove, and search for books.

Magical incantations to find books have unfortunately not been invented yet.

Challenge
You've been tasked with writing the code for the wizard library. Complete the Library and Book classes listed below.

Book Class
__init__(self, title, author)
Set .title and .author to the values of the parameters.
Library Class
__init__(self, name)
Initialize a .name member variable to the value of the name parameter. Create a .books member initialized to an empty list.
add_book(self, book)
Add book, the given Book instance, to the library's books instance variable by appending it to the end of the list.
remove_book(self, book)
If the book's title and author match a library book's title and author, the remove_book method should remove that library book from the list.
search_books(self, search_string)
For every book in the library check if the search_string is contained in the title or author field (case-insensitive). Return a list of all books that match the search string, ordered in the same order as they were added to the library.
After a book is removed, it should no longer be returned in the search results.

Hints
You can use the .lower() method to convert a string to lowercase.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for book_in_books in self.books:
            if book.title.lower() == book_in_books.title.lower() and book.author.lower() == book_in_books.author.lower():
                self.books.remove(book_in_books)

    def search_books(self, search_string):
        books_list = []
        for book in self.books:
            if search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower():
                books_list.append(book)

        return books_list

