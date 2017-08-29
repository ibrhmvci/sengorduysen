from django.db import models


class SliderImage(models.Model):
    photo = models.ImageField(blank=False, null=False, upload_to='home-images')
    title = models.CharField(max_length=250)
    link1 = models.CharField(max_length=250)
    link1_title = models.CharField(max_length=25)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider Görseli'
        verbose_name_plural = 'Slider Görselleri'


class RightBannerTop(models.Model):
    photo = models.ImageField(blank=False, null=False, upload_to='home-images')
    title = models.CharField(max_length=250)
    link1 = models.CharField(max_length=250)
    link1_title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sağ Üst Banner'
        verbose_name_plural = 'Sağ Üst Banner Görselleri'


class RightBannerBottom(models.Model):
    photo = models.ImageField(blank=False, null=False, upload_to='home-images')
    title = models.CharField(max_length=250)
    link1 = models.CharField(max_length=250)
    link1_title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sağ Alt Banner'
        verbose_name_plural = 'Sağ Alt Banner Görselleri'


class LogoCarousel(models.Model):
    photo = models.ImageField(blank=False, null=False, upload_to='home-images')
    title = models.CharField(max_length=250, null=True)
    link1 = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Logo Carousel Görseli'
        verbose_name_plural = 'Logo Carousel Görselleri'


class SocialIcons(models.Model):
    title = models.CharField(max_length=150, null=True, verbose_name='Sosyal Medya Hesap Adı')
    link = models.CharField(max_length=250, null=True, verbose_name='Sosyal Medya Hesap Adresi')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ' Sosyal Medya Hesabı'
        verbose_name_plural = 'Sosyal Medya Hesapları'

