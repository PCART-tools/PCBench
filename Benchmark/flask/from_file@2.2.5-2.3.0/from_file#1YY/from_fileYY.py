import json
from flask import Flask
app = Flask(__name__)
app.config.from_file('./test.json',  json.load)
