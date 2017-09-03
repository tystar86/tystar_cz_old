from django import forms

from .models import Actor


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = {
            "name",
            "movie",
            "born",
            "died",
            "country",
            "sex",
        }

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        super(ActorForm, self).__init__(*args, **kwargs)
