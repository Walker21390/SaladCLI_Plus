import os
import time
import requests
import sys
from time import sleep
import json
import subprocess

with open('config.json') as f:
    js = json.load(f)
wallet = js['wallet']

sys.stdout.write("\x1b]2;Choose miner...\x07")
refresh_time = 15  # seconds
color = '0A'  # like u would type "color 0A" into cmd / leave empty for default

os.system('color ' + color)
select = input(
    "Select miner! \n\n1. Phoenixminer 5.5c (GPU) \n2. XMRig 6.7.0 (CPU) \n3. XMRig-nVidia (GPU) \n4. XMRig-Amd (GPU) \n5. Gminer (GPU) \n6. NBMiner (GPU) \n7. ETHMiner (GPU) \n8. T-rex miner ETHASH (GPU) \n9. T-rex miner KAWPOW (GPU)\n10. Return to main menu\n\nSelect: ")
if select == "1" or select == "Phoenixminer":
    os.system("OptimizeGPU.bat")
    os.system("mode 230,60")
    os.system(r"Miners\PhoenixMiner-5.5c\PhoenixMiner.exe -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto.usa.nicehash.com:3353 -pool2 stratum+tcp://daggerhashimoto.eu.nicehash.com:3353 -ewal " + (wallet) + " -esm 3 -allpools 1 -allcoins 0")
if select == "2" or select == "XMrig CPU":
    os.system("cls")
    os.system("mode 230,60")
    os.system(r"Miners\XMRig-CPU-6.7.0\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380 --coin=monero -u " +
              (wallet) + r" -k --nicehash")
if select == "3" or select == "XMrig nVidia":
    os.system("OptimizeGPU.bat")
    os.system("mode 230,60")
    os.system(r"Miners\XMRig-6.7.0\xmrig.exe --no-cpu --cuda -a kawpow -o stratum+tcp://kawpow.usa.nicehash.com:3385 -u " +
              (wallet) + r" -k --nicehash")
if select == "4" or select == "XMrig amd":
    os.system("OptimizeGPU.bat")
    os.system("mode 230,60")
    os.system(r"Miners\XMRig-amd-2.14.6\xmrig-amd.exe --donate-level=1 -a kawpow -o stratum+tcp://kawpow.usa.nicehash.com:3385 -u " +
              (wallet) + r" -k --nicehash")
if select == "5" or select == "Gminer":
    os.system("OptimizeGPU.bat")
    os.system("mode 230,60")
    os.system(
        r"Miners\Gminer\miner.exe -a beamhashIII --proto stratum --server beamv3.usa.nicehash.com:3387 -u " + (wallet))

if select == "6" or select == "NBMiner":
    os.system("OptimizeGPU.bat")
    os.system("mode 230,60")
    os.system(
        r"Miners\NBMiner\nbminer.exe -a ethash -o nicehash+tcp://daggerhashimoto.usa.nicehash.com:3353 -u " + (wallet) + r" -d 0 --no-watchdog")

if select == "7" or select == "ETHMiner":
    os.system("OptimizeGPU.bat")
    os.system("mode 230,60")
    os.system(
        r"Miners\ETHMiner\ethminer.exe -P stratum2+tcp://" + (wallet) + r"@daggerhashimoto.usa.nicehash.com:3353 -U")

if select == "8" or select == "Trex ethash":
    os.system("OptimizeGPU.bat")
    os.system("mode 230,60")
    os.system(
        r"Miners\Trex\t-rex.exe --algo ethash --url stratum2+tcp://daggerhashimoto.usa.nicehash.com:3353 --user " + (wallet))

if select == "9" or select == "Trex kawpow":
    os.system("OptimizeGPU.bat")
    os.system("mode 230,60")
    os.system(
        r"Miners\Trex\t-rex.exe --algo kawpow --url stratum+tcp://kawpow.usa.nicehash.com:3385 --user " + (wallet))

if select == "9" or select == "Return":
    print("Quitting...")
    time.sleep(1)
    os.system("python Start.py")
