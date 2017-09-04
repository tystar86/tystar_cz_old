from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from .utils import unique_slug_generator

from movies.models import Movie

User = settings.AUTH_USER_MODEL

class Actor(models.Model):
    user            = models.ForeignKey(User)
    movie           = models.ForeignKey(Movie, blank=True, null=True)
    name            = models.CharField(max_length=120)
    born            = models.DateField(blank=True, null=True)
    died            = models.DateField(blank=True, null=True)
    country         = models.CharField(max_length=120, blank=True)
    sex             = models.CharField(max_length=5, blank=True)
    csfd            = models.URLField(max_length=100, blank=False)
    imdb            = models.URLField(max_length=100, blank=False)
    added           = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    public          = models.BooleanField(default=True)
    slug            = models.SlugField(blank=True)


    class Meta:
        ordering = ["-updated", "-added"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("actors:detail", kwargs={"slug" : self.slug})

    @property
    def title(self):
        return self.name

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Actor)