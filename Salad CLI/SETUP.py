import sys
import os

sys.stdout.write("\x1b]2;Salad CLI+ SETUP\x07")
os.system("python -m pip install --upgrade "pip @ https://github.com/uranusjr/pip/archive/refs/heads/sysconfig-header-with-none-project.zip") # Fixes the `value for scheme.headers does not match` error
os.system("python -m pip install pyperclip")
os.system("python -m pip install python-dateutil")
os.system("python -m pip install requests")
os.system("pause")
