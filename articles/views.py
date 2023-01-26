from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Article
from .forms import ArticleForm

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


# @login_required
# def article_create_view(request):
    
#     form = ArticleForm()
#     context = {
#         'article':{},
#         'form':form
#     }
    
#     if request.method == 'POST':
#         #  pass all uncleaned data to the form
#         form = ArticleForm(request.POST)
        
#         # check if the form is cleaned
#         if form.is_valid():
#             title =form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
        
#             # to inter new record to the db
#             new_articel = Article.objects.create(title=title, content=content)

#             context['article']=new_articel
#             context['created']=True
    
    
#     return render(request,'articles/create.html', context=context)



@login_required
def article_create_view(request):
    
    # passes the rquest otherwise passes none 
    form = ArticleForm(request.POST or None)
    context = {
        'article':{},
        'form':form
    }
        
        # check if the form is cleaned
    if form.is_valid():
        title =form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
    
        # to inter new record to the db
        new_articel = Article.objects.create(title=title, content=content)
        
        # insted the content context
        context['article']=new_articel
        context['created']=True
    
    
    return render(request,'articles/create.html', context=context)