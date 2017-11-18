from django.db import models
from django.contrib.auth.models import User


class Contestant(models.Model):

    user = models.OneToOneField(User)
    name = models.CharField(max_length=10)
    score = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-score')
        verbose_name = "参赛者"
        verbose_name_plural = verbose_name
