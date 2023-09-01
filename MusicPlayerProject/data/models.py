from django.db import models
from time import gmtime, strftime
from datetime import datetime
import math
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
    title = models.CharField(max_length=100)
    description = models.TextField()
    artist = models.ManyToManyField(Artist)
    upload_date = models.DateField(auto_now_add=True)
    cover_image = models.ImageField(upload_to="cover", null=True, blank=True)
    audio_file = models.FileField(upload_to="audio", null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    size = models.IntegerField(default=0)
    playtime = models.CharField(max_length=10, default="0.00")


    def __str__(self) -> str:
        return self.title
    
    @property
    def duration(self):
        return str((strftime("%H:%M:%S", gmtime(float(self.playtime)))))

    @property
    def file_size(self):
        if self.size == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB")
        i = int(math.floor(math.log(self.size, 1024)))
        p = math.pow(1024, i)
        s = round(self.size / p, 2)
        return "%s %s" % (s, size_name[i])

class Playlist(models.Model):
    pass



class Like(models.Model):
    pass



class Comment(models.Model):
    pass



