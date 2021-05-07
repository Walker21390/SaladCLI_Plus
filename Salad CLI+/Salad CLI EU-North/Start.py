import os
import time
import requests
import sys
import pyperclip
import json
import webbrowser

sys.stdout.write("\x1b]2;Salad CLI+\x07")
refresh_time = 15  # seconds
color = '0A'  # like u would type "color 0A" into cmd / leave empty for default
os.system("mode 200,50")

with open('config.json') as f:
    js = json.load(f)
salad_auth = js['salad_key']
cookie = {
    "Salad.Authentication": salad_auth
}
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Salad/0.4.2 Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
}
with open('Login screen.txt', encoding='utf-8') as f:
    loginscreen = f.read()
os.system('color ' + color)

sladusr = requests.get(
    url='https://app-api.salad.io/api/v1/profile', headers=headers, cookies=cookie)
if sladusr.status_code != 200:
    print('REPLACE YOUR SALAD AUTH CODE!')
    os.system('pause')
    exit()
sladusr = sladusr.json()

rfrl = requests.get(url='https://app-api.salad.io/api/v1/profile/referral-code',
                    headers=headers, cookies=cookie)
if rfrl.status_code != 200:
    print('REPLACE YOUR SALAD AUTH CODE!')
    os.system('pause')
    exit()
rfrl = rfrl.json()

print(loginscreen)
print(u'\u001b[33mUsername: ' + str(sladusr['username']))
print('Email: ' + str(sladusr['email']))
print('User id: ' + str(sladusr['id']))
print(" ")
print(" ")
print(" ")


# input selection
select = input(
    u"Select option! \n1. Balance \n2. Lifetime \n3. XP \n4. Earning History \n5. Copy Referral Code \n6. Start mining! \n7. Salad Store\n\nSelect: ")
if select == "1" or select == "Balance":
    os.system('python Balance.py')

if select == "2" or select == "Lifetime":
    os.system('python Lifetime.py')

if select == "3" or select == "XP":
    os.system('python XP.py')

if select == "4" or select == "Earning History":
    os.system('python salad_earnings_update.py')

if select == "5" or select == "Copy Referral Code":
    pyperclip.copy('Join me on Salad and use code ' +
                   str(rfrl['code']) + ' for a 2x earning rate bonus! https://www.salad.io')
    print('Code copied to clipboard!')

if select == "6" or select == "Start mining":
    os.system('python Mining.py')

if select == "7" or select == "Salad store":
    webbrowser.open('http://app.salad.io')
time.sleep(2)
os.system('python Start.py')
