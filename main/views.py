from django.shortcuts import render

# Create your views here.
def homepage(request):
    print(request.user)
    
    return render(request, "homepage.html", context={})

def dashboard(request):
    return render(request, 'dashboard.html', context={})
    
def documentation(request):
    return render(request, 'documentation.html', context={})