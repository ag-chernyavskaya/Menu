from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'С уважением, ваш любимый сайт о готовке!',
        'ag.charniauskaya@gmail.com',
        [user_email],
        fail_silently=False
    )