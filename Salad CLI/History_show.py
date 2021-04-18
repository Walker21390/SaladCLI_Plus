import os
import sys
import json
import dateutil.parser
import datetime
import math
import time
import ast
import argparse
from time import sleep

# This very epic thing is made by SharkOfGod!

sys.stdout.write("\x1b]2;Earning History\x07")

height, file, sdate, month, color, mini, monthly, weekly, rev = None, None, None, None, None, False, False, False, False
parser = argparse.ArgumentParser(description='salad graph thing')
parser.add_argument('-a', '--asd', action='store_true',
                    required=False, help='beans')
parser.add_argument('-s', '--smh', action='store_true',
                    required=False, help='beans')
parser.add_argument('-f', '--file', action='store',
                    required=True, help='file to read from')
parser.add_argument('-d', '--day', action='store',
                    required=False, help='day to select')
parser.add_argument('-m', '--month', action='store',
                    required=False, help='month to select')
parser.add_argument('--height', action='store',
                    required=False, help='height of graph', type=int)
parser.add_argument('--ansi_color', action='store',
                    required=False, help='color of graph')
parser.add_argument('-min', '--minified', action='store_true',
                    required=False, help='small graph')
parser.add_argument('--countmonth', action='store_true',
                    required=False, help='count earnings in month')
parser.add_argument('--countweekly', action='store_true',
                    required=False, help='count earnings by week')
parser.add_argument('--countdaily', action='store_true',
                    required=False, help='count earnings by day')
parser.add_argument('-rev', '--reverse', action='store_true',
                    required=False, help='print graph backwards')
args = parser.parse_args()
beans = args.asd
goose = args.smh
sdate = args.day
rev = args.reverse
month = args.month
file = args.file
height = args.height
daily = args.countdaily
if beans:
    tme = datetime.datetime.strptime(datetime.datetime.fromtimestamp(
        int(time.time())).strftime('%m-%d'), '%m-%d')
    month = int(tme.month)
    sdate = str(tme.day)
    month = str(month) if month > 10 else '0' + str(month)
try:
    color = args.ansi_color.encode().decode('unicode-escape')
except:
    pass
mini = args.minified
monthly = args.countmonth
weekly = args.countweekly
# for i, arg in enumerate(sys.argv):
# 	if arg == '--height':
# 		height = int(sys.argv[i+1])
# 	elif arg == '--file':
# 		file = sys.argv[i+1]
# 	elif arg == '--day':
# 		sdate = sys.argv[i+1]
# 	elif arg == '--month':
# 		month = sys.argv[i+1]
# 	elif arg == '--ansi_color':
# 		color = sys.argv[i+1].encode().decode('unicode-escape') # fuck you python
# 	elif arg == '--minified':
# 		mini = True
# 	elif arg == '--countmonthly':
# 		monthly = True
# 	elif arg == '--countweekly':
# 		weekly = True
# 	elif arg == '--reversed':
# 		rev = True

if not height:
    height = 5
if not file or not sdate or not month:
    print('missing arguments')
    exit()
with open(file) as f:
    js = json.load(f)
new = {}
for item in js:
    dt = int(dateutil.parser.parse(item).timestamp())
    # salads data error fix - pls fix the damn 15 mins off bug
    changes = {}
    thistime = str(datetime.datetime.fromtimestamp(dt).strftime('%m/%d/%H/%M'))
    changes['month'] = thistime.split('/')[0]
    changes['minutes'] = int(thistime.split('/')[3])
    changes['hours'] = int(thistime.split('/')[2])
    changes['days'] = int(thistime.split('/')[1])
    if changes['minutes'] == 45:
        if changes['hours'] == 23:
            changes['days'] += 1  # this ignores months but whatever
            changes['hours'] = 0
            changes['minutes'] = '00'
        else:
            changes['hours'] += 1
            changes['minutes'] = '00'
    else:
        changes['minutes'] += 15

    if changes['hours'] < 10:
        changes['hours'] = '0' + str(changes['hours'])

    if changes['days'] < 10:
        changes['days'] = '0' + str(changes['days'])

    thistime = str(changes['month']) + '/' + str(changes['days']) + \
        '/' + str(changes['hours']) + '/' + str(changes['minutes'])

    new[thistime] = js[item]

show = {
    "heights": {},
    "values": {}
}
top = 0
bottom = 0
total = 0
if daily:
    total = 0
    oldday = 0
    for i, item in enumerate(new):
        if item.split('/')[0] == month:
            if not oldday:
                oldday = item.split('/')[1]
            if item.split('/')[1] == oldday:
                total += new[item]
            else:
                print('\u001b[1m\u001b[33mtotal earned day ' +
                      str(oldday) + ': ' + str(total))
                oldday = item.split('/')[1]
                total = 0
    exit()

if weekly:
    e = -1
    h = 1
    oldday = 0
    for i, item in enumerate(new):
        if item.split('/')[0] == month:
            if e == 7:
                print('\u001b[1m\u001b[33mtotal earned week ' +
                      str(h) + ': ' + str(total))
                total = 0
                h += 1
                e = 0
            else:
                total += new[item]
                if item.split('/')[1] != oldday:
                    oldday = item.split('/')[1]
                    e += 1
    if e > 0:
        print('\u001b[1m\u001b[33mtotal earned week ' +
              str(h) + ': ' + str(total))
    exit()
