from django.conf.urls import *

from .views import MovieListView, MovieDetailView, MovieCreateView

urlpatterns = [
    url(r'^$', MovieListView.as_view(), name="list"),
    url(r'^create/$', MovieCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', MovieDetailView.as_view(), name="detail"),
    #url(r'^movies/genre/(?P<slug>\w+)/$', MovieListView.as_view(), name="movies-genre-detail"),
    #url(r'^movies/genre/$', MovieListView.as_view(), name="movies-genre"),
    #url(r'^movies/release_year/$', MovieListView.as_view(), name="movies-release_year"),
    #url(r'^movies/country$', MovieListView.as_view(), name="movies-country"),
]
handler404 = 'movies.views.handler404'
handler500 = 'actors.views.handler500'