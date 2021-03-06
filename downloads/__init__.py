from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import gevent
from gevent import monkey

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()

app = Flask(__name__)
app.config.from_object('config')
db =SQLAlchemy(app)

import logging
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler('tmp/downloads.log', 'a', 1 * 1024 * 1024, 10)
#
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)
app.logger.info('===startup downloader===')
log = app.logger.info
log2= app.logger.debug

from downloads import file_manager
from file_downloader import FileDownloader

Downloads = FileDownloader()

