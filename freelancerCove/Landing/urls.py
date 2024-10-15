from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('intermediate', views.intermediate, name='intermediate')
]
