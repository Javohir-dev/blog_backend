from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "status", "id"]
    list_filter = [
        "status",
    ]
