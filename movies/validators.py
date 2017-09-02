from django.core.exceptions import ValidationError


def validate_title_en(value):
    if value == "Hello":
        raise ValidationError(
            "Not a valid title!",
            params={"value" : value}
        )


def validate_release_year(value):
    if not 1800 < value < 2019:
        raise  ValidationError(
            "Not a valid year!",
            params={"value" : value }
        )


GENRES = ["Comedy", "Scifi", "Drama", "Thriller", "Action", "Crime"]

def validate_genre(value):
    genre = value.capitalize()
    if value not in GENRES and not genre in GENRES:
        raise  ValidationError(
            "Not a valid genre!",
            params={"value" : value}
        )