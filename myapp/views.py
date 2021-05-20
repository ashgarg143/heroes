from django.http import JsonResponse
from django.http.response import HttpResponse
from rest_framework.decorators import api_view

from .models import Movie, ActorMovie
from .serializers import MovieSerializer, ActorMovieSerializer


@api_view(['GET'])
def movies_list(request):
    actor_name = request.query_params.get("actor")

    if actor_name is not None:
        movies = ActorMovie.objects.filter(actor__name=actor_name)
        serializer = ActorMovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

    movies = Movie.objects.all().order_by('name')
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def top_movies(request):
    movies = Movie.objects.all().order_by('-rating')
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def latest_movies(request):
    movies = Movie.objects.all().order_by('-year')
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def movie_by_year(request, year):
    movies = Movie.objects.filter(year=year)
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_favourite_movies(request):
    queryset = Movie.objects.filter(favourite=True)
    serializer = MovieSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def add_favourite_movie(request):
    post_data = request.data
    movie_id = post_data['id']
    movie = Movie.objects.get(movie_id=movie_id)
    movie.favourite = True
    movie.save()
    return HttpResponse('Movie added to favourites')


@api_view(['POST'])
def remove_favourite_movie(request):
    post_data = request.data
    movie_id = post_data['id']
    movie = Movie.objects.get(movie_id=movie_id)
    movie.favourite = False
    movie.save()
    return HttpResponse('Movie removed from favourites')


@api_view(['POST'])
def add_movie(request):
    post_data = request.data
    name = post_data['name']
    movie_id = post_data['id']
    year = post_data['year']
    favourite = post_data['favourite']
    genre = post_data['genre']
    rating = post_data['rating']
    movie = Movie(movie_id=movie_id, name=name, year=year, favourite=favourite, genre=genre, rating=rating)
    movie.save()
    return HttpResponse('Movie ' + name + ' added successfully')


@api_view(['POST'])
def delete_movie(request):
    post_data = request.data
    movie_id = post_data['id']
    movie = Movie.objects.filter(movie_id=movie_id).first()
    if movie is not None:
        movie.delete()
        return HttpResponse('Movie deleted successfully')
    else:
        return HttpResponse('No Movie found with the given id')
