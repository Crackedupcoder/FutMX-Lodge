from .base import *

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
# AWS_PRIVATE_BUCKET_NAME applies to s3-example-public-and-private only
AWS_STORAGE_BUCKET_NAME = 'Futmx-Lodge'
AWS_PRIVATE_BUCKET_NAME = 'Futmx-Lodge'
AWS_S3_REGION_NAME = 'us-east-005'
AWS_S3_ENDPOINT_URL = 'https://s3.us-east-005.backblazeb2.com'
AWS_S3_FILE_OVERWRITE = False

DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"
