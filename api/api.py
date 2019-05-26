#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import json
from flask_cors import CORS
from handling.handling import handling as hd
from handling.handling import return_reply

app = Flask(__name__)
CORS(app, supports_credentials=True)

result = {}
intent = []
sentence_activated = []


@app.route("/input", methods=['POST'])
def input():
    body = request.get_json()
    if body['input'].strip() != '':
        result['content'] = body['input'].lower()
    return json.dumps(body), 200


@app.route("/output", methods=['POST'])
def output():
    body = result['content']
    sentence_activated.append(body)
    kb = hd(body)
    intent.append(kb)
    traloi = return_reply(intent=intent, sentence_activated=sentence_activated)
    print(traloi)
    return json.dumps(traloi), 200


if __name__ == "__main__":
    app.run(debug=True, port=9333)
