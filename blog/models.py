import os
import uuid
from django.db import models


def post_image_path(instance, filename):
    ext = str(filename).split(".")[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return os.path.join("blog/", filename)


class Blog(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.FileField(upload_to=post_image_path, null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        if len(self.title) > 20:
            return "{}: {}".format(str(self.author), str(self.title)[:20]) + "..."
        return "{}: {}".format(str(self.author), str(self.title))
