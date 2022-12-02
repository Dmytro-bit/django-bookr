from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def greeting_view(request):
    return HttpResponse("Hey there, welcome to Bookr!"
                        "Your one stop place"
                        " to review books")

@login_required
def greeting_view_user(request):
    user = request.user
    return HttpResponse(f"welcome to Bookr! {user}")
# Create your views here.
