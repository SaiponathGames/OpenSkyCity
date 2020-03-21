def file_checker(x):
	import os
	import files.file_creator as fcc
	if type(x) is list:
		for a in x:
			file_path = a
			file_check = os.path.isfile(file_path)
			if file_check is False:
				fcc.file_creator(a)
	else:
		file_path = x
		file_check = os.path.isfile(file_path)
		if not file_check:
			fcc.file_creator(x)
