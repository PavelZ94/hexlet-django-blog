from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.


class IndexView(View):

    def get(self, request):
          context = {'name': 'article'}
          return render(request, 'index.html', context)


def index(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")

def home_redirect(request):
    return redirect(reverse('article', args=['python', 42]))
