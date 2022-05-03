from rest_framework import serializers

from album.models import AlbumImages
from album.utils import validate_image


class AlbumImagesSerializer(serializers.ModelSerializer):
    """ Список всех изображений """

    class Meta:
        model = AlbumImages
        fields = (
            'id',
            'title',
            'albums',
            'image',
            'tags',
            'created_at',
            'updated_at',
        )


class AlbumImagesDetailSerializer(serializers.ModelSerializer):
    """Детальный просмотр фотографии"""

    class Meta:
        model = AlbumImages
        fields = (
            'id',
            'title',
            'albums',
            'description',
            'image',
            'tags',
            'created_at',
            'updated_at',
        )


class AlbumImagesUpdaterSerializer(serializers.ModelSerializer):
    """Обновление данных фотографии"""

    class Meta:
        model = AlbumImages
        fields = (
            'title',
            'description',
            'albums',
            'tags'
        )


class AlbumImagesPostSerializer(serializers.ModelSerializer):
    """Добавление фотографии"""
    image = serializers.ImageField(validators=[validate_image], )

    class Meta:
        model = AlbumImages
        fields = (
            "title",
            'description',
            'image',
            'albums',
            'tags',
        )


class AlbumImagesDeleteSerializer(serializers.ModelSerializer):
    """Удаление альбома"""

    class Meta:
        model = AlbumImages
