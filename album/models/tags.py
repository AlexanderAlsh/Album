from django.db import models


class Tags(models.Model):
    """ Тэги """

    title = models.CharField(max_length=100, verbose_name='Название тэга')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title
