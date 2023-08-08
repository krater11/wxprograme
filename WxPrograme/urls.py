from django.contrib import admin
from django.urls import path, include
from WxPrograme import views

urlpatterns = [
    path('login/', views.LoginView1.as_view()),
    path('message/', views.MessageView.as_view()),
]