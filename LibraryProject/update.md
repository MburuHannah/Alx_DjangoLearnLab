\# Update Operation



\# Retrieve the book by its current title

book = Book.objects.get(title="1984")



\# Update the title

book.title = "Nineteen Eighty-Four"



\# Save the changes to the database

book.save()



\# Confirm the update

print(book.title)  # Expected Output: Nineteen Eighty-Four

Nineteen Eighty-Four

