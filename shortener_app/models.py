from itertools import count
from django.db import models


class Shortener(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=20)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.long_url} -> {self.short_url}'
