from django.contrib import admin
from django.urls import path
from . import views, api_views

urlpatterns = [path('', views.welcome_view, name = "welcome_view"),
               path('books/', views.book_list, name = "book_list"),
               path("book/<int:pk>/", views.book_details, name ="book_details"),
               path("book-search/", views.search_view, name = 'search_view'),
               path("publisher/<int:pk>/", views.publisher_edit, name = "publisher_edit"),
               path("publisher/new/", views.publisher_edit, name = "publisher_create"),
               path("books/<int:book_pk>/reviews/new/", views.review_edit, name = "review_create"),
               path("books/<int:book_pk>/reviews/<int:review_pk>/", views.review_edit, name = "review_edit"),
               path("books/<int:book_pk>/media/", views.book_media, name = "book_media" ),
               path("api/first_api_view/", api_views.first_api_view),


               ]