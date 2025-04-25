from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 10

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'description', 'price', 'stock', 'cover_image']
    success_url = reverse_lazy('book-list')

    def test_func(self):
        return self.request.user.is_staff

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'description', 'price', 'stock', 'cover_image']
    success_url = reverse_lazy('book-list')

    def test_func(self):
        return self.request.user.is_staff

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

    def test_func(self):
        return self.request.user.is_staff 