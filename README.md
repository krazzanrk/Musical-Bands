# django-allauth

### Installation

pip install django-allauth

### setting.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Already defined Django-related contexts here

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    ...
    ### Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
)

INSTALLED_APPS = (
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

SITE_ID = 1

### Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        ### For each OAuth based provider, either add a ``SocialApp``
        ### (``socialaccount`` app) containing the required client
        ### credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}


### urls.py:

urlpatterns = [
    ...
    url(r'^accounts/', include('allauth.urls')),
    ...
]

### post installation
./manage.py migrate




 ### Refrences:
 https://django-allauth.readthedocs.io/en/latest/installation.html
 https://www.codementor.io/@rishabh_ags/django-allauth-tutorial-social-logins-bqj8gk7cd
 