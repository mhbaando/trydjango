from django.contrib import admin
from django.urls import path
from .views import home_view
from articles.views import artice_detail_view

urlpatterns = [
    path('', home_view),  # index url home page
    path('articles/<int:id>/', artice_detail_view),
    path("admin/", admin.site.urls),
]
