from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ["date", "subject", "content"]


admin.site.register(News, NewsAdmin)
