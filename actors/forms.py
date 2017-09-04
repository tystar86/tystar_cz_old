from django import forms

from .models import Actor
from movies.models import Movie


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = [
            "name",
            "sex",
            "born",
            "died",
            "country",
            "movie",
            "csfd",
            "imdb",
        ]

    def __init__(self, user=None, *args, **kwargs):
        super(ActorForm, self).__init__(*args, **kwargs)
        self.fields["movie"].queryset = Movie.objects.filter(owner=user)
