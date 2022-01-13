from django.db import models


class News(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    subject = models.CharField(max_length=256, verbose_name="Заголовок новости")
    content = models.TextField(verbose_name="Содержание новости")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
