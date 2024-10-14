from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import Hirer, job
from Freelancers.models import freelancer

def sign_up(request):
    '''sign_in view'''
    return render(request, 'h_sign-up.html')

def login(request):
    '''login view'''
    return render(request, 'h_login.html')

#@login_required
@csrf_exempt # Disable CSRF protection -for testing
def verify_signup(request):
    '''Function to handle new hirer registration'''
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email= request.POST['email']
        password = request.POST['password']
        phone_no = request.POST['phone']
        hashed_password = make_password(password)
        # other fields to be prompted later on, into the app

        new_hirer = Hirer(
                          firstName=firstname,
                          lastName=lastname,
                          email_address=email,
                          hashed_password=hashed_password,
                          phone_no=phone_no
        )
        try:
            new_hirer.save()
            return HttpResponseRedirect('/hiring/login')
        except IntegrityError:    # Email field is set to unique, hence any duplicate will tell
            message = "User already exists(Hirer)"
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
        user = Hirer.objects.get(email_address=email)
        if not check_password(password, user.hashed_password):
            return render(request, 'wrong_pwd.html')
        request.session['hirer_email'] = email  # Create user session, to be used by other functions
        return HttpResponseRedirect('home')
    except Hirer.DoesNotExist:
        return render (request, "user_no_exist.html")

#@login_required
def create_job(request):
    '''Hirer's job creation utility'''
    return render(request, 'create_job.html')

#@login_required
@csrf_exempt
def register_job(request):
    '''Function to save job ti the database after user creates it'''
    if request.method == "POST":
        title = request.POST['job_title']
        category = request.POST['category']
        description = request.POST['description']
        pay = request.POST['pay']

        hirer_email = request.session.get('hirer_email')
        hirer = Hirer.objects.get(email_address=hirer_email)
        hirer_id = hirer.id

        new_job = job(
                       title=title,
                       category=category,
                       description=description,
                       pay=pay,
                       hirer_id=hirer_id
        )
        new_job.save()
    return HttpResponseRedirect('/hiring/home')

#@login_required
def home(request):
    '''Hirer home page'''
    hirer_email = request.session.get('hirer_email')
    hirer = Hirer.objects.get(email_address=hirer_email)
    hirer_id = hirer.id
    jobs = job.objects.filter(hirer_id=hirer_id) #
    data = {"jobs": jobs}
    return render(request, 'h_home.html', data)

def freelancers_list(request):
    '''View to display available freelancers for hirer'''
    freelancers = freelancer.objects.all()
    context = {"freelancers": freelancers}
    return render(request, 'available_freelancers.html', context)

def freelancer_details(request):
    '''View to display details of  selected freelancer'''
    # Include: Freelancer price and/or rate, technologies and specialties of freelancer
    pass

def messages(request):
    '''View for displaying messages for logged in hirer'''
    pass
    # May be a future implementation