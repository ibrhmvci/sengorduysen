from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class PostHaber(models.Model):
    title = models.CharField(max_length=250, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    photo = models.ImageField(null=True, blank=True, verbose_name='Fotoğraf', upload_to='news-images')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while PostHaber.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(PostHaber, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'