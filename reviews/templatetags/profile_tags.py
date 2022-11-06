from django import template
from reviews.models import Review

register = template.Library()

@register.inclusion_tag('reviews/book-list.html')
def book_list(username):
    reviews = Review.objects.filter(creator__username__contains = username)
    book_list = [review.book.title for review in reviews]
    return {"books_read": book_list}
