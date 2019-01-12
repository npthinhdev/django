from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='list'),
    path('<slug:slug>/', views.profile_view),
    path('friend-request/send/<int:id>/', views.send_friend_request),
    path('friend-request/cancel/<int:id>/', views.cancel_friend_reuqest),
    path('friend-request/accept/<int:id>/', views.accept_friend_request),
    path('friend-request/delete/<int:id>/', views.delete_friend_request)
]
