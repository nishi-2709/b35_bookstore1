from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Adds initial set of books to the database'

    def handle(self, *args, **options):
        books_data = [
            {
                'title': 'The Girl in Room 105',
                'author': 'Chetan Bhagat',
                'description': 'A young man sets out to solve the mystery of his ex-girlfriend\'s murder.',
                'price': 299.00,
                'stock': 10
            },
            {
                'title': 'That Night',
                'author': 'Nidhi Upadhyay',
                'description': 'Four friends reunite after years, but their past comes back to haunt them.',
                'price': 349.00,
                'stock': 8
            },
            {
                'title': 'Half Girlfriend',
                'author': 'Chetan Bhagat',
                'description': 'A story about a Bihari boy who falls in love with a rich girl from Delhi.',
                'price': 199.00,
                'stock': 15
            },
            {
                'title': 'The Arranged Murder',
                'author': 'Nidhi Upadhyay',
                'description': 'A psychological thriller about a seemingly perfect marriage that turns deadly.',
                'price': 399.00,
                'stock': 12
            },
            {
                'title': '400 Days',
                'author': 'Chetan Bhagat',
                'description': 'A missing girl, a desperate mother, and a determined cop.',
                'price': 249.00,
                'stock': 20
            },
            {
                'title': 'Girl to Remember',
                'author': 'Durjoy Datta',
                'description': 'A heartwarming story about love, loss, and second chances.',
                'price': 179.00,
                'stock': 25
            },
            {
                'title': 'Can Love Happen Twice?',
                'author': 'Ravinder Singh',
                'description': 'A sequel to I Too Had a Love Story, exploring the possibility of love after loss.',
                'price': 199.00,
                'stock': 18
            },
            {
                'title': 'You Only Live Once',
                'author': 'Stuti Changle',
                'description': 'A story about chasing dreams and finding oneself.',
                'price': 279.00,
                'stock': 22
            }
        ]

        for book_data in books_data:
            book, created = Book.objects.get_or_create(
                title=book_data['title'],
                defaults=book_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added book: {book.title}'))
            else:
                self.stdout.write(f'Book already exists: {book.title}')

        self.stdout.write(self.style.SUCCESS('All books have been processed.')) 