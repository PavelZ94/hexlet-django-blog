from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from .models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request,
                      'articles/index.html',
                      context={'articles': articles, })


def index(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")

def home_redirect(request):
    return redirect(reverse('article', args=['python', 42]))
