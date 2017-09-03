from django.conf.urls import *

from .views import ActorListView, ActorDetailView, ActorCreateView

urlpatterns = [
    url(r'^$', ActorListView.as_view(), name="list"),
    url(r'^create/$', ActorCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', ActorDetailView.as_view(), name="detail"),
]