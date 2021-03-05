from django.shortcuts import render

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')