import json

from model import db
from model import LogType, Log, Summary


def reset_logtype():
    db.drop_tables([LogType])
    db.create_tables([LogType])
    log_types = json.load(open('db/init/type.json'))
    LogType.insert_many(log_types).execute()


def reset_log():
    db.drop_tables([Log])
    db.create_tables([Log])
    logs = json.load(open('db/init/log.json'))
    Log.insert_many(logs).execute()


def reset_summary():
    db.drop_tables([Summary])
    db.create_tables([Summary])
    summaries = json.load(open('db/init/summary.json'))
    Summary.insert_many(summaries).execute()


def init():
    reset_logtype()
    reset_log()
    reset_summary()


def update_log():
    logs = json.load(open('db/init/log.json'))
    Log.insert_many(logs).on_conflict(action='IGNORE').execute()


if __name__ == '__main__':
    update_log()
