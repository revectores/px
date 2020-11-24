from datetime import date, datetime, timedelta, timezone

from flask import Blueprint, render_template, send_from_directory, jsonify
from app.model import LogType, Log, Summary
from utils import models_to_dict, date_str2date_range
from playhouse.shortcuts import dict_to_model, model_to_dict



summary     = Blueprint('summary', __name__)
summary_api = Blueprint('summary_api', __name__)


@summary.route('/date/<summary_date_str>')
def html_date_summary(summary_date_str):
    return send_from_directory('templates/summary/', 'date_summary.html')



@summary_api.route('/date/<summary_date_str>')
def date_summary(summary_date_str):
    date_start, date_end = date_str2date_range(summary_date_str)
    print(date_start, date_end)

    date_summary = Summary.get_or_none((Summary.start == date_start) & (Summary.end == date_end))
    return date_summary.content if date_summary else ""
