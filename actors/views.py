from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Actor
from .forms import ActorForm


class ActorListView(ListView):
    template_name = "actors_list.html"
    def get_queryset(self):
        #return Actor.objects.filter(user=self.request.user)
        if self.request.user.is_anonymous():
            return Actor.objects.all()
        else:
            return Actor.objects.filter(user=self.request.user)


class ActorDetailView(DetailView):
    template_name = "actor_detail.html"
    queryset = Actor.objects.all()


class ActorCreateView(LoginRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = ActorForm
    login_url = "/login/"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ActorCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ActorCreateView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_queryset(self):
        if self.request.user.is_anonymous():
            return Actor.objects.all()
        else:
            return Actor.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ActorCreateView, self).get_context_data(*args, **kwargs)
        context["title"] = "Add an actor"
        return context


class ActorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "form.html"
    form_class = ActorForm
    login_url = "/login/"

    def get_queryset(self):
        if self.request.user.is_anonymous():
            return Actor.objects.all()
        else:
            return Actor.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ActorUpdateView, self).get_context_data(*args, **kwargs)
        context["title"] = "Update an actor"
        return context

    def get_form_kwargs(self):
        kwargs = super(ActorUpdateView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs