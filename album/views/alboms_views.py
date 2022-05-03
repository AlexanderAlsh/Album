from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from album.serializers import AlbumSerializer, AlbumDetailSerializer, AlbumUpdaterSerializer, \
    AlbumPostSerializer, AlbumDeleteSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from album.models import Album


class AlbumFilter(FilterSet):
    """Фильтр для списка альбомов"""

    class Meta:
        model = Album
        fields = ['title', 'tags', 'created_at']


class AlbumListViews(generics.ListAPIView):
    """Просмотр всех альбомов пользователя"""
    model = Album

    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = AlbumFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['id', 'created_at']

    def get_queryset(self):
        user = self.request.user
        queryset = Album.objects.filter(user=user)
        return queryset


class AlbumDetailViews(generics.RetrieveAPIView):
    """Детальный просмотр альбома"""

    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer
    permission_classes = [IsAuthenticated]


class AlbumUpdateViews(generics.UpdateAPIView):
    """Обновить альбом"""

    permission_classes = [IsAuthenticated]
    queryset = Album.objects.all()
    serializer_class = AlbumUpdaterSerializer


class AlbumCreateViews(generics.ListCreateAPIView):
    """Добавить альбом"""

    permission_classes = [IsAuthenticated]
    serializer_class = AlbumPostSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Album.objects.filter(user=user)
        return queryset


class AlbumDestroyViews(generics.DestroyAPIView):
    """Удалить альбом"""

    permission_classes = [IsAuthenticated]
    queryset = Album.objects.all()
    serializer_class = AlbumDeleteSerializer

