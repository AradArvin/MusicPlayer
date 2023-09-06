from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserDisplay(admin.ModelAdmin):
    list_display = ('username', 'email', 'acc_type', 'date_joined')
    list_filter = ('acc_type',)
    search_fields = ('username',)
    list_per_page = 15
    