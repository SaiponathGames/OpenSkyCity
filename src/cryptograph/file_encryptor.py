def encrypt_file(input_file, output_file):
	from cryptograph import key_reader as kr
	from cryptography.fernet import Fernet
	keys = kr.read_keys()
	key = keys[0]
	with open(input_file, 'rb') as f:
		data = f.read()
	f2 = Fernet(key)
	encrypted = f2.encrypt(data)
	with open(output_file, 'wb') as f:
		f.write(encrypted)
