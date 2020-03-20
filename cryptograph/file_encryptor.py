def encrypt_file(x, y):
    from cryptograph import key_reader as kr
    from cryptography.fernet import Fernet
    keys = kr.read_keys()
    key = keys[0]
    input_file = x
    output_file = y
    with open(input_file, 'rb') as f:
        data = f.read()
    f2 = Fernet(key)
    encrypted = f2.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)
