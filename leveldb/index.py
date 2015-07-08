#!/usr/bin/env python
from sys import stdin
import plyvel
Traceback (most recent call last):

import simplejson as json

def insert_data():
    db = plyvel.DB('/home/zack/leveldb/', create_if_missing=True)

    for line in stdin:
        obj = json.loads(line)
        db.put(obj["topic"] + "-" + obj["payload"]["at"], line)

    db.close()

result = benchmark(insert_data)
assert result is None
