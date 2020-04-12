
__author__ = ['abmyii', 'Sairam', 'NameKhan72', 'mark4q']

import time
import json
import random  # best not to use "import random as ran" as this makes the code difficult to read
import string  # same as above - you had "import string as stri" before

# All imports should be at the top of the file


# Define global constants at the top of the file
start_num, end_num = 10000000000, 99999999999


class Colors:
	bold = '\033[1m'
	italic = '\033[3m'
	underline = '\033[4m'
	bold_italic = '\033[1m' + '\033[3m'
	yellow = '\033[93m'
	blue = '\033[94m'
	normal = '\033[0m'


def read_users(input_file):
	# userid_list, username_list, password_list, key_list, key_list_1 = [], [], [], [], []
	try:
		with open(input_file, "r") as users_file:
			users = json.load(users_file)
	except FileNotFoundError or json.JSONDecodeError:
		users = []
	return users


def create_users(input_file):
	users = read_users(input_file)
	usernames = [user['username'] for user in users]
	# users_keys = [user['keys'] for user in users]
	users_count = 0
	try:
		users_count = int(input("How many users do you want to add to database? "))
	except ValueError:
		print("Please enter a numeric number!")
	print()
	# users_count = 3

	for i in range(users_count):
		member1 = str(input("What is the name of the person? "))
		print()
		# member1 = "m{}member".format(i)
		if member1 == 'exit()' or member1 == 'exit' or member1 == 'e':
			print("Okay exiting!")
			break
		else:
			# Convert to correct format
			member1 = '_'.join(_.capitalize() for _ in member1.split('_' if ('_' in member1) else ' '))
		# password = ""
		# id1 = 0
		# Add member if not already present
		if member1 not in usernames:
			developer_or_basic = str(input("What type of user you want make {}?".format(str(member1).lower())))
			id1 = random.randint(start_num, end_num)
			password = ''.join(
				random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(10, 40)))
			type1 = "developer" if developer_or_basic in ['d', 'developer'] else "basic"
			users.append({
				"userID": id1,
				"username": member1,
				"password": password,
				"usertype": type1,
				"keys": []
			})

	for user_index, user in enumerate(users):
		member1 = user['username']
		try:
			key_count = int(input("How many keys do you want to input to {}? ".format(str(member1).lower())))
		except ValueError:
			print("Please enter a numeric number!")
			break
		print()

		# key_count = random.randint(0, 3)

		for _ in range(key_count):
			premium_or_special_sandbox = str(input("Which type of key you want to input to {}? ".format(str(
				member1).lower())))
			print()
			# premium_or_special_sandbox = random.choice(["p", "s"])
			number_of_letters = 25 if premium_or_special_sandbox in ['p', 'premium'] else 35 if premium_or_special_sandbox in ['s', 'ss', 'special_sandbox'] else 30
			key_token = "premium" if number_of_letters == 25 else "special_sandbox" if number_of_letters == 35 else "not able to verify"
			key_value = (number_of_letters == 25) if (number_of_letters == 25) else (number_of_letters == 35) if (number_of_letters == 35) else True

			# Create the key and add it
			key = ''.join(l + '-' * (n % 5 == 4) for n, l in enumerate(random.choice(string.ascii_uppercase + string.digits) for _ in range(number_of_letters))).rstrip('-')
			users[user_index]["keys"].append({
				key_token: key_value,
				"key": key
			})

	return users


def print_line_one_by_one(lines: str, sep, secs):
	for line in lines.split("\n"):
		print(line)
		time.sleep(secs)


