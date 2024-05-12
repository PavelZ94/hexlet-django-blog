from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.


class IndexView(View):

    def get(self, request):
          context = {'name': 'article'}
          return render(request, 'index.html', context)


class ArticleView(View):

    def index(self, request, *args, **kwargs):
        return redirect(reverse('article',
                                kwargs={'tag': 'python', 'article_id': 42}))