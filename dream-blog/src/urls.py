from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import (index, blog, post, post_create,
                         post_update, post_delete, search)

urlpatterns = [
    path('', index),
    path('search/', search, name='search'),
    path('blog/', blog, name='post-list'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('create/', post_create, name='post-create'),
    path('post/<int:id>/', post, name='post-detail'),
    path('post/<int:id>/update/', post_update, name='post-update'),
    path('post/<int:id>/delete/', post_delete, name='post-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
