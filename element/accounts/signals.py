from django.contrib.auth.signals import user_logged_in

from ipware.ip import get_real_ip, get_ip

from .models import LoginActivity


def save_login_activity(sender, user, **kwargs):
    '''
    A signal receiver which creates a new instance of
    the LoginActivity instance when a login attempt is successful.
    '''
    ip = get_real_ip(kwargs['request']) or get_ip(kwargs['request'])
    if ip:
        LoginActivity.objects.create(user=user, ip=ip)
    else:
        LoginActivity.objects.create(user=user, ip=None)


user_logged_in.connect(save_login_activity)
