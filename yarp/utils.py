from django.template.loader import render_to_string
import yarp.settings as settings
from django.contrib import messages
from django.template import RequestContext


def error_message(request, msgtype=None, data={}):
    template = settings.BASE_DIR + 'templates/error_messages.html'
    data['type'] = msgtype
    text = render_to_string(template, data, context_instance=RequestContext(request))
    messages.error(request, text)


def success_message(request, msgtype=None, data={}):
    template = settings.BASE_DIR + 'templates/success_messages.html'
    data['type'] = msgtype
    text = render_to_string(template, data, context_instance=RequestContext(request))
    messages.success(request, text)
