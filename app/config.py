import os


class Config:
    DEBUG = True
    SQLITE3_DATABASE_PATH = os.environ.get('DB_PATH')
    FRONTEND_PATH = os.environ.get('FRONTEND_PATH')
    STATIC_PATH = FRONTEND_PATH + '/static'
