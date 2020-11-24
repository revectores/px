from flask import Flask
from app import app


from app.handler.summary.summary import summary, summary_api
from app.handler.log.log import log, log_api

app.register_blueprint(summary,     url_prefix="/summary")
app.register_blueprint(log,         url_prefix="/log")
app.register_blueprint(summary_api, url_prefix="/api/summary")
app.register_blueprint(log_api,        url_prefix="/api/log")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

