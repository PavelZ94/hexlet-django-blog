from django.urls import path
from .views import IndexView, ArticleView


urlpatterns = [
    path('', IndexView.as_view()),
    path('<str:tag>/<int:article_id>/', ArticleView.as_view(), name='article'),
]
