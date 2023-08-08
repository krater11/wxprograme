from django.contrib import admin
from django.urls import path, include
from WX import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('message/',views.MessageView.as_view()),
]