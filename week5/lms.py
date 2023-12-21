

class Book(object):

    def __init__(self,title, author, ISBN, status ):
        assert type(status) == bool
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.status = status

        #impelement method for its availability # display book details

    def status_checker(self):
        if(self.status == True):
            print("Status: Available")

        else:
            self.status = "Status: Not Available"

    def display(self):
        print(f'Book Name: {self.title}  Author: {self.author}  ISBN: {self.ISBN} ')



class User():
    def __init__(self, name, id, books_borrowed):
        self.name = name
        self.id = id
        self.borrowed = books_borrowed
        self.user_info = []
    #show user details, borrowed book, returning date
    def user_details(self):
        print(f"Name: {self.name}, ID: {id}")
    def reg_user(self):
        self.user_info.append([self.name,self.id])
    def return_date(self):
        pass
class Library(Book,User):
    def __init__(self,title, author, ISBN, status):
        super().__init__(title, author, ISBN, status)

        self.books = []
        self.usr_info = []
        #implement methods for adding books to the library, registering users and book transactions


    def add_books(self):
        book = [self.title, self.author, self.ISBN, self.status]
        self.books.append(book)
    def register_user(self, usrinfo):
        self.usr_info.append(usrinfo)
    def displayBooks(self):
        print(self.books)
        print(self.usr_info)

    def book_transactions(self):
        pass
lib1 = Library("lincoln", "JB",1234,True)

lib1.add_books()
lib1.register_user("xander")
lib1.displayBooks()