import datetime
from django.db.models import Count
from reviews.models import Review

def get_books_read_by_month(username):
    current_year = datetime.datetime.now().year
    books = Review.objects.filter (creator__username__contains=username,date_created__year=current_year).values('date_created__month')\
        .annotate(book_count=Count('book__title'))
    return books

def get_book_read(username):
    books = Review.objects.filter(creator__username__contains=username).all()
    return [{'title': book_read.book.title,'completed_on': book_read.date_created} for book_read in books]
