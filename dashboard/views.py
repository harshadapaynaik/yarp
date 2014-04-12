# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response


def render_view(request, template, data):
    '''
    wrapper for rendering views , loads RequestContext
    @request  request object
    @template  string
    @data  tumple
    '''
    return render_to_response(
        template, data,
        context_instance=RequestContext(request)
    )


def landing_page(request):
    '''
    handles the dashobard landing page
    if user not logged in and not stuff we show them the login page
    @request  request object
    '''
    if not request.user.is_active or not user.is_staff:
        return render_view(request, 'login.html', {})
    return render_view(request, 'dashboard.html', {})


def login(request):
    '''
    handles the dashobard landing page
    if user not logged in and not stuff we show them the login page
    @request  request object
    '''
    if not request.user.is_active or not user.is_staff:
        return render_view(request, 'login.html', {})
    return render_view(request, 'dashboard.html', {})


def recover_password(request):
    '''
    handles the dashobard landing page
    if user not logged in and not stuff we show them the login page
    @request  request object
    '''
    if not request.user.is_active or not user.is_staff:
        return render_view(request, 'login.html', {})
    return render_view(request, 'dashboard.html', {})