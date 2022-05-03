from rest_framework import serializers

from album.models import Tags


class TagsSerializer(serializers.ModelSerializer):
    """ Список всех тэгов """

    class Meta:
        model = Tags
        fields = (
            'id',
            'title',
        )


class TagsUpdaterSerializer(serializers.ModelSerializer):
    """Обновление данных тэга"""

    class Meta:
        model = Tags
        fields = (
            'title',
        )


class TagsCreateSerializer(serializers.ModelSerializer):
    """Добавление тэга"""

    class Meta:
        model = Tags
        fields = (
            'title',
        )


class TagsDeleteSerializer(serializers.ModelSerializer):
    """Удаление тэга"""

    class Meta:
        model = Tags
