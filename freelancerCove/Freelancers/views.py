from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseRedirect
from .models import freelancer
from Hirers.models import job, Hirer

def sign_up(request):
    '''sign_in view'''
    return render(request, "sign-up.html")
    

def login(request):
    '''login view'''
    return render(request, 'login.html')

#@login_required
@csrf_exempt # Disable CSRF protection -for testing
def verify_signup(request):
    '''Function to handle new freelancer registration'''
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        specialty = request.POST['specialty']
        technologies = request.POST['technologies']
        password = request.POST['password']
        phone_no = request.POST['phone']
        hashed_password = make_password(password)
        # other fields to be prompted later on, into the app

        new_freelancer = freelancer(
                                    firstName=firstname,
                                    lastName=lastname,
                                    email_address=email,
                                    specialty=specialty,
                                    technologies=technologies,
                                    hashed_password=hashed_password,
                                    phone_no=phone_no
        )
        try:
            new_freelancer.save()
            return HttpResponseRedirect('/freelance/login')
        except IntegrityError: # Email field is set to unique, hence any duplicate will tell
            message = "User already exists(Freelancer)"
            template = loader.get_template('user_exists.html')
            data = { "message" : message}
            return HttpResponse(template.render(data, request))
    else:
        return "forbidden", 403

#@login_required
@csrf_exempt
def verify_login(request):
    '''Function to handle user verification'''
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = freelancer.objects.get(email_address=email)
        if not check_password(password, user.hashed_password):
            return render(request, 'wrong_pwd.html')
        return HttpResponseRedirect('home') # Successful sign-in
    except freelancer.DoesNotExist:
        return render (request, "user_no_exist.html")

#@login_required
def jobs_list(request):
    '''View to display available jobs for freelancer'''
    jobs = job.objects.all()
    context = {"jobs": jobs}
    return render(request, 'home.html', context)

#@login_required
def job_details(request, job_id):
    '''View to display details of  selected job'''
    # Include: Offer from hirer, particulars hirer is looking for
    job_ = get_object_or_404(job, id=job_id)
    hirer_id = job_.hirer_id
    hirer = get_object_or_404(Hirer, id=job_.hirer_id)
    context = {'job': job_, 'hirer': hirer}
    return render(request, 'job_detail.html', context)

#@login_required
def messages(request):
    '''View for displaying messages for logged in freelancer'''
    pass
    # May be a future implementation