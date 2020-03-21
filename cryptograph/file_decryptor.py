def decrypt_file(x, y):
	from cryptograph import key_reader as kr
	from cryptography.fernet import Fernet
	keys = kr.read_keys()
	key = keys[0]
	input_file = x
	output_file = y
	with open(input_file, 'rb') as f:
		data = f.read()
	f1 = Fernet(key)
	encrypted = f1.decrypt(data)
	with open(output_file, 'wb') as f:
		f.write(encrypted)
