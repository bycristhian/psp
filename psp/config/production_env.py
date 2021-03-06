
# Base configurations
from psp.config.base import *

# Libraries
import dj_database_url
from decouple import config


DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['www.psp-adsi.site', 'psp-adsi.site']

INSTALLED_APPS += [
    'storages'
]

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_SESSION_TOKEN = config('AWS_SESSION_TOKEN')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = "{}.s3.amazonaws.com".format(AWS_STORAGE_BUCKET_NAME)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

AWS_STATIC_LOCATION = 'static'
STATICFILES_STORAGE = 'psp.storage_backends.StaticStorage'    
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

AWS_MEDIA_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'psp.storage_backends.MediaStorage'


PREPEND_WWW = True
BASE_URL = "https://psp-adsi.site"
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT')


MAILJET_API_KEY = config('MAILJET_API_KEY')
MAILJET_API_SECRET = config('MAILJET_API_SECRET')