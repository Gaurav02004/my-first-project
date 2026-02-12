# class Library:
#   def__init__(self):
#     self.noBooks = noBooks = 0
#     self.Books = []

# def addBook(self, book):
#     self.books.append(book) 
#     self.noBooks = self.Books.length

# def showInfo(self):
#     print(f"The Library has {self.noBooks} books")

# for book in self.books:
#     print(book)

# l1 = Library()
# l1.addbook("Gaurav potter1")





class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.noBooks} books")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBook("Gaurav Potter 1")
l1.addBook("Gaurav Potter 2")

l1.showInfo()
