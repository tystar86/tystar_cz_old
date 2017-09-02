"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth.views import LoginView, PasswordResetView
from django.views.generic import TemplateView

from movies.views import SearchGenreListView, MovieDetailView, MovieCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', LoginView.as_view(), name="login"),

    url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),

    url(r'^movies/$', SearchGenreListView.as_view(),name="movies"),
    url(r'^movies/create/$', MovieCreateView.as_view(), name="movie-create"),
    url(r'^movies/(?P<slug>[\w-]+)/$', MovieDetailView.as_view(), name="movie-detail"),
    url(r'^movies/genre/(?P<slug>\w+)/$', SearchGenreListView.as_view()),
    url(r'^movies/genre/$', SearchGenreListView.as_view(),name="movies-genre"),
    url(r'^movies/release_year/$', SearchGenreListView.as_view(),name="movies-release_year"),
    url(r'^movies/director$', SearchGenreListView.as_view(),name="movies-director"),
    url(r'^movies/actor$', SearchGenreListView.as_view(),name="movies-actor"),
    url(r'^movies/country$', SearchGenreListView.as_view(),name="movies-country"),

    url(r'^tvshows/$', SearchGenreListView.as_view(),name="tvshows"),

    url(r'^books/$', SearchGenreListView.as_view(),name="books"),

    url(r'^art/$', SearchGenreListView.as_view(),name="art"),

    url(r'^jingle/$', SearchGenreListView.as_view(),name="jingle"),
]
