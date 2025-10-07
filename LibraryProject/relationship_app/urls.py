from django.urls import path
from . import views 
from .views  import admin_view, librarian_view, member_view,add_book, edit_book, delete_book


urlpatterns=[
    path('',views.home,name='home'),
    path('books/',views.Books,name='books'),
    path('library/<int:pk>/',views.LibraryDetailView.as_view(),name='library-detail'),
    path('register/',views.register,name = 'register'),
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),    
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
    path('searchbooks/', views.search_books, name='search_books'),
    path('secure/', views.secure_view, name='secure_view'),
    
    
    
]