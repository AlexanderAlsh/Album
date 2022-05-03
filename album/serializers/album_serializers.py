from rest_framework import serializers

from album.models import Album
from album.utils import validate_image


class AlbumSerializer(serializers.ModelSerializer):
    """ Список альбомов пользователя """
    count_images = serializers.SerializerMethodField()

    def get_count_images(self, obj):
        return obj.get_count_images()

    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'poster',
            'count_images',
            'tags',
            'created_at',
            'updated_at',
        )


class AlbumDetailSerializer(serializers.ModelSerializer):
    """Детальный просмотр альбома"""

    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        return obj.get_images()

    class Meta:
        model = Album
        fields = (
            'title',
            'poster',
            'images',
            'description',
            'tags',
            'created_at',
            'updated_at',
        )


class AlbumUpdaterSerializer(serializers.ModelSerializer):
    """Обновление данных альбома"""

    class Meta:
        model = Album
        fields = (
            'title',
            'description',
            'tags',
        )


class AlbumPostSerializer(serializers.ModelSerializer):
    """Добавление альбома"""
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    poster = serializers.ImageField(validators=[validate_image], )

    class Meta:
        model = Album
        fields = (
            'title',
            'description',
            'poster',
            'tags',
            'user',
        )


class AlbumDeleteSerializer(serializers.ModelSerializer):
    """Удаление альбома"""

    class Meta:
        model = Album
