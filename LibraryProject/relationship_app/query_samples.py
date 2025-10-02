
from bookshelf.models import Author, Book, Publisher, Store
from relationship_app.models import Author as RelAuthor, Book as RelBook, Library, Librarian

def list_books_by_author(author_name):
    books = RelBook.objects.filter(author__name=author_name)

    for book in books:
        print(book.title)
        
def list_all_books_in_library(library_name):
   try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(book.title)
   except Library.DoesNotExist:
        print(f"No library found with name {library_name}")
     

def retrieve_librarian_by_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        if library.librarian:
            print(f"Librarian: {library.librarian.name}")
        else:
            print(f"No librarian assigned to the library {library_name}.")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")
        
