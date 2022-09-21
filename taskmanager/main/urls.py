from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),              #главная страница, высвечивается hello
    path('about-us', views.about, name='about'),      #страница about-us, высвечивается about
]
