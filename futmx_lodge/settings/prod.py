from .base import *
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api
import cloudinary_storage

DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = [
    ('Ibrahim Abdulsamad', 'ibrahimabduldamad911@gmail.com'),
]

DATABASES = {
'default': {
}
}

database_url = env('DATABASE_URL')
DATABASES['default'] = dj_database_url.parse(database_url)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME'),
    'API_KEY': env('API_KEY'),
    'API_SECRET': env('API_SECRET'),
}

DEFAULT_FILE_STORAGE = [
    'cloudinary_storage.storage.MediaCloudinaryStorage',
]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True 
SECURE_HSTS_SECONDS = 3600 # new
SECURE_HSTS_INCLUDE_SUBDOMAINS = True # new
SECURE_HSTS_PRELOAD = True # new
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True # new
CSRF_COOKIE_SECURE = True