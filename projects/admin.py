from django.contrib import admin

from projects.models import Category, Projects


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "status", "id")
    list_filter = ("category", "status")
