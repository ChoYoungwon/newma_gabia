from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '114.108.153.117', '.114.108.153.117']

# SQLite를 로컬 개발 환경에서 사용
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'newmadb.sqlite3',
    }
}
