from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.price = price
        super().__init__(title, author)

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")


book_title = input("Enter the book's title: ")
book_author = input("Enter the book's author: ")
book_price = int(input("Enter the book's price: "))
new_novel = MyBook(book_title, book_author, book_price)
new_novel.display()
