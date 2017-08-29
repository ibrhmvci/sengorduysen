from django.shortcuts import render
from .models import PostHaber
from home.models import SocialIcons


def news_view(request):
    post_habers = PostHaber.objects.all()
    icons = SocialIcons.objects.all()
    return render(request, 'haberler.html', {
        'post_habers': post_habers,
        'icons': icons
    })
