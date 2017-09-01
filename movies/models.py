from django.db import models

class Movies(models.Model):
    title_en        = models.CharField(max_length=100)
    title_origin    = models.CharField(max_length=100, blank=True)
    title_cs        = models.CharField(max_length=100, blank=True)
    release_year    = models.IntegerField(blank=True)
    country         = models.CharField(max_length=100, blank=True)
    director        = models.CharField(max_length=100, blank=True)
    genre           = models.CharField(max_length=120, blank=True)
    csfd            = models.URLField(max_length=100, blank=False)
    imdb            = models.URLField(max_length=100, blank=False)
    added           = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    #slug            = models.SlugField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title_en
