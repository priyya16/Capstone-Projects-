import random

class Book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def get_price(self):
        return self.price

class EBook(Book):
    def __init__(self, title, author, genre, price, file_size):
        super().__init__(title, author, genre, price)
        self.file_size = file_size

    def get_price(self):
        return self.price * 0.9  # 10% discount for e-books

class PrintedBook(Book):
    def __init__(self, title, author, genre, price, pages):
        super().__init__(title, author, genre, price)
        self.pages = pages

class Order:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__ordered_books = []
        self.__total_bill = 0

    def add_book(self, book):
        self.__ordered_books.append(book)
        self.__total_bill += book.get_price()

    def get_total_bill(self):
        return self.__total_bill

    def display_order(self):
        print(f"\nOrder Summary for {self.__customer_name}:")
        for book in self.__ordered_books:
            print(f"{book.title} by {book.author} - Rs.{book.get_price()}")
        print(f"Total Bill: Rs.{self.__total_bill}")

class Bookstore:
    def __init__(self):
        self.books = []
        self.orders = []
        self.total_revenue = 0

    def add_book(self, book):
        self.books.append(book)

    def display_catalog(self):
        print("\nBook Catalog:")
        for index, book in enumerate(self.books, 1):
            print(f"{index}. {book.title} by {book.author} - Rs.{book.get_price()} ({book.genre})")

    def place_order(self):
        customer_name = input("\nEnter your name: ")
        order = Order(customer_name)
        self.display_catalog()

        while True:
            choice = input("\nEnter book number to order (or type 'done' to finish): ")
            if choice.lower() == 'done':
                break
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.books):
                    order.add_book(self.books[index])
                else:
                    print("Invalid selection. Try again.")
            except ValueError:
                print("Invalid input. Enter a valid book number.")

        if order.get_total_bill() > 0:
            self.orders.append(order)
            self.total_revenue += order.get_total_bill()
            order.display_order()

    def view_total_revenue(self):
        print(f"\nTotal Revenue: Rs.{self.total_revenue}")

bookstore = Bookstore()
bookstore.add_book(PrintedBook("The Alchemist", "Paulo Coelho", "Fiction", 300, 208))
bookstore.add_book(EBook("Python Crash Course", "Eric Matthes", "Programming", 500, "5MB"))
bookstore.add_book(PrintedBook("Rich Dad Poor Dad", "Robert Kiyosaki", "Finance", 350, 336))
bookstore.add_book(EBook("The Power of Habit", "Charles Duhigg", "Self-Help", 450, "3MB"))

while True:
    print("\n1. View Book Catalog\n2. Place Order\n3. View Total Revenue\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        bookstore.display_catalog()
    elif choice == "2":
        bookstore.place_order()
    elif choice == "3":
        bookstore.view_total_revenue()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
