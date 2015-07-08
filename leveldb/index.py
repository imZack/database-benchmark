#!/usr/bin/env python
from sys import stdin
import simplejson as json
import msgpack
import requests

def insert_tags():
    objs = []
    unpacker = msgpack.Unpacker()
    for buff in stdin:
        unpacker.feed(buff)
        for o in unpacker:
            objs.append({
                "key": "%s$%s$%s" % (o["eqid"], o["tag"], o["at"]),
                "value": o["value"]
            })

        if len(objs) > 3600:
            r = requests.post('http://localhost:5000/batch', json=objs)
            objs = []

    if len(objs) > 0:
        r = requests.post('http://localhost:5000/batch', json=objs)
        objs = []

insert_tags()
