'''from flask_sqlalchemy import SQLAlchemy
import boto3
import os
from flask_wtf import CSRFProtect

db = SQLAlchemy()

s3 = boto3.client('s3',
                  aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                  aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                  region_name=os.environ['AWS_REGION'])

S3_BUCKET = os.environ['S3_BUCKET_NAME']'''

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import os
import boto3

# Initialize SQLAlchemy
db = SQLAlchemy()

# Initialize CSRF protection
csrf = CSRFProtect()

# Initialize S3 client if AWS keys are available
if 'AWS_ACCESS_KEY_ID' in os.environ and 'AWS_SECRET_ACCESS_KEY' in os.environ:
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        region_name='ap-southeast-1'
    )
else:
    s3 = None
