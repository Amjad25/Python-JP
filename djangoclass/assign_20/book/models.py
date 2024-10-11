from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE )
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    published_date = models.DateField()
    