def authorize_users(x):

	users = read_users(x)

	print1 = "Hello! settings things up, to get you logged in.\nPlease read the note carefully before entering password.\n"
	print_line_one_by_one(print1, "\n", 2)

	username = str(input("Enter your username: "))
	print()
	print2 = "Before entering your password, please read the note.\n\nNote: You must not enter other's password, if you caught, you will get punished.\n\n"
	print_line_one_by_one(print2, "\n", 2)
	password = str(input("Enter your password: "))
	for user in users:
		# print('_'.join(_.capitalize() for _ in username.split(' ')))
		password = password.replace(' ', '')
		if username == user['username'] and password == user['password']:
			print3 = f"\n\nHello {username},\nYou have successfully logged in.\n\nYou can now move on to the next step."
			print_line_one_by_one(print3, "\n", 2)
			if user['usertype'] == 'developer':
				return True, username, password, user['usertype']
			return True, username, password, user['usertype']
		elif username == user['username'] or password == user['password']:
			if not password == user['password']:
				print("\nCredentials Invalid: Your password is wrong!\nPlease try again!!")
				return False, username, password, user['usertype']
			else:
				print("\nCredentials Invalid: Your username is wrong!\nPlease try again!!")
				return False, username, password, user['usertype']


def get_key(dict1, val):
	for key2, value in dict1.items():
		if val == value:
			return key2

	return "key doesn't exist"


def get_users(input_file):
	# input_file = 'file4.json'
	good_words = ['Good', 'Excellent', 'Very good']
	color = Colors
	users = read_users(input_file)
	# print(userids)
	# print(userids.index(31562001021))
	user_authorized, username, password, usertype = authorize_users(input_file)
	if user_authorized:
		choice = 0
		print1 = "\nChoose between the below options.\n1.Key\n2.UserID\n3.Exit"
		print_line_one_by_one(print1, '\n', 2)
		try:
			choice = int(input(
				f"Which one would you like to enter, {username}? "
			))
		except ValueError:
			print("Sorry, please enter numeric number!")
		x = ""
		isalnum1 = ""
		choice1 = int(choice)
		if choice1 == 1:
			print2 = f"\n{random.choice(good_words)} choice! {username}.\n"
			print_line_one_by_one(print2, '\n', 2)
			x = str(input(
				f"Enter the key to check which type of version your key belong to and to check whether the key is valid, {username}: "
			))
		elif choice1 == 2:
			print(f"\n{random.choice(good_words)} choice! {username}.\n")
			x = str(input(f"Enter the userID to get your username, {username}: "))
		elif choice1 == 3:
			print("Exiting now!")
			print("")
		elif not 0 > choice1 > 4:
			print("Please enter the correct number!")
			exit(0)
		if choice == 1:
			key = x
			for user_index, user in enumerate(users):
				for key_index, key1 in enumerate(user['keys']):
					version = get_key(key1, True).replace("_", " ")
					if key == key1['key'] and username == user['username']:
						owner = user['username']
						print3 = f"The key {color.bold}{key}{color.normal} is a valid {version} version key.\nThe username of key {color.bold}{key}{color.normal} is {color.bold_italic}{str(owner).replace('_', ' ')}{color.normal}."
						print_line_one_by_one(print3, '\n', 2)
						break
					else:
						owner = user['username']
						print4 = f"The Owner of {key} is {str(owner).replace('_', ' ')}.\nDon't use other's keys to get {version} version.\nBuy it on your own."
						print_line_one_by_one(print4, '\n', 2)
						break
				else:
					continue
				break
			else:
				print(f"Can't able to find key {key} in the database, please check the key again!")

		elif choice == 2:
			userid = x
			for user_index, user in enumerate(users):
				if int(userid) == int(user['userID']) and password == user['password']:
					owner = user['username']
					print5 = f"The username of userid {color.bold}{userid}{color.normal} is {color.bold_italic}{str(owner).replace('_', ' ')}{color.normal}."
					print_line_one_by_one(print5, '\n', 2)
					break
				else:
					owner = user['username']
					print6 = f"The owner of userid {userid} is {str(owner).replace('_', ' ')}."
					print_line_one_by_one(print6, '\n', 2)
					break
			else:
				print(f"Can't able to find userid {userid} in the database, please check the userid again!")

		else:
			pass

	else:
		print("\nCredentials Invalid: Your credentials are invalid.\n\nPlease check credentials before entering.")


if __name__ == '__main__':
	get_users("../file4.json")
