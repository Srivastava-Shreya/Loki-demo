import json
from flask import Flask, request, jsonify, abort
import logging

app = Flask(__name__)
globalName = ""

@app.route("/")
def index():
    return jsonify({"status":"success"})

@app.route("/getMovie", methods=["GET"])
def getName():
    user = request.args.get("user")
    movie = request.args.get("movie")
    app.logger.info("User " + str(user) + " requested to watch movie " + str(movie))
    return jsonify({"status":"success!"})

app.run(host='0.0.0.0', port=5100)