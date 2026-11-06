from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.author.name}"



class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')

    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title

    