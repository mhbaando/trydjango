from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Article


def artice_detail_view(request, id):
    article_obj = Article.objects.get(id=id)
    context = {'article': article_obj}

    return render(request, 'articles/detail.html', context=context)
