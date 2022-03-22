import random
import time


from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
PrometheusMetrics(app)


@app.route("/hello")
def first_route():
    time.sleep(random.random() * 0.2)
    return "Hello World!", 200

@app.route("/health")
def health():
    time.sleep(random.random() * 0.3)
    return "OK", 200

@app.route("/error")
def oops():
    time.sleep(random.random() * 0.4)
    return ":(", 500


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, threaded=True)
