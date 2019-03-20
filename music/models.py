from __future__ import unicode_literals

from django.db import models

class Artist(models.Model):
    Name = models.CharField(max_length=500)
    Stage_Name = models.CharField(max_length=500)
    Birth_Date = models.CharField(max_length=250)
    Death_Date = models.CharField(max_length=250)
    Primary_Genre = models.CharField(max_length=1000)
    Artist_Bio = models.CharField(max_length=10000)
    Artist_Pic = models.CharField(max_length=1000)
    
class Album(models.Model):
    song = models.ForeignKey(Artist, on_delete=models.CASCADE)
