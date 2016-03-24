from django.contrib import admin
from movieapp.models import Movie, Rating, Genre, Link, Tag


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genres', 'date_added', 'date_modified')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'date_added', 'date_modified')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre', 'date_added', 'date_modified')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('imdb_link', 'tmdb_link', 'movie', 'date_added', 'date_modified')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'date_added', 'date_modified')
