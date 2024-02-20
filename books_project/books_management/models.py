# models.py

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    total_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    total_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.FloatField()
    comment = models.TextField()

    def __str__(self):
        return self.rating
