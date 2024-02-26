class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability_status = True

    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Available: {self.availability_status}"

    def update_availability(self, status):
        self.availability_status = status

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Books Borrowed: {', '.join([book.title for book in self.books_borrowed])}"

    def borrow_book(self, book):
        if book.availability_status:
            self.books_borrowed.append(book)
            book.update_availability(False)

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.update_availability(True)

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def handle_transaction(self, transaction):
        pass

class Transaction:
    def __init__(self, user, book, transaction_type):
        self.user = user
        self.book = book
        self.transaction_type = transaction_type

    def execute(self):
        if self.transaction_type == 'borrow':
            self.user.borrow_book(self.book)
        elif self.transaction_type == 'return':
            self.user.return_book(self.book)

    def generate_report(self):
        return f"User: {self.user.name}, Book: {self.book.title}, Transaction Type: {self.transaction_type}"
        transaction.execute()
        book.update_availability(True)

def main():
    library = Library()

    while True:
        print("1. Add Book")
        print("2. Register User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            ISBN = input("Enter book ISBN: ")
            book = Book(title, author, ISBN)
            library.add_book(book)

        elif choice == 2:
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            user = User(user_id, name)
            library.register_user(user)

        elif choice == 3:
            user_id = input("Enter user ID: ")
            ISBN = input("Enter book ISBN: ")
            user = next((user for user in library.users if user.user_id == user_id), None)
            book = next((book for book in library.books if book.ISBN == ISBN), None)
            if user and book:
                transaction = Transaction(user, book, 'borrow')
                library.handle_transaction(transaction)

        elif choice == 4:
            user_id = input("Enter user ID: ")
            ISBN = input("Enter book ISBN: ")
            user = next((user for user in library.users if user.user_id == user_id), None)
            book = next((book for book in library.books if book.ISBN == ISBN), None)
            if user and book:
                transaction = Transaction(user, book, 'return')
                library.handle_transaction(transaction)

        elif choice == 5:
            break

if __name__ == "__main__":
    main()
