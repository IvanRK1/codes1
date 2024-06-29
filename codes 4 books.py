favorite_books = ["Harry Potter", "number one", "New World"]
favorite_books.append("The Hunger Games")
favorite_books[1] = ("Divergent")
favorite_books.pop()
print(favorite_books)

borrowed_books= ["1984", "The Catcher in the Rye","Moby Dick"]
borrowed_books.extend(["Pride and Prejudice", "War and Peace", "Ulysses"])
borrowed_books.remove("The Catcher in the Rye")
third_book = borrowed_books[2]
print(third_book)
print(borrowed_books)