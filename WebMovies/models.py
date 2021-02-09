from django.db import models


class AdditionalInfo(models.Model):
    GENRES = {
        (0, "Other"),
        (1, "Action"),
        (2, "Animation"),
        (3, "Comedy"),
        (4, "Crime"),
        (5, "Drama"),
        (6, "Experimental"),
        (7, "Fantasy"),
        (8, "Historical"),
        (9, "Horror"),
        (10, "Romance"),
        (11, "Science Fiction"),
        (12, "Thriller"),
        (13, "Wester"),
    }
    duration = models.PositiveIntegerField(default=0)
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRES)


class Movie(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000, blank=True)
    description = models.TextField(default="")
    premiere = models.DateField(auto_now=False, null=True, blank=True)
    imdb_rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    additional_info = models.OneToOneField(
        AdditionalInfo, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)
