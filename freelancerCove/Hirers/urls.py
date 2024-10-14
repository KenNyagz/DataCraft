from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.sign_up), #c
    path('login', views.login), #c
    path('verify_login', views.verify_login), #c
    path('verify_signup', views.verify_signup), #c
    path('home', views.home), #c
    path('available_freeelancers', views.freelancers_list),
    path('create_job', views.create_job), #c
    path('register_job', views.register_job)
]