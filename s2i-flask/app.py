import os
from flask import Flask, request, jsonify, abort, redirect, url_for, render_template

app = Flask(__name__)

APP_HEALTH_OK = True
APP_VERSION = 1.0
FEATURES = [ (feat, os.environ.get(feat)) for feat in os.environ if feat.startswith("FEAT_")]

# http://flask.pocoo.org/snippets/45/
def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

@app.route("/")
def index():
    if request_wants_json():
        return jsonify(message="Hello OCP world!", version=APP_VERSION,
                    hostname=os.environ.get("HOSTNAME", "localhost"),
                    features=dict(FEATURES))
    return render_template('index.html',
                           version=APP_VERSION,
                           name=os.environ.get("HOSTNAME", "localhost"),
                           features=dict(FEATURES))


@app.route("/version")
def version():
    return jsonify(version=APP_VERSION, features=FEATURES)


@app.route("/healthz")
def healthz():
    if APP_HEALTH_OK:
        return jsonify(healthy=APP_HEALTH_OK)
    else:
        abort(500)


@app.route("/invalidate")
def invalidate():
    global APP_HEALTH_OK
    APP_HEALTH_OK = False

    abort(500)


app.run(host="0.0.0.0", port=8080, debug=True)
