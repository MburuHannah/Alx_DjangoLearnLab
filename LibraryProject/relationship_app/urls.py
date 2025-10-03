from django.urls import path
from . import views 


urlpatterns=[
    path('',views.home,name='home'),
    path('books/',views.Books,name='books'),
    path('library/<int:pk>/',views.LibraryDetailView.as_view(),name='library-detail'),
    path('register/',views.register,name = 'register')
    
]