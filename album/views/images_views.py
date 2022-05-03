from django.db.models import Q
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

from album.serializers import AlbumImagesPostSerializer, AlbumImagesDeleteSerializer, AlbumImagesUpdaterSerializer, \
    AlbumImagesDetailSerializer, AlbumImagesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from album.models import Album, AlbumImages


class AlbumImageFilter(FilterSet):
    """Фильтр для списка альбомов"""

    class Meta:
        model = AlbumImages
        fields = ['title', 'albums', 'tags', 'created_at']


class AlbumImagesListViews(generics.ListAPIView):
    """Просмотр всех Изображений пользователя"""

    serializer_class = AlbumImagesSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = AlbumImageFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['id', 'created_at']

    def get_queryset(self):
        user = self.request.user
        albums = Album.objects.filter(user=user)
        queryset = AlbumImages.objects.filter(Q(
            albums__in=albums
        ))
        return queryset


class AlbumImagesDetailViews(generics.RetrieveAPIView):
    """Детальный просмотр фотографии"""

    queryset = AlbumImages.objects.all()
    serializer_class = AlbumImagesDetailSerializer
    permission_classes = [IsAuthenticated]


class AlbumImagesUpdateViews(generics.UpdateAPIView):
    """Обновить фото"""

    permission_classes = [IsAuthenticated]
    queryset = AlbumImages.objects.all()
    serializer_class = AlbumImagesUpdaterSerializer


class AlbumImagesCreateViews(generics.ListCreateAPIView):
    """Добавить альбом"""

    permission_classes = [IsAuthenticated]
    serializer_class = AlbumImagesPostSerializer

    def get_queryset(self):
        user = self.request.user
        albums = Album.objects.filter(user=user)
        queryset = AlbumImages.objects.filter(Q(
            albums__in=albums
        ))
        return queryset


class AlbumImagesDestroyViews(generics.DestroyAPIView):
    """Удалить альбом"""

    permission_classes = [IsAuthenticated]
    queryset = AlbumImages.objects.all()
    serializer_class = AlbumImagesDeleteSerializer

