from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:service_id>/keyboard', views.keyboard, name='keyboard'),
    path('<int:service_id>/message', views.message),
]

