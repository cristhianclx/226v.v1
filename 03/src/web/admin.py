from django.contrib import admin
from web.models import Search, Match


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ["id", "cv", "created_at"]
    ordering = ["created_at"]
    search_fields = ["id"]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ["id", "search", "position", "ranking", "created_at"]
    ordering = ["created_at"]
    search_fields = ["position"]
    raw_id_fields = ["search"]