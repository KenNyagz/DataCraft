from django.shortcuts import render
#from django.template import loader

def landing_page(request):
    '''The View for the landing page'''
    #template = loader.get_template("landing.html")
    return render(request, 'landing.html')

def intermediate(request):
    '''View for user to choose hirer or freelancer'''
    return render(request, 'intermediate.html')