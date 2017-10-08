from django.conf.urls import *

from .views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, GenreListView, GenreDetailView

urlpatterns = [
    url(r'^$', MovieListView.as_view(), name="list"),
    url(r'^create/$', MovieCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', MovieDetailView.as_view(), name="detail"),
    url(r'^(?P<slug>[\w-]+)/update/$', MovieUpdateView.as_view(), name="update"),
    url(r'^genre/$', GenreListView.as_view(), name="genre_list"),
    url(r'^genre/(?P<slug>[\w-]+)/$', GenreDetailView.as_view(), name="genre_detail"),

    #url(r'^movies/release_year/$', MovieListView.as_view(), name="movies-release_year"),
    #url(r'^movies/country$', MovieListView.as_view(), name="movies-country"),
]
handler404 = 'movies.views.handler404'
handler500 = 'actors.views.handler500'