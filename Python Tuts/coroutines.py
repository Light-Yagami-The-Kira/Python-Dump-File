import time
def searcher():
    time.sleep(4)
    book = "Harry Potter is a very famous character from the series Harry Potter, I like Hermione Granger."

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book.")
        else:
            print("Your text is not in the book.")

search = searcher()
next(search)
search.send("Harry")
search.send("Harrdsafy")
search.close()