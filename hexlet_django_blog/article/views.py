from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
# Create your views here.


class IndexView(View):

    def get(self, request):
          context = {'name': 'article'}
          return render(request, 'index.html', context)
