from django.forms import ModelForm

from .models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = [
            "title_origin",
            "title_en",
            "title_cz",
            "release_year",
            "length",
            "country",
            "genre",
            "csfd",
            "imdb",
        ]