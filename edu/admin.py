from django.contrib import admin

from edu.models import EDU


@admin.register(EDU)
class EDUAdmin(admin.ModelAdmin):
    list_display = ["id", "status"]
    list_filter = [
        "status",
    ]
