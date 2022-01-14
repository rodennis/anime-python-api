from flask import Flask
from flask import request
from flask import jsonify

from peewee import *
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

db = PostgresqlDatabase('anime', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Facts(BaseModel):
    show_name = CharField()
    fact = CharField()

db.connect()
db.drop_tables([Facts])
db.create_tables([Facts])


@app.route('/', methods=['GET'])
def naruto():
    return jsonify('hello')

app.run(port=3000, debug=True)