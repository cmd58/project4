import logging
import os
from logging.config import dictConfig

import flask
from flask import request, current_app

#from app.logging_config.log_formatters import RequestFormatter
from app import config

log_con = flask.Blueprint('log_con', __name__)


#@log_con.before_app_request
#def before_request_logging():