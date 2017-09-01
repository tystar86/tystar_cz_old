from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Movies

def movies_listview(request):
    template_name = "movies_list.html"
    queryset = Movies.objects.all()
    context = {"movies_list" : queryset}
    return render(request, template_name, context)