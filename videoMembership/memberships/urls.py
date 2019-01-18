from django.urls import path
from .views import (
    MembershipSelectView, paymentView, updateTransactions, profileView, cancelSubscription
)

app_name = 'memberships'

urlpatterns = [
    path('payment/', paymentView, name='payment'),
    path('profile/', profileView, name='profile'),
    path('cancel/', cancelSubscription, name='cancel'),
    path('update-transactions/<sub_id>/', updateTransactions, name='update-transactions'),
    path('', MembershipSelectView.as_view(), name='select'),
]
