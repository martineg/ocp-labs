import os, time
from flask import Flask, request, jsonify, abort, redirect, url_for, render_template
from flask_healthz import healthz, HealthError
from flask_redis import FlaskRedis
from redis import ConnectionError

app = Flask(__name__)
app.register_blueprint(healthz, url_prefix="/healthz")
redis_client = FlaskRedis(app)

APP_HEALTH_OK = True
APP_VERSION = 1.0
FEATURES = [ (feat, os.environ.get(feat)) for feat in os.environ if feat.startswith("FEAT_")]
REDIS_URL = os.environ.get("REDIS_URL")

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1) + fib(n-2)

def healthy():
    if not APP_HEALTH_OK:
        raise HealthError("error")
    else:
        return "ok"
def liveness():
    print(healthy())

def readiness():
    print(healthy())
app.config.update(
    HEALTHZ = {
        "live" : "app.liveness",
        "ready" : "app.readiness",
    }
)

@app.route("/")
def index():
    try:
        redis_client.incr("counter")
        current_hits = redis_client.get("counter").decode()
    except ConnectionError:
        current_hits = "not available"
    if request.is_json:
        return redirect(url_for("version"))
    else:
        return render_template('index.html',
                            version=APP_VERSION,
                            name=os.environ.get("HOSTNAME", "localhost"),
                            features=dict(FEATURES),
                            current_hits=current_hits)


@app.route("/version")
def version():
    try:
        current_hits = redis_client.get("counter").decode() or 0
    except ConnectionError:
        current_hits = None
    return jsonify(version=APP_VERSION, features=FEATURES,
        hostname=os.environ.get("HOSTNAME", "localhost"),
        hits=current_hits)

@app.route("/invalidate")
def invalidate():
    global APP_HEALTH_OK
    APP_HEALTH_OK = False

    abort(500)

@app.route("/reset")
def reset_counter():
    try:
        redis_client.set("counter", 0)
    except ConnectionError:
        abort(500)
    else:
        return("OK")

@app.route("/fibonacci/<int:fib_num>")
def fibonacci(fib_num):
    request_start_time = time.time()
    res = fib(fib_num)
    return jsonify(fibonacci=res,
                   elapsed_time=time.time() - request_start_time)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)