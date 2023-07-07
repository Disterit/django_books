from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsListView, AddBook


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('new/', AddBook.as_view(), name='book_add'),
    path('search/', SearchResultsListView.as_view(), name='search_results')
]