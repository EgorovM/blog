# -*- coding: utf-8 -*-

from __future__                     import unicode_literals
from django.utils.encoding          import python_2_unicode_compatible
from django.db                      import models
from django.contrib.auth.models     import User
from datetime 					    import datetime
from pytz 						    import timezone
from django 						import forms

class Section(models.Model):
    img  = models.ImageField(upload_to = "images/", default = "images/post_default.jpg")
    name = models.CharField(max_length = 50)

    def __str__(self):
    	return str(self.name)

class Post(models.Model):
    section = models.ForeignKey('Section', on_delete = models.CASCADE)

    img   = models.ImageField(upload_to = "images/", default = "images/post_default.jpg")
    title = models.CharField(max_length = 50)
    text  = models.CharField(max_length = 500)

    date  = models.DateField('post date', default = datetime.now(tz = timezone('Asia/Yakutsk')))
    likes = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)

    def __str__(self):
    	return str(self.title)
