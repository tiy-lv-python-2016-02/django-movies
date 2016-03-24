from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    genres = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    rating = models.FloatField()
    movie = models.ForeignKey(Movie)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Genre(models.Model):
    genre = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.genre


class Link(models.Model):
    imdb_link = models.SmallIntegerField()
    tmdb_link = models.SmallIntegerField()
    movie = models.ForeignKey(Movie)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    tag = models.CharField(max_length=150)
    movie = models.ForeignKey(Movie)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
