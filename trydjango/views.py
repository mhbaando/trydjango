from django.http import HttpResponse
from articles.models import Article


def home_view(request):
    # takes request and returns the response
    article_obj = Article.objects.get(id=1)
    print(article_obj.__repr__())
    return HttpResponse(f'{article_obj.content}')
