'''
Decorators
'''
from django.shortcuts import HttpResponseRedirect
import yarp.settings as settings


def logged_out_required(function):
    '''This page cannot be viewed if a user is logged'''
    def wrapper(request, *args, **kw):
        if request.user and request.user.is_authenticated():
        	return HttpResponseRedirect(settings.BASE_URL+'home')
        else:
            return function(request, *args, **kw)
    return wrapper


def admin_required(function):
    '''This page cannot be viewed if a user is not stuff'''
    def wrapper(request, *args, **kw):
        if request.user.is_active and request.user.is_staff:
            return function(request, *args, **kw)
        else:
            return HttpResponseRedirect(settings.BASE_URL+'404')
    return wrapper


def ajax_required(f):
    """
    AJAX request required decorator
    use it in your views:

    @ajax_required
    def my_view(request):
        ....

    """
    def wrap(request, *args, **kwargs):
            if not request.is_ajax():
                #return HttpResponseBadRequest()
                return HttpResponseRedirect(settings.BASE_URL+'404')
            return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap