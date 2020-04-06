import subprocess
import time


status = subprocess.Popen('/Applications/Calculator.app/Contents/MacOS/Calculator')
print(status.poll())
time.sleep(10)
print(status.poll())


# status = subprocess.Popen(['/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/bin/python3.7',
                         #  'webbrowser_example.py'])

