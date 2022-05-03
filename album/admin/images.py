from django.contrib import admin

from ..models import AlbumImages


@admin.register(AlbumImages)
class AlbumImagesAdmin(admin.ModelAdmin):

    class Meta:
        filter_horizontal = ('tags',)
