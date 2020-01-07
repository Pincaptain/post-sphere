from django.urls import path

from .views import (
    AccountLoginView,
    AccountLogoutView,
    AccountPasswordChangeView,
    AccountPasswordChangeDoneView,
    AccountPasswordResetView,
    AccountPasswordResetDoneView,
    AccountPasswordResetConfirmView,
    AccountPasswordResetCompleteView,
    AccountRegisterView,
    AccountProfileView,
    AccountUpdateView,
)

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='accounts_login'),
    path('register/', AccountRegisterView.as_view(), name='accounts_register'),
    path('logout/', AccountLogoutView.as_view(), name='accounts_logout'),
    path('profile/', AccountProfileView.as_view(), name='accounts_profile'),
    path('update/', AccountUpdateView.as_view(), name='accounts_update'),
    path('password_change/', AccountPasswordChangeView.as_view(), name='accounts_password_change'),
    path('password_change_done/', AccountPasswordChangeDoneView.as_view(), name='account_password_change_done'),
    path('password_reset/', AccountPasswordResetView.as_view(), name='account_password_reset'),
    path('password_reset_done/', AccountPasswordResetDoneView.as_view(), name='account_password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         AccountPasswordResetConfirmView.as_view(), name='account_password_reset_confirm'),
    path('password_reset_complete/',
         AccountPasswordResetCompleteView.as_view(), name='account_password_reset_complete'),
]
