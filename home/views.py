from django.shortcuts import render
from .models import *


def index_view(request):
    sliders = SliderImage.objects.all()
    right_banner_top = RightBannerTop.objects.all()
    right_banner_bottom = RightBannerBottom.objects.all()
    logo_carousel = LogoCarousel.objects.all()
    icons = SocialIcons.objects.all()
    return render(request, 'index.html', {
        'sliders': sliders,
        'right_banner_tops': right_banner_top,
        'right_banner_bottoms': right_banner_bottom,
        'logo_carousels': logo_carousel,
        'icons': icons
    })

