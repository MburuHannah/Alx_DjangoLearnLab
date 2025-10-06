from django.shortcuts import render,redirect
from .models import Book
from django.views.generic import ListView
from .models import Book, Author, Library, Librarian
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test,permission_required
from .models import UserProfile
from .forms import BookForm,CustomUserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book



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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request,'relationship/register.html' , {'form' :form})
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'    

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship/admin_view.html')

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship/librarian_view.html')  

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'member'    
@user_passes_test(is_member)            

def member_view(request):
    return render(request, 'relationship/member_view.html')


@permission_required('relationship_app.add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()   
    return render(request, 'relationship/book_form.html', {'form': form})    

@permission_required('relationship_app.edit_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})
@permission_required('relationship_app.delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'books/delete_book.html', {'book': book})

@permission_required('relationship_app.view_book')
def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship/view_book.html', {'book': book})

@permission_required('relationship_app.create_book')
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'relationship/book_form.html', {'form': form})

   