if monthly and month:
    for i, item in enumerate(new):
        if item.split('/')[0] == month:
            total += new[item]
    print('\u001b[1m\u001b[33mtotal earned in selected month: ' + str(total))
    exit()
if sdate and month:
    for i, item in enumerate(new):
        if item.split('/')[1] == sdate and item.split('/')[0] == month:
            if new[item] > top:
                top = new[item]
            if new[item] < bottom:
                bottom = new[item]
            total += new[item]
#print(top, bottom)
d = top / height
for i in range(0, height):
    show['heights'][str(i)] = d*i
show['heights'][str(height)] = top
# print(show['heights'])
if sdate and month:
    for i, item in enumerate(new):
        if item.split('/')[1] == sdate and item.split('/')[0] == month:
            temp = {}
            for h in show['heights']:
                temp[h] = new[item]-show['heights'][h]
            teemp = []
            for t in temp:
                teemp.append(abs(temp[t]))
                n = min(teemp)
            for t in temp:
                if abs(temp[t]) == n:
                    tnum = t
            show['values'][item.split('/')[2] + ':' +
                           item.split('/')[3]] = tnum
# print(show['values'])
text = ''
positions = {}
nums = 0
if color:
    print(color, end='\r')

with open('art.txt', encoding='utf-8') as f:
    art = f.read()

color = '0A'
os.system('color ' + color)

print(art)

if not goose:

    print('Total earned today: \u001b[1m\u001b[33m$' + str(total))
    print(' \u001b[32m')
    print('-------------------------------------')
    print('Press ctrl+c to Return!')

else:

    print('Total earned today: \u001b[1m\u001b[33m$' + str(total))
    print(' \u001b[32m')
    print('-------------------------------------')
    print(' ')

    if not mini:
        for i in reversed(range(0, height+1)):
            rnded = str(math.floor(show['heights'][str(i)]*10000)/10000)
            if len(rnded) > nums:
                nums = len(rnded)
        for i in reversed(range(0, height+1)):
            rnded = math.floor(show['heights'][str(i)]*10000)/10000
            while len(str(rnded)) < nums:
                rnded = str(rnded) + '0'
            text = str(rnded) + ' : '
            if not rev:
                for k, v in show['values'].items():
                    try:
                        if int(v) == i or positions[k]:
                            text = text + '  *   '
                            positions[k] = True
                        else:
                            text = text + '      '
                    except:
                        if int(v) == i:
                            text = text + '  *   '
                            positions[k] = True
                        else:
                            text = text + '      '
                            positions[k] = False
            else:
                for k in sorted(show['values']):
                    v = show['values'][k]
                    try:
                        if int(v) == i or positions[k]:
                            text = text + '  *   '
                            positions[k] = True
                        else:
                            text = text + '      '
                    except:
                        if int(v) == i:
                            text = text + '  *   '
                            positions[k] = True
                        else:
                            text = text + '      '
                            positions[k] = False
            print(text)
            text = ''
        for i in range(0, nums):
            text = text + ' '
        text = text + '   '
        if not rev:
            for day in show['values']:
                text = text + day + ' '
        else:
            for day in sorted(show['values']):
                text = text + day + ' '
        print(text)
    else:
        for a in show['values']:
            for b in sorted(show['values']):
                if not rev:
                    print(
                        '\u001b[33mShowing from: from ' + a + ' to: ' + b)
                    print(" ")
                else:
                    print('\u001b[33mShowing from: ' +
                          b + ' to: ' + a)
                    print(" ")
                break
            break
        for i in reversed(range(0, height+1)):
            rnded = str(math.floor(show['heights'][str(i)]*10000)/10000)
            if len(rnded) > nums:
                nums = len(rnded)
        for i in reversed(range(0, height+1)):
            rnded = math.floor(show['heights'][str(i)]*10000)/10000
            while len(str(rnded)) < nums:
                rnded = str(rnded) + '0'
            text = str(rnded) + ' : '
            if not rev:
                for k, v in show['values'].items():
                    try:
                        if int(v) == i or positions[k]:
                            text = text + ' *'
                            positions[k] = True
                        else:
                            text = text + '  '
                    except:
                        if int(v) == i:
                            text = text + ' *'
                            positions[k] = True
                        else:
                            text = text + '  '
                            positions[k] = False
            else:
                for k in sorted(show['values']):
                    v = show['values'][k]
                    try:
                        if int(v) == i or positions[k]:
                            text = text + ' *'
                            positions[k] = True
                        else:
                            text = text + '  '
                    except:
                        if int(v) == i:
                            text = text + ' *'
                            positions[k] = True
                        else:
                            text = text + '  '
                            positions[k] = False
            print(text)
    print(' \u001b[32m')
    print('-------------------------------------')
    print('Press ctrl+c to Return!')

while True:
    try:
        sleep(5)
    except KeyboardInterrupt:
        print("Quitting...")
        os.system('python "Start.py"')
