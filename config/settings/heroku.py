'''
A production settings for heroku.com
'''
import dj_database_url
from .common import *

DEBUG = True

ALLOWED_HOSTS = ['*']
INSTALLED_APPS += (
    'gunicorn',
)
DATABASES['default'] = dj_database_url.config()
SECRET_KEY = '@#$RSDFDSfsfdg#$%#$%@#$@$DFGDFG'

SECURE_SSL_REDIRECT = True
# Honor the 'X-Forwarded-Proto' SECURE_PROXY_SSL_HEADERer for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Heroku URL does not pass the DB number, so we parse it in
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '{0}/{1}'.format(env('REDIS_URL', default='redis://127.0.0.1:6379'), 0),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,  # mimics memcache behavior.
                                        # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
        }
    }
}
