from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    login_url = 'account_login'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )


class AddBook(CreateView):
    model = Book
    template_name = 'books/book_add.html'
    fields = ['title', 'price', 'cover']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateBook(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['price', 'cover']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class AddReview(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'books/book_review.html'
    fields = ['review']

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs['book_id'])
        form.instance.book = book
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.kwargs['book_id']})


class DeleteReview(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'books/review_confirm_delete.html'
    success_url = reverse_lazy('book_detail')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.kwargs['book_id']})
