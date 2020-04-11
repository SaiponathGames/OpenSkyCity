import os


def dirs_creator(dirs):
	for dir_path in dirs:
		dir_check = os.path.isdir(dir_path)
		if dir_check is False:
			os.makedirs(dir_path)


def dirs_reader(file):
	dirs = open(file, 'r')
	home_dirs, appdata_dirs = [], []
	home = os.path.expanduser('~')
	appdata = os.getenv('LOCALAPPDATA')
	for dir1 in dirs:
		if 'APPDATA' in dir1:
			appdata_dirs.append(os.path.join(appdata, dir1.strip("~\\/' \n").strip('\\APPDATA\\')))
		else:
			home_dirs.append(os.path.join(home, dir1.strip("~\\/' \n")))
	return home_dirs, appdata_dirs

