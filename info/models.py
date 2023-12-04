import os
from uuid import uuid4
from django.db import models


def get_avatar_file_path(instance, filename):
    ext = str(filename).split(".")[-1]
    filename = "{}.{}".format(uuid4(), ext)
    return os.path.join("my-avatar/", filename)


def get_cv_file_path(instance, filename):
    ext = str(filename).split(".")[-1]
    filename = "{}.{}".format(uuid4(), ext)
    return os.path.join("cv/", filename)


class MyInfo(models.Model):
    fullname = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to=get_avatar_file_path)
    profession = models.CharField(max_length=255)
    youtube = models.URLField(max_length=375)
    github = models.URLField(max_length=375)
    linkedin = models.URLField(max_length=375)
    telegram = models.URLField(max_length=375)
    description = models.TextField()

    def __str__(self) -> str:
        if not self.fullname:
            return "Fullname not found!"
        return self.fullname


class CV(models.Model):
    resume = models.TextField()
    cv = models.FileField(upload_to=get_cv_file_path)

    def __str__(self) -> str:
        return "Javohir's Resume"
