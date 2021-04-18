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
    "Select miner! \n\n1. Phoenixminer 5.5c (GPU) \n2. XMRig 6.7.0 (CPU) \n3. XMRig-nVidia (GPU) \n4. XMRig-Amd (GPU \n5. Gminer \n6. Return to main menu\n\nSelect: ")
if select == "1" or select == "Phoenixminer":
    os.system("OptimiseGPU.bat")
#	print("%appdata%\salad\plugin-bin\PhoenixMiner-5.5c\PhoenixMiner.exe -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto.usa.nicehash.com:3353 -pool2 stratum+tcp://daggerhashimoto.eu.nicehash.com:3353 -ewal "+ (phoenixwallet) + " -esm 3 -allpools 1 -allcoins 0")
#	time.sleep(1100000)
    os.system("mode 230,60")
    os.system(r"PhoenixMiner-5.5c\PhoenixMiner.exe -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto.usa.nicehash.com:3353 -pool2 stratum+tcp://daggerhashimoto.eu.nicehash.com:3353 -ewal " + (wallet) + " -esm 3 -allpools 1 -allcoins 0")
if select == "2" or select == "XMrig CPU":
    os.system("cls")
#	print(r"%appdata%\salad\plugin-bin\XMRig-CPU-6.7.0\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380 --coin=monero -u "+ (xmrwallet) + " -k --nicehash -o stratum+tcp://randomxmonero")
#	time.sleep(1100000)
    os.system("mode 230,60")
    os.system(r"XMRig-CPU-6.7.0\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380 --coin=monero -u " +
              (wallet) + " -k --nicehash -o stratum+tcp://randomxmonero")
if select == "3" or select == "XMrig nVidia":
    os.system("OptimiseGPU.bat")
#	print(r"%appdata%\salad\plugin-bin\XMRig-CPU-6.7.0\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380 --coin=monero -u "+ (xmrwallet) + " -k --nicehash -o stratum+tcp://randomxmonero")
#	time.sleep(1100000)
    os.system("mode 230,60")
    os.system(r"XMRig-6.7.0\xmrig.exe --no-cpu --cuda --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380 --coin=monero -u " +
              (wallet) + " -k --nicehash -o stratum+tcp://randomxmonero")
if select == "4" or select == "XMrig nVidia":
    os.system("OptimiseGPU.bat")
#	print(r"%appdata%\salad\plugin-bin\XMRig-CPU-6.7.0\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380 --coin=monero -u "+ (xmrwallet) + " -k --nicehash -o stratum+tcp://randomxmonero")
#	time.sleep(1100000)
    os.system("mode 230,60")
    os.system(r"XMRig-amd-2.14.6\xmrig-amd.exe --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380 --coin=monero -u " +
              (wallet) + " -k --nicehash -o stratum+tcp://randomxmonero")
if select == "5" or select == "Gminer":
    os.system("OptimiseGPU.bat")
    os.system("mode 230,60")
    os.system(
        r"Gminer\miner.exe -a beamhashIII --proto stratum --server beamv3.eu.nicehash.com:3387 -u " + (wallet))
if select == "6" or select == "Return":
    print("Quitting...")
    time.sleep(1)
    os.system("py Start.py")

# miner.exe -a beamhashIII --proto stratum --server beamv3.eu.nicehash.com:3387 -u 3N1wxx2YQrvobXJtpz7Js5h5zNqx2qo7H6.b74ejt91iguspx
