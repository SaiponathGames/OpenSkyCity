def file_read(input_file):
	with open(input_file, "r") as __in__:
		return [data for data in __in__]


def file_write(input_file, content):
	with open(input_file, "w") as __in__:
		__in__.write(content)


def file_append(input_file, content):
	with open(input_file, "a") as __in__:
		__in__.write(content)


def binary_file_read(input_file):
	with open(input_file, "rb") as __in__:
		return [bytes_1 for bytes_1 in __in__]


def binary_file_write(input_file, bytes_1):
	with open(input_file, "wb") as __in__:
		__in__.write(bytes_1)


def binary_file_append(input_file, bytes_1):
	with open(input_file, "ab") as __in__:
		__in__.write(bytes_1)
