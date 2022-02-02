from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:token>/', views.redirect_to_main_url, name='short_url'),
]
