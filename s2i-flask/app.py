import os
from flask import Flask, jsonify, abort, redirect, url_for

app = Flask(__name__)

APP_HEALTH_OK = True
APP_VERSION=1.0

@app.route("/")
def index():
  return "Hello OCP world from {} running version {}".format(os.environ.get('HOSTNAME', 'localhost'), APP_VERSION)

@app.route("/healthz")
def healthz():
  if APP_HEALTH_OK:
    return jsonify(healthy=APP_HEALTH_OK, version=APP_VERSION)
  else:
    abort(500)

@app.route("/invalidate")
def invalidate():
  global APP_HEALTH_OK
  APP_HEALTH_OK = False
  
  abort(500)

app.run(host="0.0.0.0", port=8080, debug=True)
