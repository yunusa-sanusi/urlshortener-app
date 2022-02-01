from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-short-url/', views.create_short_url, name='create-short-url'),
    path('<str:short_url>/', views.redirect_to_main_url, name='redirect_to_main_url')
]
