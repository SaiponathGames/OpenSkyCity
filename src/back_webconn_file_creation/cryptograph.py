import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from . import settings
from .file import binary_file_append, binary_file_read, binary_file_write

settings_ = settings.Settings()


def decrypt_file(input_file, output_file):
    key = binary_file_read(settings_.KEYS_FILE)[0]
    data = binary_file_read(input_file)
    binary_file_write(output_file, Fernet(key).decrypt(data))


def encrypt_file(input_file, output_file):
    key = binary_file_read(settings_.KEYS_FILE)[0]
    data = binary_file_read(input_file)
    binary_file_write(output_file, Fernet(key).encrypt(data))


def create_key(string: str):
    password_provided = str(string).encode()
    salt = b'\xfb|\xe8\xe0\xe5\x9d\x11\xf5\xbc 8o\xbe<\xd9\x92'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_provided))
    binary_file_append(settings_.KEYS_FILE, bytes(key + os.linesep.encode()))
