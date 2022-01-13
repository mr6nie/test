from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewsForm


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
