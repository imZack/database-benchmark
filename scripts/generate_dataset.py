#!/usr/bin/env python

# {"topic": "/equs/My ioLogik-E2242", "payload": {"at": "2015-07-06T14:51:31Z"
# ,"tags": [{"id": "di0", "value": 1}, ...]}}
from __future__ import print_function
import datetime
import string
import copy
import simplejson as json
from random import uniform

tags = [_ for _ in string.lowercase]
start_time = datetime.datetime.utcnow()
output = open("/mnt/data/dataset", "w")
for equs_id in xrange(1, 100):
    equs_time = copy.deepcopy(start_time)
    for tag_index in xrange(1, 60 * 60):  # 1 day / per second
        equs_time = equs_time + datetime.timedelta(0, 1)
        obj = {
            "topic": "/equs/" + str(equs_id),
            "payload": {
                "at": equs_time.isoformat(),
                "tags": []
            }
        }
        for tag in tags:
            obj["payload"]["tags"].append({
                    "id": tag,
                    "value": uniform(0, 9)
                })
        output.write(json.dumps(obj) + "\n")

    print (str(equs_id) + " has been generated.")
print ("All done.")
