from django.shortcuts import render

def index(request):
    names = "john,doe,mark,swain"
    return render(request, "filter_demo/index.html", {'names': names})
def greeting_view(request):
    books = {
        "The night rider": "Ben Author",
        "The Justice": "Don Abeman"
    }
    return render(request, 'filter_demo/simple_tag_template.html', {'username': 'jdoe', 'books': books})
# Create your views here.
