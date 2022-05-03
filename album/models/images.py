from django.db import models

from .album import Album
from .tags import Tags
from ..utils import validate_image, uploader


class AlbumImages(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название фото')
    albums = models.ForeignKey(Album, related_name='images', verbose_name='В какой альбом загрузить?',
                               on_delete=models.CASCADE)
    description = models.CharField(max_length=256, verbose_name='Краткое описание', blank=True, null=True)
    image = models.ImageField(validators=[validate_image], upload_to=uploader, verbose_name="Загрузить фото в альбом")
    tags = models.ManyToManyField(Tags, verbose_name='Тэги')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Изображение альбома'
        verbose_name_plural = 'Изображения альбома'

    def __str__(self):
        return self.title