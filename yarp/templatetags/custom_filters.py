from django.template import Library
from datetime import datetime
register = Library()


@register.filter
def get_range(value):
	str = value.split(',');
 	start = int(str[0])
  	end = int(str[1])
  	return range(start, end)


@register.filter
def is_false(arg):
    return arg is False


@register.filter
def date_today(arg):
	return datetime.today().strftime("%B %d, %Y")


@register.filter
def chop_title(s, l = 20):
	return s if len(s)<=l else s[0:l-3]+'...'


@register.filter
def chop_body(s, l = 50):
	return s if len(s)<=l else s[0:l-3]+'...'