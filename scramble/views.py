from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from scramble.models import UserProfile, Course
from scramble.forms import UserForm, CourseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import password_reset
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response("index.html", context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response("about.html", context_dict, context)

@login_required
def dashboard(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response("dashboard.html", context_dict, context)

@login_required
def players(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response("players.html", context_dict, context)

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
                return HttpResponseRedirect('/dashboard')
            else:
                context_dict['disabled_account'] = True
                return render_to_response("signin.html", context_dict, context)
                #Invalid login details
        else:
            print "Invalid login details: {0}, {1}".format(username,password)
            context_dict['bad_details'] = True
            return render_to_response("signin.html", context_dict, context)
    else:
        return render_to_response("signin.html", context_dict, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

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
    return render_to_response("register.html", context_dict, context)

@login_required
def new_scramble(request):
    context = RequestContext(request)

    course_list = get_course_list()

    context_dict = {}

    context_dict['course_list'] = course_list

    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CourseForm()

    context_dict['form'] = form
    return render_to_response('new_scramble.html', context_dict, context)


@login_required
def friends(request):
        context = RequestContext(request)
        context_dict = {}

        return render_to_response("friends.html", context_dict, context)

@login_required
def history(request):
        context = RequestContext(request)
        context_dict = {}

        return render_to_response("history.html", context_dict, context)

@login_required
def profile(request):
        context = RequestContext(request)
        context_dict = {}
        return render_to_response("profile.html", context_dict, context)

@login_required
def change_password(request):
    if request.method == 'POST':
        return password_reset(request,
            from_email=request.POST.get('email'))
    else:
        return render(request, 'change_password.html')


@login_required
def password_reset_done(request):
        context = RequestContext(request)
        context_dict = {}

        return render_to_response("password_reset_done.html", context_dict, context)


def get_course_list(max_results=0, starts_with=''):
    course_list = []

    if starts_with:
        course_list = Course.objects.filter(name__startswith=starts_with)
    else:
        course_list = Course.objects.all()


    if max_results > 0:
        if len(course_list) > max_results:
            course_list = course_list[:max_results]

    return course_list

@login_required
def courses(request):
        context = RequestContext(request)

        course_list = get_course_list()

        context_dict = {'course_list' : course_list}

#added last based off of views.py category rango
        try:
            course = Course.objects.order_by('name')
            context_dict['course'] = course_list

        except Course.DoesNotExist:
            pass

        return render_to_response("courses.html", context_dict, context)



def track_url(request):
    context = RequestContext(request)
    course_id = None
    url = '/dashboard/courses/'
    if request.method == "GET":
        if 'course_id' in request.GET:
            course_id = request.GET['course_id']
            try:
                course = Course.objects.get(id=course_id)

                course.save()
                url = course.url
            except:
                pass
    return redirect(url)
