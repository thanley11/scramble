from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from scramble.models import UserProfile
from scramble.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = {}
    
    return render_to_response("scramble/index.html", context_dict, context)
    
def about(request):
    context = RequestContext(request)
    context_dict = {}
    
    return render_to_response("scramble/about.html", context_dict, context)    

@login_required  
def dashboard(request):
    context = RequestContext(request)
    context_dict = {}
    
    return render_to_response("scramble/dashboard.html", context_dict, context)    
    
def signin(request):
    context = RequestContext(request)
    context_dict = {}
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/scramble/dashboard')
            else:
                context_dict['disabled_account'] = True
                return render_to_response("scramble/signin.html", context_dict, context)
                #Invalid login details
        else:
            print "Invalid login details: {0}, {1}".format(username,password)
            context_dict['bad_details'] = True
            return render_to_response("scramble/signin.html", context_dict, context)
    else:        
        return render_to_response("scramble/signin.html", context_dict, context)     

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/scramble/')
        
def register(request):
    context = RequestContext(request)
    context_dict = {}
    
    registered = False;
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
    
            registered = True
        else:
            print user_form.errors
    
    else:
        user_form = UserForm()
    
    context_dict['user_form'] = user_form
    context_dict['registered'] = registered
    return render_to_response("scramble/register.html", context_dict, context)
    
@login_required
def new_scramble(request):
        context = RequestContext(request)
        context_dict = {}
        
        return render_to_response("scramble/new_scramble.html", context_dict, context)    