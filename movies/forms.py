from django import forms

from .models import Movie


class MovieCreateViewForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = {
            "title_en",
            "release_year",
            "genre",
            "length",
        }