from django.contrib import admin
from .models import AdditionalInfo, Movie

# Register your models here.
# admin.site.register(Movie)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ["Title", "Description", "Year"]
    # exclude = ["Description"]
    list_display = ["title", "imdb_rating", "year"]
    list_filter = ("year",)
    search_fields = ("title",)


admin.site.register(AdditionalInfo)