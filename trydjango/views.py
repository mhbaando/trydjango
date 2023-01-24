from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article


def home_view(request):
    # # takes request and returns the response
    # article_obj = Article.objects.get(id=1)

    # # one to render the template
    # html_string = render_to_string('home.html', context=article_obj.__repr__())

    # # we can also render this way
    # tmpl = get_template('home.html')
    # # pass any data here
    # tmpl_srting = tmpl.render(context=article_obj.__repr__())

    articls_objt = Article.objects.all()
    context = {
        'articles': articls_objt
    }

    print(id)

    html_string = render_to_string('home.html', context=context)
    return HttpResponse(html_string)
