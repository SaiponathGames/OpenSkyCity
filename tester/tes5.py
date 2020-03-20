from reusable_code import *
# import time as t
import re
x = 'premium_userrss.txt'


# t.sleep(3)
print("Hello! settings things up, to get you logged in.\nPlease read the note carefully before entering password.\n")
# t.sleep(2)
username = str(input("Enter your username: "))
print()
password = str(
    input("Before entering your password, please read the note.\n\nNote: You must not enter other's password,"
          " if you caught, you will get punished.\n\nEnter your password: "))
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
        if username in p2 and password in p3:
            if username == p2[k] and password == p3[k]:
                print(
                    "Hello " + username + ",\nYou have successfully logged in.\n\nYou can now move on to the next step.")
                print(True, username, password)
            elif username == p2[k] or password == p3[k]:
                if not password == p3[k]:
                    print(
                        "\nCredentials Invalid: Your credentials are invalid.\nPlease check credentials before entering.")
                    print(False, username, password)
        else:
            print(False, username, password)
        k += 1
        # del p1, p4
