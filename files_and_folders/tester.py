import os
import re
original_dir = os.getcwd()
os.chdir("..")
x = 'paths.txt'
f1 = open(x, 'r')
var0 = []
var2 = []
var4 = []
for data in f1:
    var0.append(data)
home = os.path.expanduser('~')
appdata = os.getenv('LOCALAPPDATA')
for var1 in var0:
    var3 = var1.strip("~\\/' \n")
    if re.search('APPDATA', var1):
        var5 = var3.strip('\\APPDATA\\')
        vs = os.path.join(appdata, var5)
        var4.append(vs)
    else:
        vs = os.path.join(home, var3)
        var2.append(vs)
print(var2)
print(var4)

from cryptograph.key_reader import read_keys

read_keys()
