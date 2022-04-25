from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_form, name='post_form'),
]