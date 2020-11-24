import os


class Config:
    DEBUG = True
    SQLITE3_DATABASE_PATH = os.environ.get('DB_PATH')


if __name__ == '__main__':
    print(Config.SQLITE3_DATABASE_PATH)