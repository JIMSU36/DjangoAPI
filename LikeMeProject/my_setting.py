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
SECRET_KEY ='django-insecure-+qzl*9(omqwlmtypd6ks+_h2271h!%u@%3ht+6v#7n9=@razzo'