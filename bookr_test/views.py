from django.http import HttpResponse

def greeting_view(request):
    return HttpResponse("Hey there, welcome to Bookr!"
                        "Your one stop place"
                        " to review books")

# Create your views here.
