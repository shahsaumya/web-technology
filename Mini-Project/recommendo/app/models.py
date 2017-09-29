from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    #profile_pic = models.ImageField(uploadTo='profile_pic', blank=True)
    active = models.BooleanField(default=True)
    age = models.CharField(max_length=2, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def to_dict(self):
            return convert_to_dict(self)

class Movies(models.Model):
    movieId = models.CharField(max_length = 10, default=None)
    title = models.CharField(max_length = 100, default=None)
    genres = models.CharField(max_length = 100, default=None)
    imdbId = models.CharField(max_length = 10, default=None)
    tmdbId = models.CharField(max_length = 10, default=None)

    def __str__(self):
        return self.movieId

    def to_dict(self):
        return convert_to_dict(self)