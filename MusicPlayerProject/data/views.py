from typing import Any, Dict
from django.shortcuts import render
from .models import Song
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib.auth.decorators import login_required, permission_required
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
    
    
@permission_required
@login_required
class PlayListView(View):
    template_name = ""


@login_required
class LikeView():
    pass


@login_required
class LikedSongsView():
    pass


@login_required
class CreateCommentView():
    pass


@login_required
class CommentView():
    pass


@login_required
class ProfileView():
    pass


