from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
   # path('new',views.new),
    path('about.html',views.about),
    path('services.html',views.services),
    path('contact.html',views.contact),
    path('index.html', views.index),
    path('contacts', views.contacts, name='contacts'),
    path('register.html',views.register),
   # path('login.html',views.login),
    path('register',views.register,name='register'),
    path('news',views.news,name='news')
]