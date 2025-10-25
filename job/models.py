from django.db import models

from utils.models import BaseModel


# Create your models here.
class Job(BaseModel):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    posted_date = models.DateField()
