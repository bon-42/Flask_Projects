from flask import Flask, jsonify
import requests

app = Flask(__name__)

# get response from api and convert to string
response = requests.get("https://api.coincap.io/v2/rates")


@app.route("/")
def currency():
    return response.json()


# manipulate the response to only get the bitcoin info
@app.route("/bitcoin", methods=["GET"])
def bitcoin_price():
    data = response.json()["data"]

    price = NotImplemented
    for item in data:
        if item["id"] == "bitcoin":
            price = item
    return jsonify(price["rateUsd"])
