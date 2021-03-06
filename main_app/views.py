from distutils.log import error
from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import NewsSerializer
from .forms import NewsForm
from .models import News


class NewsListAPIview(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all().order_by("-date")
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = ["date"]


def newsCreate(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                form = NewsForm()
            except:
                pass
    else:
        form = NewsForm()
    return render(request, "news_create.html", {"form": form})
