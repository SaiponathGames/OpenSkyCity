def _convert_from_list_to_tuple(list_1: list):
	return tuple(list_1)


def _convert_from_tuple_to_list(tuple_1: tuple):
	return list(tuple_1)


def _convert_from_tuple_to_set(tuple_1: tuple):
	return set(tuple_1)


def _convert_from_set_to_tuple(set_1: set):
	return tuple(set_1)


def _convert_from_list_to_set(list_1: list):
	return set(list_1)


def _convert_from_set_to_list(set_1: set):
	return list(set_1)


def convert__from__to__(content1, to_1):
	if type(content1) == list and type(to_1) == tuple:
		return _convert_from_list_to_tuple(content1)
	elif type(content1) == tuple and type(to_1) == list:
		return _convert_from_tuple_to_list(content1)
	elif type(content1) == tuple and type(to_1) == set:
		return _convert_from_tuple_to_set(content1)
	elif type(content1) == set and type(to_1) == tuple:
		return _convert_from_set_to_tuple(content1)
	elif type(content1) == list and type(to_1) == set:
		return _convert_from_list_to_set(content1)
	elif type(content1) == set and type(to_1) == list:
		return _convert_from_set_to_list(content1)
	elif type(content1) == dict:
		return "Sorry Under construction"
	else:
		return f"Not possible with {type(content1)} and {to_1}"


print(convert__from__to__((98, 99, 100), set({})))

