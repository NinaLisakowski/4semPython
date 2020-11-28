# Exercise2:
# 1. Make a simple flask server with one, get endpoint /wiki/randomNodes.
#    1. Make it write Hello World.
# 2. Edit the /wiki/randomNodes endpoint to print the randomly generated node, and all the neightboring nodes.

from flask import Flask, jsonify, abort, request
from sqlalchemy.types import Integer, Text
import sqlalchemy as s_a
import pandas as pd

app = Flask(__name__)

@app.route('/flask_app/')
def index():
    return 'Hello world! Flask server week 9'

@app.route('/wiki/randomNodes')
def randomNodes():
    return "Random nodes";
