import os
from uuid import uuid4
from django.db import models


def get_projects_file_path(instance, filename):
    ext = str(filename).split(".")[-1]
    filename = "{}.{}".format(uuid4(), ext)
    return os.path.join("projects/", filename)


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=400)
    descriptions = models.TextField()
    thumbnail = models.ImageField(upload_to=get_projects_file_path)
    created_at = models.DateField(auto_now_add=True)
    video = models.TextField()
    category = models.ManyToManyField(Category, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title[:25]}..."
