from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home Page
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

# Contact Page
def contact_view(request, *args, **kwargs):
    contact_page = "<html><body>Contact Page</body></html>"
    return HttpResponse(contact_page)

# Tech Support
def support_view(request, *args, **kwargs):
    support_page = "<html><body>Support Page</body></html>"
    return HttpResponse(support_page)