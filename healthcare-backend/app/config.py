import secrets
import os

class Config:
    SECRET_KEY = secrets.token_hex(32)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://username:password@localhost/db_name')
    SQLALCHEMY_TRACK_MODIFICATIONS=False