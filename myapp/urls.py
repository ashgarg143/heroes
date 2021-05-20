from django.urls import path

from . import views

urlpatterns = [

    path('', views.movies_list, ),
    path('top/', views.top_movies, ),
    path('latest/', views.latest_movies, ),
    path('movie/add/', views.add_movie, ),
    path('movie/delete/', views.delete_movie, ),
    path('year/<year>/', views.movie_by_year, ),
    path('favourites/', views.get_favourite_movies, ),
    path('favourites/add/', views.add_favourite_movie, ),
    path('favourites/remove/', views.remove_favourite_movie, ),
]
