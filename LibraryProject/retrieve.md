\# Retrieve Operation

>>> "Fetch the book instance by title"

'Fetch the book instance by title'

>>> #Fetch the book instance by title 

>>> book=Book.objects.get(title ="1984")

>>> print(book.title) #Expected Output is the title 1984

1984

>>> print(book.author) #Expected Output is the authot George Orwell

George Orwell

>>> print(book.publication\_year) #Expected Output is the publication year 1949

1949

