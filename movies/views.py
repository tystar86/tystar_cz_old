from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Movie
from .forms import MovieCreateViewForm


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
            queryset = Movie.objects.filter(genre__icontains=slug)
        else:
            queryset = Movie.objects.all()
        return queryset


class MovieDetailView(DetailView):
    template_name = "movie_detail.html"
    queryset = Movie.objects.all()


class MovieCreateView(LoginRequiredMixin, CreateView):
    form_class = MovieCreateViewForm
    template_name = "movie_form.html"
    login_url = "/login/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(MovieCreateView, self).form_valid(form)