# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect, get_object_or_404
from yarp.models import Post
#from django.http import Http404 
from dashboard.forms import loginForm, AddPostForm
from yarp.utils import error_message, success_message
import yarp.settings as settings
from django.contrib.auth import authenticate, login
from yarp.decorators import logged_out_required
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


def render_view(request, template, data={}):
    '''
    wrapper for rendering views , loads RequestContext
    @request  request object
    @template  string
    @data  tumple
    '''
    data['pagename'] = 'Dashboard'
    data['pagedesc'] = 'Sample description for dashboard page'
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
    if not request.user.is_active or not request.user.is_staff:
        return render_view(request, 'login.html', {})
    if request.POST:
        form = AddPostForm(request.POST, request.FILES)
        if not form.is_valid():
            error_message(request, "addpost")
        else:
            post = form.save()
            success_message(request, "addpost", {'post': post, 'is_published': request.POST['is_published']})
    return render_view(request, 'dashboard-index.html', {})


@login_required
def posts_page(request):
    '''
    handles the dashobard posts
    '''
    posts = {}
    #pagename = 'Posts'
    #pagedesc = 'Edit your posts here'
    try:
        posts = Post.objects.all().order_by('-id')
    except Exception, e:
        raise e
    return render_view(request, 'dashboard-posts.html', {'posts': posts})


@logged_out_required
def login_page(request):
    '''
    handles the dashobard landing page
    if user not logged in and not stuff we show them the login page
    @request  request object
    '''
    if request.POST:
        form = loginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active and user.is_staff:
                    login(request, user)
                    success_message(request, "login")
                    return HttpResponseRedirect(settings.DASHBOARD_URL)
                else:
                    error_message(request, "login")
            else:
                error_message(request, "login")
        else:
            error_message(request, "login")
    return render_view(request, 'login.html')


@logged_out_required
def recover_password(request):
    '''
    handles the dashobard landing page
    if user not logged in and not stuff we show them the login page
    @request  request object
    '''
    if not request.user.is_active or not request.user.is_staff:
        return render_view(request, 'login.html', {})
    return render_view(request, 'dashboard.html', {})


@login_required
def editblog_page(request, slug, action):
    '''
    handles the blog page 
    @request  request object
    '''
    post = get_object_or_404(Post.objects.filter(slug=slug, owner=request.user.pk), slug=slug, owner=request.user.pk)
    if request.POST:
        post = Post.objects.get(slug=slug, owner=request.user.pk)
        post_action = request.POST['post_action']
        if post_action == 'edit':
            post.title = request.POST['title']
            post.body = request.POST['body']
            if 'attachment' in request.FILES:
                post.attachment = request.POST['title']
            post.save()
            slug = post.slug
            success_message(request, "editpost", {'post': post})
            return HttpResponseRedirect(reverse('editblogpost', args=(slug, action)))
        if post_action == 'delete':
            post.delete()
            success_message(request, "deletepost",)
            return HttpResponseRedirect(reverse('dashboardposts',))
        if post_action == 'unpublish':
            post.is_published = 0
            post.save()
            success_message(request, "unpublish",)
            action = 'publish'
            return HttpResponseRedirect(reverse('editblogpost', args=(slug, action)))
        if post_action == 'publish':
            post.is_published = 1
            post.save()
            success_message(request, "editpost", {'post': post})
            action = 'edit'
            return HttpResponseRedirect(reverse('editblogpost', args=(slug, action)))
    return render_view(request, 'dashboard-editpost.html', {'post': post, 'action': action})

