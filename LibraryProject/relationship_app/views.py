from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
from .models import Book, Author, Library, Librarian
from django.views.generic.detail import DetailView



# Create your views here.

def Books(request):
    books=Book.objects.all()
    return render(request, 'relationship/books.html' ,{'books':books})

class LibraryDetailView(DetailView):
    model=Library
    template_name='relationship/library_detail.html'
    context_object_name='library'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        library=self.get_object()
        context['books']=self.object.books.all()
        return context
    
    