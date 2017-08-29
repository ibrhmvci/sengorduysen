from django.shortcuts import render, get_object_or_404
from .models import PostYazar
from home.models import SocialIcons


def yazar_list_view(request):
    post_yazars = PostYazar.objects.all()
    icons = SocialIcons.objects.all()
    return render(request, 'yazarlar.html', {
        'post_yazars': post_yazars,
        'icons': icons
    })


def post_detail(request, slug):
    post = get_object_or_404(PostYazar, slug=slug)
    icons = SocialIcons.objects.all()
    return render(request, 'yazi.html', {
        'post': post,
        'icons': icons
    })
# Create your views here.
