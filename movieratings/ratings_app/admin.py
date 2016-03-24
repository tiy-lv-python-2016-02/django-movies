from django.contrib import admin
from ratings_app.models import Genre, Link, Movie, Rating, Tag

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id","genres", "created_at", "modified_at")

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "imdbid", "tmdbid", "created_at", "modified_at")

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "genres", "created_at", "modified_at")

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("userid", "rating", "created_at", "modified_at")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("userid", "tag", "created_at", "modified_at")