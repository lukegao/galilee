import os
from .base import *

DEBUG = False

# Read settings from environment variables
env = os.environ.copy()

# Secret_key
SECRET_KEY = env['SECRET_KEY']

# AWS S3 settings
AWS_STORAGE_BUCKET_NAME = 'luke-gao-devlog'
AWS_REGION_NAME = 'ap-northeast-2'
AWS_ACCESS_KEY_ID = env['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = env['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_DEFAULT_ACL = None

# not sure about the effect of host headers
ALLOWED_HOSTS = ['*']


try:
    from .local import *
except ImportError:
    pass
