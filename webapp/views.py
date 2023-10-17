from django.shortcuts import render

def index(request):
    """Main, index my site"""
    return render(request, 'webapp/index.html')
