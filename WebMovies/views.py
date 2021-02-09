from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from WebMovies.models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required


def all_movies(request):
    movies_all = Movie.objects.all()
    return render(request, "movies.html", {"movies": movies_all})


@login_required
def new_movie(request):

    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, "movie_form.html", {"form": form, "new": True})


@login_required
def edit_movie(request, id):

    movie = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)

    if form.is_valid():
        form.save()
        return redirect(all_movies)

    return render(request, "movie_form.html", {"form": form, "new": False})


@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == "POST":
        movie.delete()
        return redirect(all_movies)

    return render(request, "confirm.html", {"movie": movie})