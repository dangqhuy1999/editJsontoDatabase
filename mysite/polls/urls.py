from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addd/', views.haft, name="haft"),
]
