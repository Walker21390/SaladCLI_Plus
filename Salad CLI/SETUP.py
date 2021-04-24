import sys
import os

sys.stdout.write("\x1b]2;Salad CLI+ SETUP\x07")
os.system("python -m pip install --upgrade pip")
os.system("python -m pip install pyperclip")
os.system("python -m pip install python-dateutil")
os.system("python -m pip install requests")
