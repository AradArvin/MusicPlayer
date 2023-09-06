import csv
import pandas
from typing import List
from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render
from django.urls import path
from django.contrib import admin
from django.urls.resolvers import URLPattern
from .forms import CsvImportForm
from accounts.models import CustomUser
from .models import (
    Artist, 
    Song, 
    Playlist, 
    Comment, 
    Genre, 
    Like,
    )
# Register your models here.



@admin.action(description="Mark selected comments as banned")
def make_banned(modeladmin, request, queryset):
    queryset.update(confirm="B")
    messages.success(request, "Selected comments were banned succsessfully...", "success")

@admin.action(description="Mark selected comments as confirmed")
def make_confirmed(modeladmin, request, queryset):
    queryset.update(confirm="C")
    messages.success(request, "Selected comments were confirmed succsessfully...", "success")
    

@admin.action(description="Export data(csv)")
def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response["Content-Description"] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)
    
    writer.writerow(field_names)
    for object in queryset:
        row = writer.writerow([getattr(object, field) for field in field_names])
    
    return response


@admin.register(Comment)
class CommentDisplay(admin.ModelAdmin):
    list_display = ('user', 'song', 'confirm',)
    list_filter = ('confirm',)
    search_fields = ('user', 'song',)
    actions = (make_banned, make_confirmed, export_as_csv,)
    list_per_page = 15
    change_list_template = "admin/comment_changelist.html"


    def get_urls(self) -> List[URLPattern]:
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]

        return my_urls + urls
    

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = pandas.read_csv(csv_file)
            try:
                for i in range(len(reader)):
                    user=CustomUser.objects.get(username=reader["user"][i])
                    song=Song.objects.get(title=reader["song"][i])
                    Comment.objects.create(
                        pk=reader["id"][i], 
                        confirm=reader["confirm"][i], 
                        user=user,
                        song=song,
                        commentz=reader["commentz"][i],
                        )
                self.message_user(request, "You'r csv file has been imported")
                return redirect("..")
            except:
                self.message_user(request, "The csv file fields does not match comment data!", 'error')
                return redirect("..")
        form = CsvImportForm()
        context = {"form":form}
        return render(request, "admin/csv_form.html", context)



@admin.register(Song)
class SongDisplay(admin.ModelAdmin):
    list_display = ("title", "genre", "playtime", "upload_date",)
    list_filter = ("genre",)
    search_fields = ("title",)
    list_per_page = 15



@admin.register(Like)
class LikeDisplay(admin.ModelAdmin):
    list_display = ('user', 'song',)
    search_fields = ('user', 'song',)
    list_per_page = 15



@admin.register(Playlist)
class PlayListDisplay(admin.ModelAdmin):
    list_display = ('title', 'owner',)
    search_fields = ('title', 'owner',)
    list_per_page = 15




admin.site.register(Genre)
admin.site.register(Artist)




