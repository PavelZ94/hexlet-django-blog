from django.urls import path
from .views import IndexView, home_redirect, index


urlpatterns = [
    path('', IndexView.as_view()),
#    path('', home_redirect),
#    path('articles/<str:tags>/<int:article_id>/', index, name='article'),
]
