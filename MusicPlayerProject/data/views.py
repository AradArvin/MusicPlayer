from typing import Any, Dict
from django.shortcuts import render
from .models import Song
from django.views.generic import ListView, DetailView
from django.views import View
# Create your views here.


class HomeView(View):
    template_name = "data/index.html"

    def get(self, request, *args, **kwargs):
        songs = Song.objects.all()
        context = {"songs":songs}
        return render(request=request,template_name="data/index.html", context=context)


class SongListView(ListView):
    template_name = ""
    model = Song
    context_object_name = "songs"



class SongDetailView(DetailView):
    template_name = ""
    model = Song

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["song"] = Song.objects.filter(pk=kwargs["pk"])
        return context
    

class PlayListView(View):
    template_name = ""



class LikeView():
    pass



class LikedSongsView():
    pass



class CreateCommentView():
    pass



class CommentView():
    pass



class ProfileView():
    pass


