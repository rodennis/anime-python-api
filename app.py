from flask import Flask
from flask import request
from flask import jsonify

from peewee import *
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

db = PostgresqlDatabase('anime', user='postgres', password='', host='localhost', port=5432)

app.run(port=3000, debug=True)