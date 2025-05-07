from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.db.models import Count

def dashboard(request):
    movies = Movie.objects.all()
    total_movies = movies.count()
    genre_counts = movies.values('genre').annotate(count=Count('genre'))
    return render(request, 'movies/dashboard.html', {'movies': movies, 'total_movies': total_movies, 'genre_counts': genre_counts})

def add_movie(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'movies/add_movie.html', {'form': form})

def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'movies/add_movie.html', {'form': form})

def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('dashboard')

def public_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/public_list.html', {'movies': movies})
