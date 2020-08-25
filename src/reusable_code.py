def user_writer(x, h, k, j, p):
	import random as ran
	import re
	import file as f
	import string as stri
	input_file = x
	p2 = int(input("How many " + h + " users do you want to add to database? "))
	if p2 == 0:
		print('No number is given. So, exiting the function.\n')
	p1 = []
	p3 = []
	p5 = []
	p7 = []
	for i in range(p2):
		member = str(input("Type the person's name. "))
		if member == 'exit()' or member == 'exit' or member == 'e':
			print("Okay exiting!")
			break
		else:
			u8 = re.search(r"\s", member)
			if u8:
				uo, ui1 = member.split(' ')
				iw, a98 = str(uo).capitalize(), str(ui1).capitalize()
				p98 = ''.join(iw + '_' + a98)
				member = p98
			else:
				uo = member.capitalize()
				member = uo
			p1.append(member)
		id1 = ran.randint(k, j)
		p3.append(str(id1))
		yt = ''.join(l + '-' * (n % 5 == 4) for n, l in enumerate(ran.choice(stri.ascii_uppercase + stri.digits) for _ in range(p))).rstrip('-')
		p5.append(yt)
		p6 = ''.join(
			ran.choice(stri.ascii_lowercase + stri.digits + stri.punctuation) for _ in range(ran.randint(10, 36)))
		p7.append(p6)
	for i, e, o, y in zip(p1, p3, p5, p7):
		ui = (e + ' ' + i + ' ' + y + ' ' + o + '\n')
		f.file_append(input_file, ui)
	print()
	if not p2 == 0 or p1 != []:
		print("Done\n")


class Colors:
	bold = '\033[1m'
	italic = '\033[3m'
	underline = '\033[4m'
	bold_italic = '\033[1m' + '\033[3m'
	yellow = '\033[93m'
	blue = '\033[94m'
	normal = '\033[0m'


def do_nothing(*x):
	for a in x:
		list(x).append(a)
		pass


def users_reader(x):
	import file as f
	input_file = x
	user1r = f.file_read(input_file)
	p2 = []
	p4 = []
	p5 = []
	p6 = []
	p7 = []
	for data in user1r:
		p2.append(data)
	for i in range(len(p2)):
		p10, p11, p12, p13 = p2[int(i)].rstrip('\n').split(' ')
		p11 = str(p11).replace('_', ' ')
		p4.append(p10), p5.append(p11), p6.append(p12), p7.append(p13)
	return p4, p5, p6, p7


def users_authorizer(x):
	import time as t
	import re
	t.sleep(3)
	print(
		"Hello! settings things up, to get you logged in.\nPlease read the note carefully before entering password.\n")
	t.sleep(2)
	username = str(input("Enter your username: "))
	print()
	password = str(
		input("Before entering your password, please read the note.\n\nNote: You must not enter other's password, if you caught, you will get punished.\n\nEnter your password: "))
	p1, p2, p3, p4 = users_reader(x)
	k = 0
	for _in_, _in1_ in zip(p2, p3):
		do_nothing(_in1_, _in1_)
		u8 = re.search(r"\s", username)
		if u8:
			uo, ui1 = username.split(' ')
			iw, a98 = str(uo).capitalize(), str(ui1).capitalize()
			p98 = ''.join(iw + '_' + a98)
			username = p98
		else:
			uo = username.capitalize()
			username = uo
			pwd = password.replace(' ', '')
			password = pwd
			if username in p2 and password in p3:
				if username == p2[k] and password == p3[k]:
					print(
						"Hello " + username + ",\nYou have successfully logged in.\n\nYou can now move on to the next step.")
					return True, username, password
				elif username == p2[k] or password == p3[k]:
					if not password == p3[k]:
						print(
							"\nCredentials Invalid: Your credentials are invalid.\nPlease check credentials before entering.")
						return False, username, password
			else:
				return False, username, password
			k += 1
			del p1, p4


def users_checker(n, y):
	import re
	import random as ran
	p = Colors
	p1, p2, p3, p4 = users_reader(y)
	t1, us1, pw1 = users_authorizer(y)
	p5 = ['Good', 'Excellent', 'Very good']
	if t1:
		y = str(input("\nChoose between the below options." + '\n' + '1.Key' + '\n' + '2.UserID' + '\n' + '3.Exit' + "\n" + "Which one would you like to enter, {}? ".format(us1)))
		x = ""
		x4 = []
		p09 = ""
		if not y.isnumeric():
			return "Sorry, please enter numeric number!"
		else:
			y1 = int(y)
			if y1 == 1:
				print("\n{} choice! {}.\n".format(ran.choice(p5), us1))
				x = input("Enter the key to check whether you have " + n + " version or not, {}: ".format(us1))
			elif y1 == 2:
				print("\n{} choice! {}.\n".format(ran.choice(p5), us1))
				x = input("Enter the username to check whether you have " + n + " or not: ")
			elif y1 == 3:
				print("Exiting now!")
				return
			elif not 0 > y1 > 4:
				return "Please enter the correct number!"
		p78 = re.search(r"-", x)
		if p78:
			p09 = x.replace('-', '')
		if p09.isalnum():
			k = 0
			for u88 in p4:
				do_nothing(u88)
				if x in p4:
					if x == p4[k]:
						if us1 in p2:
							if p2.index(us1) == p4.index(x):
								z = p2[int(k)]
								return "The key " + p.bold + x + p.normal + " is a valid " + n + " version key. The username of key " + p.bold + x + p.normal + " is " + p.italic + str(z).replace('_', ' ') + p.normal + "."
							else:
								k1 = p4.index(x)
								r5 = p2[int(k1)]
								return "The Owner of " + x + " is " + r5 + ".\nDon't use other's keys to get " + n + " version.\nBuy it on your own."
				else:
					return "Can't able to find " + x + " in the database, please check the key again!"
				k += 1
		else:
			k = 0
			for u87 in p1:
				p98 = x
				ui = p98 in p1[int(k)]
				do_nothing(u87)
				if ui:
					p99 = p1[int(k)]
					io = p.bold + p.blue + str(p99).replace('_', ' ') + p.normal
					if p99 in p1:
						if ui:
							if us1 in p2:
								if p2.index(us1) == p1.index(x):
									z = p4[int(k)]
									li = p.bold_italic + p.yellow + z + p.normal
									x4.append(
										"The username " + io + " has a valid" + n + " version key. The key of username " + io + " is " + li + ".")
									if len(x4) > 1:
										return "There is same alias for " + p.bold + str(
											len(x4)) + p.normal + " names! Please be more specific!"
									else:
										return x4[0]
					else:
						return "Can't able to find the userID " + io + " in the database, please check the name again!"
					k += 1
			else:
				return "Please enter a valid " + p.bold_italic + "userID" + p.normal + " of your name!"
	else:
		return "\nCredentials Invalid: Your credentials are invalid.\n\nPlease check credentials before entering."
