from django.contrib import admin
from .models import Author, AuthorProfile, Publisher, Book

# Register your models here.

admin.site.register(Author)
admin.site.register(AuthorProfile)
admin.site.register(Publisher)
admin.site.register(Book)
