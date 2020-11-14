#!/usr/bin/env python3

import os
import shutil
import requests as rq

TRADIER_TOKEN = os.environ['TRADIER_TOKEN']
CKSIZE = 100000

CBOE_URL = 'https://markets.cboe.com/us/options/market_statistics/historical_data/download/all_symbols/'
CBOE_FILE = 'optionvolume.csv'
payload = {'reportType': 'volume',
            'month': '',
            'year': '2020',
            'volumeType': 'sum',
            'volumeAggType': 'daily',
            'exchanges': ['CBOE', 'BATS', 'EDGX', 'C2']}

with open(CBOE_FILE, 'wb') as f:
    with rq.get(CBOE_URL, params=payload, stream=True) as r:
        for chunk in r.iter_content(chunk_size=CKSIZE):
            f.write(chunk)
