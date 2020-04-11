import os
import re

original_dir = os.getcwd()
os.chdir("..")
x = 'paths.txt'
f1 = open(x, 'r')
var0 = []
var2 = []
var4 = []
# for data in f1:
# 	var0.append(data)
home = os.path.expanduser('~')
appdata = os.getenv('LOCALAPPDATA')
print(appdata)
print(home)
for dir1 in f1:
	if 'APPDATA' in dir1:
		# var3 = var1.strip()
		# print(var3)
		# print(re.findall('APPDATA', var1))
		# var5 =
		# print(var5)
		# vs =
		var4.append(os.path.join(appdata, dir1.strip("~\\/' \n").strip('\\APPDATA\\')))
	else:
		# var3 =
		# print(var3)
		# vs =
		var2.append(os.path.join(home, dir1.strip("~\\/' \n")))
print(var2)
print(var4)

from cryptograph.key_reader import read_keys

read_keys()
