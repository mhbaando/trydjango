from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    # takes request and returns the response
    article_obj = Article.objects.get(id=1)
    html_string = render_to_string('home.html', context=article_obj.__repr__())
    return HttpResponse(html_string)
