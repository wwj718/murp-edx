#from django.http import HttpResponse
#from django.shortcuts import render_to_response
from django.template import RequestContext
#from edxmako.shortcuts import render_to_response
from edxmako.shortcuts import render_to_response, render_to_string

# Create your views here.
def murp_hello(request):
    #return HttpResponse("hello murp")
    return render_to_response('murp/murp.html',{})
def murp_home(request):
    """
    """
    #return HttpResponse("hello murp")
    return render_to_response('murp/murp.html',{})
