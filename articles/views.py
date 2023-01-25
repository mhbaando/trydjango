from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Article


def article_search_view(request):
    # get the data from the form 
    data = request.GET
    id = data.get("q")
    
    #  find on based on the id 
   
    article_obj = None
    if id is not None: 
        article_obj = Article.objects.get(id=id)
        
        
    context = {
        'article': article_obj
    }
    
    return render(request,'articles/search.html', context=context)

def artice_detail_view(request, id):
    article_obj = Article.objects.get(id=id)
    context = {'article': article_obj}

    return render(request, 'articles/detail.html', context=context)

def article_create_view(request):
    
    context = {
        'article':{}
    }
    
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        content = data.get('content')
        
        # to inter new record to the db
        new_articel = Article.objects.create(title=title, content=content)
        
        context['article']=new_articel
        context['created']=True
    
    
    return render(request,'articles/create.html', context=context)