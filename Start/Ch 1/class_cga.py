# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOKTYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK','COMICBOOK')

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOKTYPES
    
    # TODO: create a static method
    def getBooklist():  # static methods don't take any inputs, not even 'self'
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        if (not booktype in Book.BOOKTYPES):
            raise ValueError(f'{booktype} is not a valid book type.')
            # raise ValueError(f'{booktype} is not a valid book type. Please use one of the following {Book.BOOKTYPES}')
        else:
            self.booktype = booktype
        self.title = title


# TODO: access the class attribute
print('The available book types are: ',Book.getBookTypes())


# TODO: Create some book instances
b1 = Book('Purity', 'HARDCOVER')
b2 = Book('Saga', 'COMICBOOK')


# TODO: Use the static method to access a singleton object.
# We contain the catalog in the Book class to help ensure only one catalog will exist
bookCatalog = Book.getBooklist()
bookCatalog.append(b1)
bookCatalog.append(b2)

print(bookCatalog)