
from django.urls import path
from . import views
urlpatterns = [
    path(r'index/',views.index),
    path(r'admin/',)
]