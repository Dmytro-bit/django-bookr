from django.db import models
from django.contrib import auth
class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the publisher")
    website = models.URLField(help_text="Publisher website")
    email = models.EmailField(help_text="The publisher email")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=70, help_text="Title of the book")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isbn = models.CharField(max_length=20, verbose_name="ISBN namber of the book")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField("Contributor", through="BookContributor")

    def __str__(self):
        return self.title

    def isbn13(self):
        return "{}-{}-{}-{}-{}".format(self.isbn[0:3],self.isbn[3:4],self.isbn[4:6],self.isbn[6:12],self.isbn[12:13] )

class Contributor(models.Model):
    first_names = models.CharField(max_length=50, help_text="Contributor's first name or names")
    last_names = models.CharField(max_length=50, help_text="Contributor's last name or names")
    email = models.EmailField(help_text="Contact email for the contributor")

    def __str__(self):
        return self.initialled_name()

    def initialled_name(self):
        res = self.last_names + ', '
        for word in self.first_names.split():
            res += word[0]
        return res

class BookContributor(models.Model):
    class ContributorRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor hed in the book", choices=ContributorRole.choices, max_length=20)

class Review(models.Model):
    content = models.TextField(help_text="The review text")
    rating = models.IntegerField(help_text="The rating the reviewer has given")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review wos created")
    date_edited = models.DateTimeField(null=True, help_text="The date and time the review wos last edited")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The book that this review is for")

