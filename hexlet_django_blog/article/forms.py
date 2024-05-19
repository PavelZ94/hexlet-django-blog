from django import forms
#from .forms import CommentArticleForm
from .models import Article
from django.views import View
from django.shortcuts import render
from django.db import models
from django.forms import ModelForm

#class CommentArticleForm(forms.Form):
#    content = forms.CharField(label='Комментарий')


#class CommentArticleView(View):

#    def get(self, request, *args, **kwargs):
#        form = CommentArticleForm()
#        return render(request, 'comment.html', {'form': form})


#    def post(self, request, *args, **kwargs):
#        form = CommentArticleForm(request.POST)
#        if form.is_valid():
#            comment = Comment(
#                name=form.cleaned_data['content'],
#            )
#            comment.save()


#class ArticleComment(models.Model):
#    content = models.CharField('content', max_length=100)


#class ArticleCommentForm(ModelForm):
#    class Meta:
#        model = ArticleComment
#        fields = ['content']


#class ArticleCommentFormView(View):

#    def post(self, request, *args, **kwargs):
#        form = ArticleCommentForm(request.POST)
#        if form.is_valid():
#            form.save()


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
