from album.serializers import TagsSerializer, TagsCreateSerializer, TagsDeleteSerializer, TagsUpdaterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from album.models import Tags


class TagsListViews(generics.ListAPIView):
    """Просмотр всех тэгов"""

    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [IsAuthenticated]


class TagsUpdateViews(generics.UpdateAPIView):
    """Обновить тэг"""

    permission_classes = [IsAuthenticated]
    queryset = Tags.objects.all()
    serializer_class = TagsUpdaterSerializer


class TagsCreateViews(generics.ListCreateAPIView):
    """Добавить тэг"""

    permission_classes = [IsAuthenticated]
    serializer_class = TagsCreateSerializer
    queryset = Tags.objects.all()


class TagsDestroyViews(generics.DestroyAPIView):
    """Удалить тэг"""

    permission_classes = [IsAuthenticated]
    queryset = Tags.objects.all()
    serializer_class = TagsDeleteSerializer

