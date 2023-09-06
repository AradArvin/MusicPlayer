from django.urls import path
from .views import *

urlpatterns =[
    path("", HomeView.as_view(), name="home"),
    path("songs/", SongListView.as_view(), name="songlist"),
    path("song/<slug:slug>/", SongDetailView.as_view(), name="songlist"),
]