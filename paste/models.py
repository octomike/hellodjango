from django.db import models
from uuid import uuid4

def get_short_uuid():
   return str(uuid4())[0:5]

class Code(models.Model):
    key  = models.CharField(max_length=6, primary_key=True, default=get_short_uuid)
    lang = models.CharField(max_length=32, default='bash')
    code = models.TextField(max_length=2048, help_text="some Code")
