from django.contrib import admin
from django.urls import path
from .views import home_view
from articles import views
from accounts.views import login_view

urlpatterns = [
    path('', home_view),  # index url home page
    path('articles/', views.article_search_view),
    path('articles/create/', views.article_create_view),
    path('articles/<int:id>/', views.artice_detail_view),
    
    path("admin/", admin.site.urls),
    path('login/', login_view), 
    
]
