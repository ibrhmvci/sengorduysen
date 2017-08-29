from django.shortcuts import render, get_object_or_404
from .models import PostBlog
from home.models import SocialIcons


def blog_list_view(request):
    posts = PostBlog.objects.all()
    icons = SocialIcons.objects.all()
    return render(request, 'blog.html', {
        'posts': posts,
        'icons': icons
    })


def post_detail(request, slug):
    post = get_object_or_404(PostBlog, slug=slug)
    icons = SocialIcons.objects.all()
    return render(request, 'blog-detail.html', {
        'post': post,
        'icons': icons
    })
# Create your views here.
