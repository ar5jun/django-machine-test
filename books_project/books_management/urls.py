# urls.py

from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
    path('authors/<int:author_id>/reviews/', AuthorReviewListView.as_view(), name='author-review-list'),
    path('call/', list_authors_view, name='call_api'),
]
