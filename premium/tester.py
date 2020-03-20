import reusable_code as rc
import re

n = 'premium'
p = rc.Colors
p1, p2, p3, p4 = rc.users_reader('premium_userrss.txt')
y = str(input("Choose between the below options." + '\n' + '1.Username' + '\n' + '2.Key' + '\n' +
              "Which one would you like to enter? "))
y1 = 0
x = ""
x4 = []
password = str(input("Enter your password, the password is case sensitive: "))
k1 = 0
for _ in p3:
    if password == p3[x]:

        if not y.isnumeric():
            print("Sorry, please enter numeric number!")
        else:
            y1 = int(y)
        if y1 == 1:
            x = input("Enter the username to check whether you have " + n + " or not: ")
        elif y1 == 2:
            x = input("Enter the id to check whether you have " + n + " or not: ")
        elif not 0 > y1 > 3:
            print("Please enter the correct number!")
        p78 = re.search(r"-", x)
        if p78:
            x = x.replace('-', '')
        if x.isalnum():
            k = 0
            for _ in p4:
                if x in p2:
                    if x == p2[k]:
                        z = p4[int(k)]
                        print("The key " + p.bold + x + p.normal + " is " + n + " version. The username of " + \
                              p.bold + x + p.normal + " is " + p.italic + str(z).replace('_', ' ') \
                              + p.normal + ".")
                else:
                    print("Can't able to find " + x + \
                          " in the database, please check the key again!")
                k += 1
        else:
            k = 0
            for _ in p4:
                p98 = ''
                u8 = re.search(r"\s", x)
                if u8:
                    uo, ui1 = x.split(' ')
                    iw, a98 = str(uo).capitalize(), str(ui1).capitalize()
                    p98 = ''.join(iw + '_' + a98)
                else:
                    uo = x.capitalize()
                    p98 = uo
                    ui = p98 in p2[int(k)]
                    if ui:
                        p99 = p2[int(k)]
                        io = p.bold + p.blue + str(p99).replace('_', ' ') + p.normal
                        if p99 in p4:
                            if ui:
                                z = p4[int(k)]
                                li = p.bold_italic + p.yellow + z + p.normal
                                x4.append(
                                    "The username " + io + " has a " + n + " version. The key of " + io + " is " + li + ".")
                                if len(x4) > 1:
                                    print("There is same alias for " + p.bold + str(
                                        len(x4)) + p.normal + " names! Please be more specific!")
                                else:
                                    print(x4[0])
                        else:
                            print("Can't able to find the " + io + \
                                  " in the database, please check the name again!")
                    k += 1
            else:
                print("Please enter a valid " + p.bold_italic + "alias" + p.normal + " of your name!")
    k1 += 1
