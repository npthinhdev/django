from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import index, blog, post, search

urlpatterns = [
    path('', index),
    path('search/', search, name='search'),
    path('blog/', blog, name='post-list'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('post/<id>/', post, name='post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
