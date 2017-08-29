from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class PostYazar(models.Model):
    title = models.CharField(max_length=250, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    photo = models.ImageField(null=True, blank=True, verbose_name='Fotoğraf', upload_to='news-images')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    Author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('yazarlar:detail', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while PostYazar.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(PostYazar, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Gönderi'
        verbose_name_plural = 'Yazar Gönderileri'


class Author(models.Model):
    name = models.CharField(max_length=125, null=False, blank=False, verbose_name='Yazarın Adı-Soyadı')
    photo = models.ImageField(null=True, blank=True, verbose_name='Fotoğrafı', upload_to='author-img')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Yazar'
        verbose_name_plural = 'Yazarlar'

