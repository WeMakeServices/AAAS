from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr
from flask_cors import CORS, cross_origin
import random
app = Flask(__name__)
CORS(app, support_credentials=True)

limiter = Limiter(
    app,
    key_func=lambda: request.headers["X-Real-Ip"],
)

@app.route('/<x>/<y>', methods=['GET'])
@cross_origin(support_credentials=True)
@limiter.limit("1 per day")
def add(x, y):
    try:
        x = int(x)
        y = int(y)
    except:
        return "Bad request", 400

    # Bounds check
    if x >= 10 or y >= 10 or x <= 0 or y <= 0:
        return "Bad request", 400

    return str(x + y), 200