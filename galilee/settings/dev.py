from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6nw1qcnsrljhwrt+leu8u9=iyn0ddj-o)i!=bfwwq%kb1a$dt%'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

try:
    from .local import *
except ImportError:
    pass
