from django.db import models
from time import gmtime, strftime
from datetime import datetime
import math
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=50)
    thumb_nail = models.ImageField(upload_to="genre", default="genre.avif")

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
    artist = models.ManyToManyField(Artist, related_name="songs")
    upload_date = models.DateField(auto_now_add=True)
    cover_image = models.ImageField(upload_to="cover", null=True, blank=True)
    audio_file = models.FileField(upload_to="audio", null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    size = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    playtime = models.CharField(max_length=10, default="0:00")
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.title
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Song, self).save(*args, **kwargs)

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
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name="playlists")

    def __str__(self) -> str:
        return self.title



class Like(models.Model):
    # like = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)



class Comment(models.Model):
    class Status(models.TextChoices):
        PENDING = "P", _("Pending")
        BAN = "B", _("Banned")
        CONFIRM = "C", _("Confirmed")

    confirm = models.CharField(choices=Status.choices, max_length=1, default="P")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    commentz = models.TextField(verbose_name="Comment")



