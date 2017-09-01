from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import Movies

from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response


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
