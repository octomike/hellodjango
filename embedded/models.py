from django.db import models

class Url(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=32, primary_key=True)
