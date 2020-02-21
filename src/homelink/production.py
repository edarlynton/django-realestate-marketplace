"""
Django settings for homelink project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from django.conf import settings

if not settings.DEBUG:

    import os

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'fg2@!fui#3@fnspegpcar(8k*v=cn%7(0m-_358(!c=1rhr@_w'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    ALLOWED_HOSTS = ['167.99.80.118', 'homelink.ng', 'www.homelink.ng', 'homelink.com.ng', 'www.homelink.com.ng', 'homelink.nakasoft.ng']


    ADMINS = (
        ("Homelink Support", "support@nakasoft.com.ng"),
    )



    EMAIL_HOST = 'box.nakamail.com' #'smtp.gmail.com'
    EMAIL_HOST_USER = 'nakasoft-noreply@nakasoft.com.ng' #'lynton101@gmail.com'
    EMAIL_HOST_PASSWORD = 'nakas0ft05' #'ikechukwu69'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    SERVER_EMAIL = 'nakasoft-noreply@nakasoft.com.ng'
    DEFAULT_FROM_EMAIL = 'nakasoft-noreply@nakasoft.com.ng'



    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'django.contrib.staticfiles',
        'django.contrib.humanize',

        # third party apps
        'crispy_forms',
        'django_filters',
        'markdown_deux',
        'pagedown',
        'watermarker',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        # 'allauth.socialaccount.providers.facebook',
        # 'allauth.socialaccount.providers.twitter',
        # 'allauth.socialaccount.providers.instagram',
        # 'allauth.socialaccount.providers.google',

        # local apps
        'comments',
        'contact',
        'dashboard',
        'newsletter',
        'posts',
        'products', 
    ]


    CRISPY_TEMPLATE_PACK = 'bootstrap4'



    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',

        # `allauth` specific authentication methods, such as login by e-mail
        'allauth.account.auth_backends.AuthenticationBackend',
    )



    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'homelink.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'homelink.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'homelink',
            'USER': 'homelinkuser',
            'PASSWORD': '!G0t2M@ny69',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


    # Password validation
    # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]


    # Internationalization
    # https://docs.djangoproject.com/en/2.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/
    
    STATIC_URL = '/static/'
    STATIC_ROOT = '/var/www/static-root/homelink/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    MEDIA_URL = '/media/'
    MEDIA_ROOT = '/var/www/media-root/homelink/'




    SITE_ID = 1


    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = '/'

    ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = LOGIN_REDIRECT_URL
    ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
    ACCOUNT_CONFIRM_EMAIL_ON_GET = False
    ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
    ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

    ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"
    ACCOUNT_EMAIL_SUBJECT_PREFIX = None
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

    ACCOUNT_LOGOUT_ON_GET = True
    ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL
    ACCOUNT_SIGNUP_FORM_CLASS = 'dashboard.forms.SignupForm'
    ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
    ACCOUNT_UNIQUE_EMAIL = True
    ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'
    ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
    ACCOUNT_USERNAME_MIN_LENGTH = 5
    ACCOUNT_USERNAME_BLACKLIST = ['homelink', 'homelinkng', 'homelink.ng']
    ACCOUNT_USERNAME_REQUIRED = True
    ACCOUNT_PRESERVE_USERNAME_CASING = False
    ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
    ACCOUNT_PASSWORD_MIN_LENGTH = 8
    ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
    ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
    ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
    ACCOUNT_SESSION_REMEMBER = False


    # SOCIALACCOUNT_ADAPTER = "allauth.socialaccount.adapter.DefaultSocialAccountAdapter"
    # # Specifies the adapter class to use, allowing you to alter certain default behaviour.
    # SOCIALACCOUNT_AUTO_SIGNUP = True
    # # Attempt to bypass the signup form by using fields (e.g. username, email) retrieved from the social account provider. If a conflict arises due to a duplicate e-mail address the signup form will still kick in.
    # SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION
    # # As ACCOUNT_EMAIL_VERIFICATION, but for social accounts.
    # SOCIALACCOUNT_EMAIL_REQUIRED = ACCOUNT_EMAIL_REQUIRED
    # # The user is required to hand over an e-mail address when signing up using a social account.
    # SOCIALACCOUNT_FORMS = {}
    # # Used to override forms, for example: {'signup': 'myapp.forms.SignupForm'}
    # SOCIALACCOUNT_PROVIDERS = dict
    # # Dictionary containing provider specific settings.
    # SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
    # # Request e-mail address from 3rd party account provider? E.g. using OpenID AX, or the Facebook “email” permission.
    # SOCIALACCOUNT_STORE_TOKENS = True


    # http://localhost:8000/accounts/facebook/login/callback/
    # http://127.0.0.1:8000/accounts/facebook/login/callback/
    # http://127.0.0.1:8000/accounts/instagram/login/callback/
    # http://oyaconstruct.com/accounts/facebook/login/callback/

    # SOCIALACCOUNT_PROVIDERS = \
    #     {'facebook':
    #        {'METHOD': 'oauth2',
    #         'SCOPE': ['email', 'public_profile', 'user_friends'],
    #         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    #         'FIELDS': [
    #             'id',
    #             'email',
    #             'name',
    #             'first_name',
    #             'last_name',
    #             'verified',
    #             'locale',
    #             'timezone',
    #             'link',
    #             'gender',
    #             'updated_time'],
    #         'EXCHANGE_TOKEN': True,
    #         'LOCALE_FUNC': lambda request: 'en_US',
    #         'VERIFIED_EMAIL': True,
    #         'VERSION': 'v2.9'}}



