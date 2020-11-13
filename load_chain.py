#!/usr/bin/env python3

import os
import requests as rq

ZAPIER_TOKEN = os.environ['ZAPIER_TOKEN']

CBOE_URL = 'https://markets.cboe.com/us/options/market_statistics/historical_data/download/all_symbols/'
CBOE_FILE = 'optionvolume.csv'
payload = {'reportType': 'volume',
            'month': '',
            'year': '2020',
            'volumeType': 'sum',
            'volumeAggType': 'daily',
            'exchanges': ['CBOE', 'BATS', 'EDGX', 'C2']}
# ?reportType=volume&month=2&year=2020&volumeType=sum&volumeAggType=daily&exchanges=CBOE&exchanges=BATS&exchanges=C2&exchanges=EDGX

with open(CBOE_FILE, 'wb') as f, \
        rq.get(CBOE_URL, params=payload) as r:
    for line in r.iter_lines():
        f.write(line)
