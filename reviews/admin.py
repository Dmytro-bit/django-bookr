from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review
class BookAdmin(admin.ModelAdmin):
    search_fields = ("title","isbn__exact", "publisher__name")
    date_hierarchy = "publication_date"
    list_display = ("title","isbn13", "publisher" )
    list_filter = ("publisher", "publication_date")
    filter_horizontal = ("contributors", )

class ReviewAdmin(admin.ModelAdmin):
    # fields = ("content", "rating", "creator","book" )
    # fieldsets = (
    #     ("Linkage",        {"fields": ("creator","book") } ),
    #     ("Review content", {"fields": ("content","rating") } )
    # )
    fieldsets = (("Linkage", {'fields': ('creator', 'book')}),
                 ('Review content', {'fields': ('content', 'rating')}))

class ContributorAdmin(admin.ModelAdmin):
    list_display = ("last_names", "first_names")
    search_fields = ("last_names", "first_names")
    list_filter = ("last_names", )


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
