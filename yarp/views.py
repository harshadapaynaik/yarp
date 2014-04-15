# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from yarp.models import Post


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
    handles the landing page 
    @request  request object
    '''
    return render_view(request, 'index.html', {'featuredposts': featuredPosts()})


def blog_page(request, slug):
    '''
    handles the blog page 
    @request  request object
    '''
    post = get_object_or_404(Post.objects.filter(slug=slug), slug=slug)
    return render_view(request, 'post.html', {'post': post, 'featuredposts': featuredPosts()})


def featuredPosts():
    '''
    Get featured posts from db
    '''
    posts = {}
    try:
        posts = Post.objects.all().filter(is_featured=1)[:4]
    except Exception:
        pass
    if not posts.count():
        posts = Post.objects.all().order_by('-id')[:4]
    return posts
