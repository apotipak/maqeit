from django.shortcuts import render

# Create your views here.

# @login_required(login_url='/accounts/login/')
def index(request):    
    
    page_title = "HOME"
    
    return render(request, 'index.html', {
        'page_title': page_title, 
    })