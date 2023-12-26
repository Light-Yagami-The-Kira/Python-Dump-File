"""
CREATE LIBRARY CLASS
-> PRINT ALL BOOKS
-> LEND BOOK
-> DONATE BOOK
-> RETURN BOOK

HARRY = LIBRARY(LISTOFBOOKS, LIBRARYNAME)

=> DICTIONARY (LEND : OWNER)
"""

class LIBRARY:
    name = None
    listOfBooks = None
    numberOfBooks = None
    len_dic = {}

    def __init__(self,LIBRARYNAME, LISTOFBOOKS):
        self.name = LIBRARYNAME
        self.listOfBooks = list(LISTOFBOOKS)
        self.numberOfBooks = len(self.listOfBooks)

    @property
    def books(self):
        return ",".join(self.listOfBooks)
    
    def lend_book(self):
        n = input("Enter name of the person: ")
        t = input("Which books you wanna lend (bookA,bookB,...): ")
        t = t.split(',')
        for item in t:
            if item not in self.listOfBooks:
                print(f"{item} is not availabe, so it will be skipped.")
                t.remove(item)
            else:
                self.listOfBooks.remove(item)
        self.len_dic= dict.fromkeys(t,n)
        self.numberOfBooks -= len(t)

Krishanu = LIBRARY("Harry Potter Series", ['Season1', 'Season2', 'Season3', 'Season4'])
print(Krishanu.books)
print(Krishanu.numberOfBooks)
Krishanu.lend_book()
print(Krishanu.books)
print(Krishanu.numberOfBooks)

