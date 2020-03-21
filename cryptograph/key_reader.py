def read_keys():
	f1 = open("keys.key", 'rb')
	f2 = []
	for data in f1:
		f2.append(data)
	return f2
