from django.shortcuts import render

def index(request):
    names = "john,doe,mark,swain"
    return render(request, "filter_demo/index.html", {'names': names})
# Create your views here.
