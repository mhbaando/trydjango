from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # index url home page
    path("admin/", admin.site.urls),
]
