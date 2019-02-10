from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']

        if password == password2:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'Этот логин уже занят')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Эта эл. почта уже занята')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=user_name,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.is_active = False
                    user.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Активация аккаунта для использования платформы E-Petition.'
                    message = render_to_string('accounts/acc_activate_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                        'token': account_activation_token.make_token(user),
                    })
                    to_email = [user.email]
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    email.send()
                    messages.success(request, 'Мы отправили письмо на вашу почту для активация вашего аккаунта')
                    return redirect('login')
        else:
            messages.error(request, 'Пароли не совпадают!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        messages.success(request, 'Вы успешно активировали свой аккаут!')
        return redirect('index')
    else:
        messages.error(request, 'Ссылка для активации не валидна!')
        return redirect('login')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Вы вошли в систему')
            return redirect('index')
        else:
            messages.error(request, 'Неверный логин/пароль!', )
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Вы покинули систему')
        return redirect('index')





