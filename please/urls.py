from django.urls import path
from . import views

app_name = "please"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('medicine/', views.medicine, name='medicine'),
    path('medicine1/', views.medicine1, name='medicine1'),
    path('buy/', views.buy, name='buy'),
    path('buy1/', views.buy1, name='buy1'),
    path('news/', views.news, name='news'),
    path('news1/', views.news1, name='news1'),
    path('contact/', views.contact, name='contact'),
    path('contact1/', views.contact1, name='contact1'),
    path('login/', views.login, name='login'),
    path('login1/', views.login1, name='login1'),
    path('new/', views.new, name='new'),
    path('payment/<int:pk>/', views.payment, name='payment'),
    path('payment1/<int:pk>/', views.payment1, name='payment1'),
]

