# Create Operation

# new Book instance
Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Expected Output:
# <Book: Book object (1)>
<Book: Book object (1)>


# This confirms that the book was successfully created and assigned a primary key of 1.
