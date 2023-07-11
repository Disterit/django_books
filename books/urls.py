from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsListView, AddBook, UpdateBook, DeleteBook, AddReview, DeleteReview
from django.conf.urls import handler404


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('<uuid:pk>/update', UpdateBook.as_view(), name='book_update'),
    path('<uuid:pk>/delete', DeleteBook.as_view(), name='book_delete'),
    path('<uuid:book_id>/review/', AddReview.as_view(), name='book_review'),
    path('<uuid:book_id>/review/<int:pk>/delete/', DeleteReview.as_view(), name='delete_review'),
    path('new/', AddBook.as_view(), name='book_add'),
    path('search/', SearchResultsListView.as_view(), name='search_results')
]