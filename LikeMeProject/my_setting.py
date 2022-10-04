import json

from django.core.exceptions import ImproperlyConfigured

with open("secret.json") as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"Set the {setting} enviroment variable"
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'likeme', #2
        'USER': 'root', #3                      
        'PASSWORD': 'LikeMeDB1!',  #4              
        'HOST': '127.0.0.1',   #5                
        'PORT': '3306', #6
    }
}