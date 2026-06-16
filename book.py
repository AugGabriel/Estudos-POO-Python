# Dunder methods: methods that change the behavior of an object for common operations,
# like adding two objects.

# __init__    : instantiating a class into an object
# __str__     : printing and object or turning it into a string
# __repr__    : representing and object in a string format, but meant for devs
# __eq__      : comparing equality between two objects
# __lt__      : less than, or '<'
# __gt__      : greater than, or '>'
# __add__     : adding two objects
# __contains__: keyword in object, checking if something is in the object
# like if it was an iterable
# __getitem__ : object[key], subscripting and object like a dictionary

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        return f'Book("{self.title}", "{self.author}", {self.num_pages})'
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        in_title = keyword.casefold() in self.title.casefold()
        in_author = keyword.casefold() in self.author.casefold()
        return in_title or in_author
    
    def __getitem__(self, key):
        if key == 'title': return self.title
        if key == 'author': return self.author
        if key == 'num_pages': return self.num_pages
        raise KeyError(f"Book does not contain attribute '{key}'")


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)