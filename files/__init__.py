import os


def files_checker(*file_paths: str):
	if type(file_paths) is tuple:
		for file_path in file_paths:
			file_check = os.path.isfile(file_path)
			if file_check is False:
				with open(file_path, 'w'):
					pass
	else:
		file_check = os.path.isfile(file_paths[0])
		if not file_check:
			with open(file_paths[0], 'w'):
				pass


def files_reader(input_file):
	files = open(input_file, 'r')
	return [data.rstrip('\n') for data in files]