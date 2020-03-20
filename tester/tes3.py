import reusable_code as rc
x = 'premium_userrss.txt'
username = str(input("Enter your username: "))
password = str(input("Before entering your password, please read the note.\n\nNote: You must not enter other's password,"
                     " if you caught, you will get punished.\nEnter your password: "))
p1, p2, p3, p4 = rc.users_reader(x)
k = 0
for _in_, _in1_ in zip(p2, p3):
    rc.do_nothing(_in1_, _in1_)
    if username in p2 and password in p3:
        if username == p2[k] and password == p3[k]:
            print("You can move on to the next step.")
            print(True, username, password)
        elif username == p2[k] or password == p3[k]:
            if not password == p3[k]:
                print("Credentials Invalid: Your credentials are invalid.\nPlease check credentials before entering.")
                print(False)

    else:
        print("Sorry, something went wrong!")
    k += 1
