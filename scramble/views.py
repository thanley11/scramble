from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = {'hellotext':"hello text"}
    
    return render_to_response("scramble/index.html", context_dict, context)
    
def about(request):
    context = RequestContext(request)
    context_dict = {}
    
    return render_to_response("scramble/about.html", context_dict, context)    

def test(request):
    context = RequestContext(request)
    context_dict = {}
    
    return render_to_response("scramble/test.html", context_dict, context)     
    
def caro(request):
    context = RequestContext(request)
    context_dict = {}
    
    return render_to_response("scramble/caro.html", context_dict, context)     