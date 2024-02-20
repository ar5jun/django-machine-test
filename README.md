# django-machine-test

**URLs** :
```
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
    path('authors/<int:author_id>/reviews/', AuthorReviewListView.as_view(), name='author-review-list'),
    path('call/', list_authors_view, name='call_api'),
]
```

To build docker image of the project:

`docker build -t books_management . `

To run docker:

`docker run -p 8000:8000 books_management`
