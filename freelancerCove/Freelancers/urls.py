from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.sign_up),
    path('login', views.login),
    path('verify_signup', views.verify_signup),
    path('verify_login', views.verify_login),
    path('home', views.jobs_list, name='freelancer_home'), # so apparently 'name' is for identifying a url
    path('job_detail/<int:job_id>', views.job_details, name='job_detail') # Especially in templating when using {% url %}
]