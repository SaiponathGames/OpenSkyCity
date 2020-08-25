def decrypt_file(input_file, output_file):
	from cryptograph import key_reader as kr
	from cryptography.fernet import Fernet
	keys = kr.read_keys()
	key = keys[0]
	with open(input_file, 'rb') as f:
		data = f.read()
	f1 = Fernet(key)
	decrypted = f1.decrypt(data)
	with open(output_file, 'wb') as f:
		f.write(decrypted)
