from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Horror', 'Horror'),
    ]
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    release_date = models.DateField()

    def __str__(self):
        return self.title
