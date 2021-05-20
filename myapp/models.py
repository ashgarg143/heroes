from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)
    actor_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200)
    movie_id = models.IntegerField(primary_key=True)
    year = models.IntegerField(default=2021)
    favourite = models.BooleanField(default=False)
    genre = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class ActorMovie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.actor.name

