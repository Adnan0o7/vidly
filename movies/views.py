from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    output = ', '.join([movie.title for movie in movies])
    return render(request, 'movies/index.html', {'movies': movies})
