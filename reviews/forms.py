from django import forms
from .models import Publisher, Review, Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


RADIO_CHOICE = (
    ("title", "Title"),
    ("contributor", "Contributor")
)


class SearchForm(forms.Form):
    search = forms.CharField(min_length=3 , required=False)
    search_in = forms.ChoiceField(choices=RADIO_CHOICE, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.add_input(Submit("","Search"))

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["date_edited","book"]
    rating = forms.IntegerField(max_value=5 , min_value=0)

class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["cover","sample"]


