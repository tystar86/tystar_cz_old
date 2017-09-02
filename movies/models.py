from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

class Movie(models.Model):
    title_en        = models.CharField(max_length=100)
    title_origin    = models.CharField(max_length=100, blank=True)
    title_cs        = models.CharField(max_length=100, blank=True)
    release_year    = models.IntegerField()
    length          = models.IntegerField(blank=True)
    country         = models.CharField(max_length=100, blank=True)
    director        = models.CharField(max_length=100, blank=True)
    actor           = models.CharField(max_length=100, blank=True)
    genre           = models.CharField(max_length=120, blank=True)
    csfd            = models.URLField(max_length=100, blank=False)
    imdb            = models.URLField(max_length=100, blank=False)
    added           = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(blank=True)

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title_en

    @property
    def title(self):
        return self.title_en


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Movie)