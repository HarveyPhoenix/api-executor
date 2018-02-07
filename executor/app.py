#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests
import os
from flask import Flask
from flask import request, Response, abort, jsonify
import config
from executor.utils.logger import logger

## init logger https://github.com/senko/python-logger/blob/master/logger.py
logger.basicConfig()

app = Flask(__name__)

@app.route(config.FLASK_URI_STATUS, methods=['GET'])
def executor_status():
    if not request.method == 'GET':
        abort(400)
        return
    ## get params
    logger.debug("user input request.args %r" % (request.args))
    ## get headers dict
    real_ip = request.headers.get('X-Real-IP')
    logger.info("GET header X-Real-IP %r" % (real_ip))
    cmd = config.CMD_URI_STATUS
    res_cmd = os.popen(cmd).read()
    logger.info("CMD RESULT = %r" % (res_cmd))
    results = {
            "cmd": cmd,
            "result": res_cmd
        }
    return (jsonify(results), 200)

@app.route(config.FLASK_URI, methods=['GET'])
def executor_main():
    if not request.method == 'GET':
        abort(400)
        return
    ## get params
    logger.debug("user input request.args %r" % (request.args))
    ## get headers dict
    real_ip = request.headers.get('X-Real-IP')
    logger.info("GET header X-Real-IP %r" % (real_ip))
    cmd = config.CMD_URI_MAIN
    res_cmd = os.popen(cmd).read()
    logger.info("CMD RESULT = %r" % (res_cmd))
    results = {
            "cmd": cmd,
            "result": res_cmd
        }
    return (jsonify(results), 200)
