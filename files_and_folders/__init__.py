import os
import files
import random
import dirs


def switch_dirs(app_dir_indices, file_dir_indices, appdata_dirs, home_dirs, file_list):
	for (app_dir_index_1, app_dir_index), file_dir_index in zip(enumerate(app_dir_indices), file_dir_indices):
		if app_dir_index_1 >= 2:
			os.chdir(appdata_dirs[app_dir_index])
		else:
			os.chdir(home_dirs[app_dir_index])
		files.files_checker(file_list[file_dir_index])


def folder_and_file_creator():
	try:
		original_path = os.path.realpath(os.path.dirname(__file__))
		os.chdir(original_path)
		os.chdir("..")
		mapnames = []
		with open("some_city_names.txt", "r", encoding="utf-8") as f1:
			for cityname in f1:
				cityname1 = cityname.replace("\n", "")
				mapnames.append(cityname1)
		home_dirs, appdata_dirs = dirs.dirs_reader('paths.txt')
		dirs.dirs_checker(home_dirs)
		dirs.dirs_checker(appdata_dirs)
		file_list = files.files_reader('files.txt')
		os.chdir(original_path)
		app_dir_indices = [0, 1, 0, 1]
		file_dir_indices = [0, 2, 1, 3]
		switch_dirs(app_dir_indices, file_dir_indices, appdata_dirs, home_dirs, file_list)
		os.chdir(home_dirs[8])
		for i in range(1, 10):
			files.files_checker(file_list[5].format(i))
		os.chdir(home_dirs[6])
		for i in range(5):
			if len(os.listdir(home_dirs[6])) < 5:
				mapname = random.choice(mapnames)
				files.files_checker(file_list[4].format(mapname))
			else:
				break
	except Exception as e:
		return False
	else:
		return True


if __name__ == '__main__':
	folder_and_file_creator()
