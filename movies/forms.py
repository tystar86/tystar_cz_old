from django import forms

class MovieCreateForm(forms.Form):
    title_en        = forms.CharField(required=True)
    release_year    = forms.IntegerField(required=True)
    genre           = forms.CharField(required=True)
    length          = forms.IntegerField(required=False)

    def clean_title_en(self):
        title_en = self.cleaned_data.get("title_en")
        if title_en == "Hello":
            raise forms.ValidationError("Not a valid title!")
        return title_en

    def clean_release_year(self):
        release_year = self.cleaned_data.get("release_year")
        if not 1800 < release_year < 2019:
            raise  forms.ValidationError("Not a valid year!")
        return release_year