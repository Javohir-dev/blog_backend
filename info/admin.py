from django.contrib import admin

from info.models import MyInfo, CV


@admin.register(MyInfo)
class MyInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "fullname", "profession"]


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = [
        "id",
    ]
