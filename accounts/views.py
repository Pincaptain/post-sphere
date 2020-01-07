from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy

from .forms import (
    AccountLoginForm,
    AccountRegisterForm,
    AccountPasswordChangeForm,
    AccountPasswordResetForm,
    AccountPasswordResetConfirmForm,
    AccountUpdateForm,
)
from forum.models import Post, Thread, Comment


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AccountLoginForm


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logged_out.html'


class AccountRegisterView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = AccountRegisterForm
    success_url = reverse_lazy('accounts_login', kwargs={'redirect': 'register'})


class AccountProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/profile.html'
    login_url = reverse_lazy('accounts_login')

    def get_context_data(self, **kwargs):
        return {
            'threads': Thread.objects.filter(admin=self.request.user)[:5],
            'posts': Post.objects.filter(op=self.request.user)[:5],
            'comments': Comment.objects.filter(commenter=self.request.user)[:5]
        }


class AccountUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'accounts/account_form.html'
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accounts_profile')

    def get_object(self, queryset=None):
        return self.request.user


class AccountPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('account_password_change_done')
    form_class = AccountPasswordChangeForm


class AccountPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


class AccountPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    form_class = AccountPasswordResetForm
    success_url = reverse_lazy('account_password_reset_done')


class AccountPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class AccountPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = AccountPasswordResetConfirmForm
    success_url = reverse_lazy('account_password_reset_complete')


class AccountPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
