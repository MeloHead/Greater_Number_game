from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('start_game', views.start_game),
    path('delete', views.delete)
]