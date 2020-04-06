import subprocess

"""
read more here:
https://docs.python.org/3.7/library/subprocess.html
"""

pl = subprocess.Popen(['ps', '-U', '0'],
                      stdout=subprocess.PIPE).communicate()[0]
print(pl.decode('utf-8'))

