from flask import Flask
from app.config import Config
app = Flask(__name__, static_folder=Config.STATIC_PATH)
app.config.from_object(Config)

from app import route
