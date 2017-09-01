from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import Movies


class SearchGenreListView(ListView):
    template_name = "movies_list.html"

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Movies.objects.filter(genre__icontains=slug)
        else:
            queryset = Movies.objects.all()
        return queryset

class MovieDetailView(DetailView):
    template_name = "movie_detail.html"
    queryset = Movies.objects.all()
