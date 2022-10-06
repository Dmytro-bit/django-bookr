from django.shortcuts import render, get_object_or_404 , redirect
from .models import Book , Review, Contributor , Publisher
from .utils import average_rating
from .forms import SearchForm , PublisherForm, ReviewForm, BookMediaForm
from django.contrib import messages
from django.utils import timezone
import PIL.Image
from io import BytesIO
from django.core.files.images import ImageFile
from django.contrib.auth.decorators import user_passes_test , login_required
from django.core.exceptions import PermissionDenied


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0

        book_list.append({"book": book,
                          "book_rating": book_rating,
                          "number_of_reviews": number_of_reviews})

    context = {
        "book_list": book_list
    }
    return render(request, "reviews/book_list.html", context)

def welcome_view(request):
    return render(request, "base.html")

def search_view(request):
    max_search_books_length = 10
    books = []
    search_text = ''
    form = SearchForm(request.GET)
    search_history = request.session.get('search_history', [])
    if form.is_valid() and form.cleaned_data['search']:
        search_text = form.cleaned_data['search']
        search_in = form.cleaned_data.get("search_in") or "title"

        if search_in == 'title':
            books = Book.objects.filter(title__icontains = search_text )

        else:
            books = Book.objects.filter(contributors__first_names__icontains = search_text )| Book.objects.filter(contributors__last_names__icontains = search_text )

        if request.user.is_authenticated:
            search_history.append([search_in, search_text])
            request.session['search_history'] = search_history

    elif search_history:
        initial = dict(search=search_text,search_in=search_history[-1][0])
        form = SearchForm(initial=initial)

    return render(request, "reviews/search-results.html", {"books": books, "form": form, "search_text": search_text})

def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    overall_rating = average_rating([review.rating for review in book.review_set.all()])
    context = { "overall_rating": overall_rating ,"book": book}

    if request.user.is_authenticated:
        max_viewed_books_length = 10
        viewed_books = request.session.get('viewed_books', [])
        viewed_book = [book.id, book.title]
        if viewed_book in viewed_books:
            viewed_books.pop(viewed_books.index(viewed_book))
        viewed_books.insert(0, viewed_book)
        viewed_books = viewed_books[:max_viewed_books_length]
        request.session['viewed_books'] = viewed_books
    return render(request, "reviews/book_details.html", context)

def is_staff_user(user):
    return user.is_staff

@user_passes_test(is_staff_user)
def publisher_edit(request, pk = None):
    if pk is not None:
        publisher = get_object_or_404(Publisher,pk=pk)
    else:
        publisher = None

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            update_publisher = form.save()
            if publisher is None:
                messages.success(request, f'Publisher "{update_publisher}" was created')
            else:
                messages.success(request, f'Publisher "{update_publisher}" was updated')
            return redirect("publisher_edit", update_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, "reviews/instance-form.html", {"instance": publisher, "form": form, "model_type": "Publisher" })

@login_required
def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)

    if review_pk is not None:
        review = get_object_or_404(Review, book_id = book_pk, pk = review_pk )
        user = request.user
        if not user.is_staff and review.creator.id !=user.id:
            raise PermissionDenied
    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            update_review = form.save(commit=False)
            update_review.book = book

            if review is None:
                update_review.date_edited = timezone.now()
            update_review.save()

            if review is None:
                messages.success(request, f'Review for "{book.title}" was created')

            else:
                messages.success(request, f'Review for "{book.title}" was updated')

            return redirect("review_edit", book_pk, update_review.pk )

    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/instance-form.html", {"instance": review, "form": form, "model_type": "Review",
                                                 "related_model_type": "Book",
                                                 "related_instance":book})
@login_required
def book_media(request, book_pk):
    book = get_object_or_404(Book, pk = book_pk)

    if request.method == 'POST':
        form = BookMediaForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            book = form.save(False)
            cover = form.cleaned_data["cover"]

            if cover:
                image = PIL.Image.open(cover)
                image.thumbnail((300, 300))
                image_data = BytesIO()
                image.save(fp=image_data, format=cover.image.format)
                image_file = ImageFile(image_data)
                book.cover.save(cover.name, image_file)
                messages.success(request,f"Book {book} was successfully updated.")
                return redirect("book_details", book.pk)
    else:
        form =BookMediaForm()
    return render(request, "reviews/instance-form.html", {"form":form, "instance":book, "model_type": Book, "is_file_upload":True })



