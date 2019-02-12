from django.urls import path
from .views import (
    ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
)

urlpatterns = [
    path('create/', ArticleCreateView.as_view()),
    path('<int:pk>', ArticleDetailView.as_view()),
    path('<int:pk>/update/', ArticleUpdateView.as_view()),
    path('<int:pk>/delete/', ArticleDeleteView.as_view()),
    path('', ArticleListView.as_view()),
]
