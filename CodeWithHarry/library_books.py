class Library:
    def __init__(self):
        self.total_books = 0
        self.books ={}
    def show_books(self):
        print("Books: ")
        for book,category in self.books.items():
            print("-", book ,"(category:", category,")")
    def add_book(self, book, category):
        self.books[book] = category
        self.total_books +=1
    def get_total_books(self):
        return self.total_books


#create a library object
library = Library()

#show the initial number of books
print("Initial number of books: ", library.get_total_books())

#add books
while True:
    print("enter a book name (Enter 'q' to quit and get the total info): ")
    book = input()
    if book == 'q':
        break
    print("Enter the category of the book: ")
    category = input()
    library.add_book(book,category)
#show the fnal number of books
print("Final number of books: ", library.get_total_books())

#print all books
library.show_books()
