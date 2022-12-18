import json
from flask import Flask, request, jsonify, abort
import logging

app = Flask(__name__)
globalName = ""

@app.route("/")
def index():
    return jsonify({"status":"success"})

@app.route("/getRecommendation", methods=["GET"])
def getName():
    user = request.args.get("user")
    app.logger.info("User " + str(user) + " recommended " + \
 "Movie1, Movie2, Movie3")
    return jsonify({"status":"success!"})

app.run(host='0.0.0.0', port=5101)