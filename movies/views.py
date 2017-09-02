from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

from .models import Movie
from .forms import MovieCreateForm

def movie_createview(request):
    form = MovieCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        obj = Movie.objects.create(
            title_en = form.cleaned_data.get("title_en"),
            release_year = form.cleaned_data.get("release_year"),
            genre = form.cleaned_data.get("genre"),
            length = form.cleaned_data.get("length"),
        )
        return HttpResponseRedirect("/movies/")
    if form.errors:
        errors = form.errors

    template_name = "movie_form.html"
    context = {"form" : form}
    return render(request, template_name, context)



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

