from django.contrib import admin
from django.urls import path
from real import views

urlpatterns = [
  
  path('', views.welcome, name='welcome'),
  path('signup/', views.signup, name='signup'),
   path('index/', views.index, name='index'),
   path('residential/', views.residential, name='residential'),
   path('p1/', views.p1, name='p1'),
   path('p2/', views.p2, name='p2'),
   path('p3/', views.p3, name='p3'),
   path('p4/', views.p4, name='p4'),
   path('l1/', views.l1, name='l1'),
   path('l2/', views.l2, name='l2'),
   path('l3/', views.l3, name='l3'),
   path('l4/', views.l4, name='l4'),
   path('register/', views.register, name='register'),
   path('transaction/', views.transaction, name='transaction'),
   path('com/', views.com, name='com'),
   path('c1/', views.c1, name='c1'),
   path('c2/', views.c2, name='c2'),
   path('contact/', views.contact, name='contact'),
   path('loan/', views.loan, name='loan'),
   path('add_property/', views.add_property, name='add_property'),
   path('documental/', views.documental, name='documental'),
] 
