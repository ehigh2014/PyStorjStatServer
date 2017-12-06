# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 10:19:24 2017

@author: ehigh
@email : ehigh2014@163.com
"""

from flask import Flask
from flask import request
from flask import Response
from flask_table import Table, Col
import redis

import logging 

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='server.log',
                filemode='w')

redis = redis.Redis(host='127.0.0.1', port=6379, db=0)

app = Flask(__name__)

class NodeItemTable(Table):
    name = Col('Name')
    node_id = Col('NodeID')
    address = Col('Address')
    port = Col("Port")
    allocs = Col('Allocs')
    shared = Col('Shared')
    timestamp = Col('TStamp')
    lastSeen = Col('LastSeen')
    responseTime = Col('ResponseTime')
   
def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

def get_node_list():
    nodes = []
    for node in redis.hvals('NodeHB'):
        if type(node) is str:
            node = eval(node)
        nodes.append(node)
    return nodes

@app.route('/hb', methods=['POST'])
def hb_post():
    hb = request.form.to_dict()
    redis.hset('NodeHB', hb['node_id'], hb)
    content = str(hb)
    return Response_headers(content)

@app.route('/nodes')
def get_nodes():
    try:
        nodes = get_node_list()
        table = NodeItemTable(nodes)
        return table.__html__()
    except Exception, e:
        logging.error(e)
        return "Nodes get error!"

def server_run():
    redis.hdel('NodeHB')
    logging.info("Start Server on port : 5000")
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    server_run()
    