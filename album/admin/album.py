from django.contrib import admin

from ..models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):

    class Meta:
        filter_horizontal = ('tags',)
