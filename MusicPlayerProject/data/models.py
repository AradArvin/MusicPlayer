from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    bio = models.TextField(verbose_name="Artist Bio", null=True, blank=False)
    image = models.ImageField(upload_to="artists", null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)


class Song(models.Model):
    pass


class Playlist(models.Model):
    pass



class Like(models.Model):
    pass



class Comment(models.Model):
    pass



