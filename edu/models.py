import os
from uuid import uuid4
from django.db import models


def get_thumbnail_file_path(instance, filename):
    ext = str(filename).split(".")[-1]
    filename = "{}.{}".format(uuid4(), ext)
    return os.path.join("thumbnail/", filename)


class EDU(models.Model):
    title = models.CharField(max_length=400)
    descriptions = models.TextField()
    tech = models.CharField(max_length=700)
    thumbnail = models.ImageField(upload_to=get_thumbnail_file_path)
    created_at = models.DateField(auto_now_add=True)
    video = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title[:25]}..."
