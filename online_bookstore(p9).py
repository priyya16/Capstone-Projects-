import sqlite3
import os

# Database Initialization
DB_FILE = "bookstore.db"

def initialize_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        genre TEXT NOT NULL,
                        price REAL NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_name TEXT NOT NULL,
                        books_ordered TEXT NOT NULL,
                        total_price REAL NOT NULL)''')

    conn.commit()
    conn.close()

# Book Management
def add_book():
    try:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        price = float(input("Enter book price: "))

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, genre, price) VALUES (?, ?, ?, ?)", 
                       (title, author, genre, price))
        conn.commit()
        conn.close()
        print("Book added successfully!")
    except Exception as e:
        print("Error:", e)

def view_books():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()

    if books:
        print("\nAvailable Books:")
        for book in books:
            print(f"{book[0]}. {book[1]} by {book[2]} [{book[3]}] - ${book[4]}")
    else:
        print("No books available.")

# Order Management
def place_order():
    view_books()
    customer_name = input("Enter your name: ")
    book_ids = input("Enter book IDs to order (comma-separated): ").split(',')

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    ordered_books = []
    total_price = 0

    for book_id in book_ids:
        cursor.execute("SELECT title, price FROM books WHERE id=?", (book_id.strip(),))
        book = cursor.fetchone()
        if book:
            ordered_books.append(book[0])
            total_price += book[1]

    if ordered_books:
        cursor.execute("INSERT INTO orders (customer_name, books_ordered, total_price) VALUES (?, ?, ?)", 
                       (customer_name, ", ".join(ordered_books), total_price))
        conn.commit()
        print(f"Order placed successfully! Total Bill: ${total_price:.2f}")
    else:
        print("Invalid book selection.")

    conn.close()

def view_orders():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()

    if orders:
        print("\nOrder History:")
        for order in orders:
            print(f"Order {order[0]} - {order[1]}: {order[2]} | Total: ${order[3]:.2f}")
    else:
        print("No orders found.")

def total_revenue():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(total_price) FROM orders")
    revenue = cursor.fetchone()[0] or 0
    conn.close()
    print(f"\nTotal Revenue: ${revenue:.2f}")

# File Handling
def export_data():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        with open("books.txt", "w") as f:
            cursor.execute("SELECT * FROM books")
            for book in cursor.fetchall():
                f.write(f"{book[0]},{book[1]},{book[2]},{book[3]},{book[4]}\n")

        with open("orders.txt", "w") as f:
            cursor.execute("SELECT * FROM orders")
            for order in cursor.fetchall():
                f.write(f"{order[0]},{order[1]},{order[2]},{order[3]}\n")

        conn.close()
        print("Data exported successfully!")
    except Exception as e:
        print("Error:", e)

def import_data():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        if os.path.exists("books.txt"):
            with open("books.txt", "r") as f:
                for line in f:
                    data = line.strip().split(',')
                    cursor.execute("INSERT INTO books (id, title, author, genre, price) VALUES (?, ?, ?, ?, ?)", 
                                   (int(data[0]), data[1], data[2], data[3], float(data[4])))

        if os.path.exists("orders.txt"):
            with open("orders.txt", "r") as f:
                for line in f:
                    data = line.strip().split(',')
                    cursor.execute("INSERT INTO orders (id, customer_name, books_ordered, total_price) VALUES (?, ?, ?, ?)", 
                                   (int(data[0]), data[1], data[2], float(data[3])))

        conn.commit()
        conn.close()
        print("Data imported successfully!")
    except Exception as e:
        print("Error:", e)

# Interactive Menu
def main():
    initialize_db()
    while True:
        print("\n=== Online Bookstore System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Place Order")
        print("4. View Orders")
        print("5. View Total Revenue")
        print("6. Export Data")
        print("7. Import Data")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            place_order()
        elif choice == '4':
            view_orders()
        elif choice == '5':
            total_revenue()
        elif choice == '6':
            export_data()
        elif choice == '7':
            import_data()
        elif choice == '8':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
