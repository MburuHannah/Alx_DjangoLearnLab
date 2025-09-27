\# Delete Operation



\# Retrieve the book by its title

book = Book.objects.get(title="Nineteen Eighty-Four")



\# Delete the book from the database

book.delete()



\# Expected Output:

\# (1, {'bookshelf.Book': 1})



(1, {'bookshelf.Book': 1})



\# This confirms that one Book instance was deleted.



\# Try retrieving all books to confirm deletion

books = Book.objects.all()

print(books)



\# Expected Output:

\# <QuerySet \[]>

<QuerySet \[]>



\# This confirms that no Book instances remain in the database.



