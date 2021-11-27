from flask import Flask
from app.config import Config
app = Flask(__name__, static_folder=Config.STATIC_PATH)
app.config.from_object(Config)

from app.route import register_blueprints
register_blueprints()

if __name__ == '__main__':
    app.run()
