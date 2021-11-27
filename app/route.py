from app import app
from app.handler.summary import summary, summary_api
from app.handler.log import log, log_api

def register_blueprints():
    app.register_blueprint(summary, url_prefix="/summary")
    app.register_blueprint(log, url_prefix="/log")
    app.register_blueprint(summary_api, url_prefix="/api/summary")
    app.register_blueprint(log_api, url_prefix="/api/log")
