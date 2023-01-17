from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def homepage(request):
    
    return render(request, "homepage.html", context={})

def dashboard(request):
    return render(request, 'dashboard.html', context={})
    
def documentation(request):
    return render(request, 'documentation.html', context={})

def add_credits(request):
    if request.user.is_authenticated:
        request.user.credits += 5
        request.user.save()
        return JsonResponse({"credits": request.user.credits})