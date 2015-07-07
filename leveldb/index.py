#!/usr/bin/env python
from sys import stdin
import plyvel
import simplejson as json

db = plyvel.DB('/mnt/data/leveldb/', create_if_missing=True)

for line in stdin:
    obj = json.loads(line)
    db.put(obj["topic"] + "-" + obj["payload"]["at"], line)

db.close()
