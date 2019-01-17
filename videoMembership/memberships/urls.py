from django.urls import path
from .views import MembershipSelectView, paymentView

app_name = 'memberships'

urlpatterns = [
    path('payment', paymentView, name='payment'),
    path('', MembershipSelectView.as_view(), name='select'),
]
