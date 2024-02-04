from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addd/', include([
        path('', views.haft, name="haft"),
        path('jsonFile/', views.jsonFileT, name="jsonFileT"),
    ])),
]