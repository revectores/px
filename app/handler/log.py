from datetime import datetime
from flask import jsonify, Blueprint

from app.model import LogType, Log
from app.utils import models_to_dict, date_str2date_range

log = Blueprint('log', __name__)
log_api = Blueprint('log_api', __name__)


@log_api.route('/type')
def get_log_types():
    log_types = LogType.select()
    return jsonify(models_to_dict(log_types))


@log_api.route('/date/<date_str>')
def date_logs(date_str):
    date_start, date_end = date_str2date_range(date_str)
    query = Log.select().where((Log.start < date_end) & (Log.end > date_start))
    logs = models_to_dict(query)
    for id in logs:
        if datetime.fromisoformat(logs[id]['start']) < date_start:
            logs[id]['start'] = str(date_start)
        if datetime.fromisoformat(logs[id]['end']) > date_end:
            logs[id]['end'] = str(date_end)
    return jsonify(logs)
