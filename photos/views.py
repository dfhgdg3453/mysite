from django.shortcuts import render

def IndexView(request):
    
    return render(request, 'photos\index.html')
# Create your views here.
