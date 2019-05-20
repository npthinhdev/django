from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import (IndexView, PostListView, PostDetailView, PostCreateView,
                         PostUpdateView, PostDeleteView, SearchView)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('blog/', PostListView.as_view(), name='post-list'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
