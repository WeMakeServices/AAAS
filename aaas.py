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

string_number_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_mapped_val(val):
    if val in string_number_mapping:
        return string_number_mapping[val]
    
    return val

@app.route("/<x>/<y>", methods=["GET"])
@cross_origin(support_credentials=True)
@limiter.limit("1 per day")
def add(x, y):
    try:
        x = int(get_mapped_val(x))
        y = int(get_mapped_val(y))
    except:
        return "Bad request", 400

    # Bounds check
    if x >= 10 or y >= 10 or x <= 0 or y <= 0:
        return "Bad request", 400

    return str(x + y), 200


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
