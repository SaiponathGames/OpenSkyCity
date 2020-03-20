import random as ran
import file.file as f
import string as stri
x = 'premium_userrss.txt'
h = 'premium'
k = 1000000000000
j = 9999999999999
p = 25
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
        member = member.replace(' ', '_')
        p1.append(member)
    id1 = ran.randint(k, j)
    p3.append(str(id1))
    yt = ''.join(
        l + '-' * (n % 5 == 4) for n, l in enumerate(ran.choice(stri.ascii_uppercase + stri.digits) for x in range(p))).rstrip('-')
    p5.append(yt)
    p6 = ''.join(ran.choice(stri.ascii_lowercase + stri.digits + stri.punctuation) for n in range(ran.randint(10, 36)))
    p7.append(p6)
for i, e, o, y in zip(p1, p3, p5, p7):
    ui = (e + ' ' + i + ' ' + y + ' ' + o + '\n')
    f.file_append(input_file, ui)
print()
if not p2 == 0 or p1 != []:
    print("Done")
