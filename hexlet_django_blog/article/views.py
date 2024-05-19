from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
# Create your views here.
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm
from django.contrib import messages


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request,
                      'articles/index.html',
                      context={'articles': articles, })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request,
                      'articles/show.html',
                      context={'article': article, })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        messages = ''
        return render(request,
                      'articles/create.html',
                      {'form': form, 'messages': messages})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья добавлена')
            return redirect('articles')
        messages.error(request, 'При создании статьи произошла ошибка')
        return render(request,
                      'articles/create.html',
                      {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        messages = ''
        return render(request,
                      'articles/update.html',
                      {'form': form,
                       'article_id': article_id,
                       'messages': messages})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья изменена')
            return redirect('articles')
        messages.error(request, 'При редактировании статьи произошла ошибка')
        return render(request,
                      'articles/update.html',
                      {'form': form,
                       'article_id': article_id,
                       'messages': messages})
