from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_title_en, validate_release_year, validate_genre

User = settings.AUTH_USER_MODEL

class Movie(models.Model):
    owner           = models.ForeignKey(User)
    title_en        = models.CharField(max_length=100, validators=[validate_title_en])
    title_origin    = models.CharField(max_length=100, blank=True)
    title_cs        = models.CharField(max_length=100, blank=True)
    release_year    = models.IntegerField(validators=[validate_release_year])
    length          = models.IntegerField(blank=True)
    country         = models.CharField(max_length=100, blank=True)
    director        = models.CharField(max_length=100, blank=True)
    actor           = models.CharField(max_length=100, blank=True)
    genre           = models.CharField(max_length=120, blank=True, validators=[validate_genre])
    csfd            = models.URLField(max_length=100, blank=False)
    imdb            = models.URLField(max_length=100, blank=False)
    added           = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(blank=True)

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title_en

    def get_absolute_url(self):
        return reverse("movie-detail", kwargs={"slug" : self.slug})

    @property
    def title(self):
        return self.title_en


def pre_save_receiver(sender, instance, *args, **kwargs):
    instance.genre = instance.genre.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Movie)