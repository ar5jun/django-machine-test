# views.py

from rest_framework import generics, permissions
from .models import Author, Book, Review
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer
from django.http import HttpResponse
from .authors import call_api
import requests
import json
from django.shortcuts import render


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer


class AuthorReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        return Review.objects.filter(author_id=author_id)


def list_authors_view(request):
    data = {
        "username": "admin",
        "password": "admin"
    }
    url = "http://127.0.0.1:8000/token/"
    response = requests.post(url, data=data)
    token = json.loads(response.text).get('access')

    if token:
        token = f"Bearer {token}"
        response = call_api('authors', token)
        authors_data = json.loads(response.text)
        context = {'authors_data': authors_data}
        return render(request, 'authors_table.html', context)
    else:
        return HttpResponse('No Key', content_type='text/plain')

# def create_authors_view(request):
