from logging import PlaceHolder
from django.db import models


class News(models.Model):
    date = models.DateField(
        auto_now_add=False,
        auto_now=False,
        verbose_name="Дата",
    )
    subject = models.CharField(max_length=256, verbose_name="Заголовок новости")
    content = models.TextField(verbose_name="Содержание новости")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
