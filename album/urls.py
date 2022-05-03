from django.urls import path

from album.views import AlbumListViews, AlbumDetailViews, AlbumUpdateViews, AlbumCreateViews, AlbumDestroyViews, \
    AlbumImagesUpdateViews, AlbumImagesListViews, AlbumImagesDestroyViews, AlbumImagesCreateViews, \
    AlbumImagesDetailViews, TagsCreateViews, TagsUpdateViews, TagsDestroyViews, TagsListViews

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from app import settings

urlpatterns = [
    #Работа с альбомами
    path('album_list/', AlbumListViews.as_view()),
    path('album_list/<int:pk>', AlbumDetailViews.as_view()),
    path('album_add/', AlbumCreateViews.as_view()),
    path('album_update/<int:pk>/', AlbumUpdateViews.as_view()),
    path('album_delete/<int:pk>/', AlbumDestroyViews.as_view()),
    #Работа с фотографиями
    path('photo_list/', AlbumImagesListViews.as_view()),
    path('photo_list/<int:pk>', AlbumImagesDetailViews.as_view()),
    path('photo_add/', AlbumImagesCreateViews.as_view()),
    path('photo_update/<int:pk>/', AlbumImagesUpdateViews.as_view()),
    path('photo_delete/<int:pk>/', AlbumImagesDestroyViews.as_view()),
    #Работа с тэгами
    path('tags_list/', TagsListViews.as_view()),
    path('tags_add/', TagsCreateViews.as_view()),
    path('tags_update/<int:pk>/', TagsUpdateViews.as_view()),
    path('tags_delete/<int:pk>/', TagsDestroyViews.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ]