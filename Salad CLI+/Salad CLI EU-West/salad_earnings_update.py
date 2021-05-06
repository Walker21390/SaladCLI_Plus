import requests
import json
import time
import sys
import os

sys.stdout.write("\x1b]2;Downloading History\x07")

headers = {
	"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Salad/0.4.0 Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
}

with open('config.json') as f:
    js = json.load(f)
salad_auth = js['salad_key']
cookie = {
	"Salad.Authentication": salad_auth
}

r = requests.get(url = 'https://app-api.salad.io/api/v2/reports/1-day-earning-history', cookies = cookie, headers = headers)
jason = r.json()
with open('data.json', 'w+') as f:
	f.write(json.dumps(jason))
print('Downloading data...')
time.sleep(2)

os.system('python "History_show.py" --asd -f data.json --smh -min -rev')