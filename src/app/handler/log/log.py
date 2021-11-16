from zoneinfo import ZoneInfo
from datetime import datetime, timedelta, timezone
from flask import render_template, redirect
from playhouse.shortcuts import dict_to_model, model_to_dict

from flask import Blueprint, render_template, send_from_directory, jsonify
from app.model import LogType, Log
from app.utils import models_to_dict, date_str2date_range

from pprint import pprint


log     = Blueprint('log', __name__)
log_api = Blueprint('log_api', __name__)


@log_api.route('/type')
def get_log_types():
    log_types = LogType.select()
    return jsonify(models_to_dict(log_types))


# @log_api.route('/range/<start>/<end>')



@log_api.route('/date/<date_str>')
def date_logs(date_str):
    date_start, date_end = date_str2date_range(date_str)
    query = Log.select().where((Log.start < date_end) & (Log.end > date_start))
    logs = models_to_dict(query)
    return jsonify(logs)



@log_api.route('/week/<week_index>')
def week_logs(week_index):
    pass

