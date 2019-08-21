#!/usr/bin/env python3

from flask import jsonify, request
from .run import app
from general_trader import loader

@app.route('/')
def root():
    return jsonify({"test":"works"})

@app.route('/input', methods=['POST'])
def ticker_loader():
    ticker1 = request.json['ticker1']
    ticker2 = request.json['ticker2']
    return loader.loader(ticker1,ticker2)
