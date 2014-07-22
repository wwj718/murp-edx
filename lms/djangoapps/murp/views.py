#from django.http import HttpResponse
#from django.shortcuts import render_to_response
from django.template import RequestContext
#from edxmako.shortcuts import render_to_response
from edxmako.shortcuts import render_to_response, render_to_string
from courseware.courses import get_courses, sort_by_announcement
from django.contrib.auth.models import User, AnonymousUser
from django.conf import settings

# Create your views here.
def murp_hello(request):
    #return HttpResponse("hello murp")
    return render_to_response('murp/murp.html',{})
def course_list(request, extra_context={}, user=AnonymousUser()):
    domain = settings.FEATURES.get('FORCE_UNIVERSITY_DOMAIN')
    # do explicit check, because domain=None is valid
    if domain is False:
    	domain = request.META.get('HTTP_HOST')
    courses = get_courses(user, domain=domain)
    courses = sort_by_announcement(courses)
    context = {'courses': courses}
    #return render_to_response('murp/selects.html',context)
    return render_to_response('murp/mytest.html',context)
