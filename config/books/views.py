from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

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