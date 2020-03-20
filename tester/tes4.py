# u8 = re.search(r"\s", x)
#                 if u8:
#                     uo, ui1 = x.split(' ')
#                     iw, a98 = str(uo).capitalize(), str(ui1).capitalize()
#                     p98 = ''.join(iw + '_' + a98)
#                 else:
#                     uo = x.capitalize()
#                     p98 = uo
import os
import random as ran
import reusable_code as rc
import file.file as f
import string as stri
x1 = 'premium_tester.txt'
x2 = 'premium_testers.txt'
s = 1
if os.path.isfile(x1) and os.path.isfile(x2):
    x = 'premium_tester' + 's'*ran.randint(1, 10) + str(ran.randint(1, 1000)) + '.txt'
else:
    if os.path.isfile(x1):
        x = 'premium_testers.txt'
    else:
        x = 'premium_tester.txt'
h = 'premium'
k = 1000000000000
j = 9999999999999
p = 25
input_file = x
p2 = int(input("How many " + h + " users do you want to create? "))
if p2 == 0:
    print('No number is given. So, exiting the function.\n')
member = ""
for i in range(p2):
    rc.do_nothing(member)
    print("m{} Creating now".format(i))
    member = 'm{}'.format(i)  # str(input("Type the person's name. "))
    rc.do_nothing(member)
    if member == 'exit()' or member == 'exit' or member == 'e':
        print("Okay exiting!")
        break
    else:
        rc.do_nothing(member)
        member = member.replace(' ', '_')
    id1 = ran.randint(k, j)
    yt = ''.join(
        l + '-' * (n % 5 == 4) for n, l in enumerate(ran.choice(stri.ascii_uppercase + stri.digits) for x in range(p))).rstrip('-')
    stri1 = stri.punctuation.replace('`', '').replace('\\', '')
    p6 = ''.join(ran.choice(stri.ascii_lowercase + stri.digits + stri1) for n in range(ran.randint(10, 36)))
    f.file_append(input_file, str(id1) + ' ' + member + ' ' + p6 + ' ' + yt + '\n')
print()
print("Created the users in {}".format(x))
if not p2 == 0:  # or p1 != []:
    print("Done")
