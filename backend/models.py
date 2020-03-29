# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name


class UploadFile(models.Model):
    file_name = models.CharField(max_length=256)
    upload_time = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=64)
    user_name = models.CharField(max_length=64)
    status = models.IntegerField(max_length=1)

    def __unicode__(self):
        return self.book_name
