from django.shortcuts import render,redirect
from .models import Book
from django.views.generic import ListView
from .models import Book, Author, Library, Librarian
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def home(request):
    return render(request, 'relationship/home.html')

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
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html' , {'form' :form})

