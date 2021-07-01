from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class CounterModel(models.Model):
    num = CharField(max_length=10)
