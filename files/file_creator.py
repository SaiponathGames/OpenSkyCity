def file_creator(y):
	import os
	file_path = y
	if os.path.isfile(file_path) is False:
		with open(file_path, 'w'):
			pass
