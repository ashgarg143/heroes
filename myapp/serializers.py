from rest_framework import serializers

from myapp.models import Movie, ActorMovie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'name', 'year', 'genre', 'rating', 'favourite']


class ActorMovieSerializer(serializers.HyperlinkedModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = ActorMovie
        fields = ['movie']
