from django.contrib.auth import get_user_model
from django.db import models

from .tags import Tags
from ..utils import validate_image, uploader

from sorl.thumbnail import get_thumbnail


class Album(models.Model):
    """ Модель Альбома """
    title = models.CharField(max_length=100, verbose_name='Название альбома')
    poster = models.ImageField(validators=[validate_image], upload_to=uploader)
    description = models.CharField(max_length=256, verbose_name='Кратокое описание', blank=True, null=True)
    tags = models.ManyToManyField(Tags, verbose_name='Тэги')
    user = models.ForeignKey(get_user_model(), verbose_name='Владелец', on_delete=models.CASCADE, related_name='albums')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.title

    def get_images(self):
        images = self.images.all()
        for image in images:
            mini_image = get_thumbnail(image.image, '100x100', crop='center', quality=99)
            return {
                'image': image.image.url,
                'mini_image': mini_image.url
            }

        return None

    def get_count_images(self):
        return self.images.all().count()
