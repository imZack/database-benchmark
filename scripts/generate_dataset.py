#!/usr/bin/env python

# {"topic": "/equs/My ioLogik-E2242", "payload": {"at": "2015-07-06T14:51:31Z"
# ,"tags": [{"id": "di0", "value": 1}, ...]}}
from __future__ import print_function
import datetime
import string
import copy
import msgpack
from random import uniform

tags = [_ for _ in string.lowercase]
start_time = datetime.datetime.utcnow()
output = open("dataset", "w")
for equs_id in xrange(1, 100):
    equs_time = copy.deepcopy(start_time)
    for tag_index in xrange(1, 60 * 60):  # 1 day / per second
        equs_time = equs_time + datetime.timedelta(0, 1)
        obj = {
            "eqid": str(equs_id),
            "at": equs_time.isoformat(),
            "tag": '',
            "value": ''
        }

        for tag in tags:
            obj["tag"] = tag
            obj["value"] = uniform(0, 9)
            # output.write(json.dumps(obj) + "\n")
            output.write(msgpack.packb(obj))

    print (str(equs_id) + " has been generated.")

output.write('\n')
output.close()
print ("All done.")
