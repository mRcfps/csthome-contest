from django.db import models


class Single(models.Model):

    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=1)

    class Meta:
        verbose_name = "单选题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question.split("\n")[0]


class Multiple(models.Model):

    question = models.CharField(max_length=200)
    answers = models.CharField(max_length=4)

    class Meta:
        verbose_name = "多选题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question.split("\n")[0]
