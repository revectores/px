import peewee
from enum import Enum
from config import Config

db = peewee.SqliteDatabase(Config.SQLITE3_DATABASE_PATH)


class SummaryType(Enum):
    RANGE    = 0
    DATE     = 1
    WEEK     = 2
    MONTH    = 3
    YEAR     = 4


class LogType(peewee.Model):
    id       = peewee.FixedCharField(36, primary_key=True)
    name     = peewee.CharField()
    parent   = peewee.FixedCharField(36, null=True)
    color    = peewee.CharField()

    class Meta:
        database = db


class Log(peewee.Model):
    id       = peewee.FixedCharField(36, primary_key=True)
    start    = peewee.DateTimeField()
    end      = peewee.DateTimeField()
    type     = peewee.FixedCharField(36)
    comment  = peewee.CharField()

    class Meta:
        database = db


class Summary(peewee.Model):
    id       = peewee.IntegerField(primary_key=True)
    start    = peewee.DateTimeField()
    end      = peewee.DateTimeField()
    type     = peewee.IntegerField()
    content  = peewee.CharField()

    class Meta:
        database = db


class Project(peewee.Model):
    id          = peewee.IntegerField(primary_key=True)
    name        = peewee.CharField()
    description = peewee.CharField()

    class Meta:
        database = db
