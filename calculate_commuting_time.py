# -*- coding: utf-8 -*-
import json
import requests

# http://map.amap.com/service/subway?_1592051499713&srhdata=3100_drw_shanghai.json
with open('subway.json') as f:
  data = json.load(f)

output = open("home1.csv", "w")

from_data = [
    # ('静安寺', "BV10025485"),
    # ('陆家嘴', "BV10029743"),
    # ('漕河泾开发区','BV10025213'),
    ('张江高科', 'BV10039897'),
]

#reading file
for from_stop, from_id in from_data:
    for line in data['l']:
        print(line['ln'])
        for stop in line['st']:
            log, lat = stop['sl'].split(',')
            # print (stop['n'], stop['sl'], stop['poiid'])
            url = 'https://gaode.com/service/nav/bus'
            payload = {
                'night': 0,
                'group': 1,
                'pure_walk': 1,
                'date': '2020-6-13',
                'time': '19-00',
                'eta': 1,
            }
            payload.update({
                'poiid1': from_id,
                'poiid2': stop['poiid']
            })
            r = requests.get(url, params=payload)
            data = r.json()
            print(data.keys())
            if 'data' in data:
                res = '{},{},{}\n'.format(from_stop, stop['n'], data['data']['buslist'][0]['expensetime'])
                output.write(res)
                print(res)

output.close()