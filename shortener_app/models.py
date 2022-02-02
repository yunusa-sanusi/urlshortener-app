from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Shortener(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    long_url = models.URLField()
    short_url = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.long_url} -> {self.short_url}'
