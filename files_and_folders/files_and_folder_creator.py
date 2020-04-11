def folder_and_file_creator():
	import os
	import random
	import dirs
	import files

	original_path = os.path.realpath(os.path.dirname(__file__))
	os.chdir(original_path)
	os.chdir("..")
	mapnames = []
	f1 = open("some_city_names.txt", "r", 1, "utf-8")
	for cityname in f1:
		cityname1 = cityname.replace("\n", "")
		mapnames.append(cityname1)

	home_dirs, appdata_dirs = dirs.dirs_reader('paths.txt')
	dirs.dirs_checker(home_dirs)
	dirs.dirs_checker(appdata_dirs)
	file_list = files.files_reader('files.txt')
	os.chdir(original_path)
	os.chdir(home_dirs[0])
	files.files_checker(file_list[0])
	os.chdir(home_dirs[1])
	files.files_checker(file_list[2])
	os.chdir(appdata_dirs[0])
	files.files_checker(file_list[1])
	os.chdir(appdata_dirs[1])
	files.files_checker(file_list[3])
	os.chdir(home_dirs[8])
	for i in range(10):
		files.files_checker(file_list[5].format(i))
	os.chdir(home_dirs[6])
	for i in range(5):
		if len(os.listdir(home_dirs[6])) < 5:
			mapname = random.choice(mapnames)
			files.files_checker(file_list[4].format(mapname))
		else:
			break



if __name__ == '__main__':
	folder_and_file_creator()
