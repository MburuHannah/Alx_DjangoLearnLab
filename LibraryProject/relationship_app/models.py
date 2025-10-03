from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    class Meta:
        permission=[
            ('can_add_book','Can add book'),
            ('can_change_book','Can change book'),
            ('can_delete_book','Can delete book'),  
        ]
    def __str__(self):
        return self.title   
    
class Library(models.Model):
    name=models.CharField(max_length=100)
    books=models.ManyToManyField(Book,related_name='libraries')
    
class Librarian(models.Model):
    name=models.CharField(max_length=100)
    library=models.OneToOneField(Library, related_name='librarian', on_delete=models.CASCADE)

class UserProfile(models.Model):
    ROLE_CHOICES=[
        ('admin','Admin'),
        ('member','Member'),    
        ('Librarian','librarian')
    ]
    user=models.OneToOneField('auth.User', on_delete=models.CASCADE)
    role=models.CharField(max_length=50)
 
    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
