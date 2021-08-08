from  . import views
from django.urls import path

urlpatterns = [

    path('', views.index),
    path('about', views.about),
    path('about2', views.about2),
    path('index2', views.about2)

]