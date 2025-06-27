from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "movies": ["Harry Potter", "Top Gun", "Gladiator"],
        "game": "fifa",
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})

def dont_know(request):
    return render(request, "movies/fuck.html", {})

# app/templates/app/index.html