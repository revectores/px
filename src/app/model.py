import json
import peewee
from enum import Enum
from playhouse.shortcuts import dict_to_model, model_to_dict
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from pprint import pprint
from config import Config

db = peewee.SqliteDatabase(Config.SQLITE3_DATABASE_PATH)


"""
class LogType(Enum):
    MANAGEMENT = 0
    SKILLS     = 1
    DEVELOP    = 2
    HEALTH     = 3
    NETWORKING = 4
    ROUTINES   = 5
    ENTERTAIN  = 6
"""


class SummaryType(Enum):
    RANGE    = 0
    DATE     = 1
    WEEK     = 2
    MONTH    = 3
    YEAR     = 4


class LogType(peewee.Model):
    id       = peewee.IntegerField(primary_key=True)
    name     = peewee.CharField()
    depth    = peewee.IntegerField()
    parent   = peewee.IntegerField()
    color    = peewee.CharField()

    class Meta:
        database = db


class Log(peewee.Model):
    id       = peewee.IntegerField(primary_key=True)
    start    = peewee.DateTimeField()
    end      = peewee.DateTimeField()
    type     = peewee.IntegerField()
    reported = peewee.BooleanField()
    report   = peewee.CharField()

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


if __name__ == '__main__':

    MODELS = [LogType, Log, Summary, Project]
    db.drop_tables(MODELS)
    db.create_tables(MODELS)
    types = json.load(open('db/init/type.json'))
    
    logs  = json.load(open('db/init/log.json'))
    for log in logs:
        log['start'] = datetime.fromtimestamp(log['start']).replace(tzinfo=ZoneInfo('Asia/Shanghai'))
        log['end'] = datetime.fromtimestamp(log['end']).replace(tzinfo=ZoneInfo('Asia/Shanghai'))

    summaries = json.load(open('db/init/summary.json'))
    for summary in summaries:
        summary['start'] = datetime.fromtimestamp(summary['start']).replace(tzinfo=ZoneInfo('Asia/Shanghai'))
        summary['end'] = datetime.fromtimestamp(summary['end']).replace(tzinfo=ZoneInfo('Asia/Shanghai'))

    LogType.insert_many(types).execute()
    Log.insert_many(logs).execute()
    Summary.insert_many(summaries).execute()

    # for log_type in types:
    #     print(log_type)
    #     dict_to_model(LogType, log_type).save(force_insert=True)


