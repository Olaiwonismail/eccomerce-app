
import os
class Config:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
    SECRET_KEY='b30bb8384e15acbc267f8cb0f1b94c84'
    MAIL_SERVER='smtp.gmail.com'
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SQLALCHEMY_DATABASE_URI =  os.getenv('SQLALCHEMY_DATABASE_URI')
    # MAIL_PORT=587
    # MAIL_USE_TLS=True
    # MAIL_USE_SSL=False
    # MAIL_USERNAME='olaiwonismail@gmail.com'
    # MAIL_PASSWORD='oladayo@14'