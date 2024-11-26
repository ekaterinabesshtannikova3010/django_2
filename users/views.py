from audioop import reverse
from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
import secrets
from users.forms import UserRegisterForm
from users.models import User
from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_mail = 'dolmatova3010@yandex.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_mail, recipient_list)

    # def form_valid(self, form):
    #    user = form.save()
    #    user.is_active = False
    #    token = secrets.token_hex(16)
    #    host = self.request.get_host()
    #    url = f'http://{host}/users/email_confirm/{token}/'
    #    send_mail(
    #        subject="Подтверждение почты",
    #        message=f"Привет, перейди пожалуйста по ссылке для подтверждения почты {url}",
    #        from_email=EMAIL_HOST_USER,
    #        recipient_list=[user.email]
    #    )
    #    return super().form_valid(form)

# def email_verification(request, token):
#     user = get_object_or_404(User,token=token)
#     user.is_active = True
#     return redirect(reverse("users:login"))