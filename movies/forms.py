from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = {
            "title_en",
            "title_origin",
            "title_cz",
            "release_year",
            "length",
            "country",
            "genre",
            "csfd",
            "imdb",
        }