from django.urls import path
from .views import CourseListView, CourseDetailView, LessonDetailView

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='detail'),
    path('<slug:course_slug>/<slug:lesson_slug>/', LessonDetailView.as_view(), name='lesson-detail')
]
