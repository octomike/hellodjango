from django.db import models
from uuid import uuid4

def get_short_uuid():
   return str(uuid4())[0:5]

class Url(models.Model):
    key = models.CharField(max_length=6, primary_key=True, default=get_short_uuid)
    url = models.URLField(max_length=2000, help_text="Some URL")
