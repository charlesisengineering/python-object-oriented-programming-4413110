# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price) # periodicals should leverage the code already implemented by the publication base class
        self.period = period
        self.publisher = publisher


class Book(Publication): # add Publication class in parentheses to inherit it 
    def __init__(self, title, author, pages, price):
        super().__init__(title, price) # super to reference a method of the parent class
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher) # TODO add type safety


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher) # TODO add type safety


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
