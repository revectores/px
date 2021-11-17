from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
from playhouse.shortcuts import dict_to_model, model_to_dict


def models_to_dict(models):
    return {model.id: model_to_dict(model) for model in models}


def date_str2date_range(date_str):
    date_ = datetime.strptime(date_str, "%Y-%m-%d")
    date_start = date_.replace(tzinfo=ZoneInfo('Asia/Shanghai'))
    date_end   = (date_ + timedelta(days=1)).replace(tzinfo=ZoneInfo('Asia/Shanghai'))
    return date_start, date_end

