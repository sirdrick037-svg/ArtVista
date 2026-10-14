from django.contrib import admin
from .models import Artwork

# Register your models here.
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "created_at")
    search_fields = ("title", "description", "artist__username")
    list_filter = ("created_at",)