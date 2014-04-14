from django.conf import settings


def global_vars(request):
	LOGGED_IN = False
	if request.user.is_authenticated() and request.user.is_staff:
		LOGGED_IN = True
	return {'BASE_URL':settings.BASE_URL, 'APP_NAME': settings.APP_NAME,
    'LOGGED_IN':LOGGED_IN, 'DASHBOARD_URL':settings.DASHBOARD_URL}