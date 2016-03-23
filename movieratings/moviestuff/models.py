from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=150)
    genres = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Link(models.Model):
    imdbid = models.SmallIntegerField()
    tmdbid = models.SmallIntegerField()

    movie = models.ForeignKey(Movie)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Genre(models.Model):
    genres = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Rating(models.Model):

    userid = models.IntegerField()
    rating = models.FloatField()

    movie = models.ForeignKey(Movie)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):

    userid = models.IntegerField()
    tag = models.CharField(max_length=100)

    movie = models.ForeignKey(Movie)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
