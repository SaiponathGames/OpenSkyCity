def file_read(x):
    f1 = open(x, 'r')
    list1 = []
    for a in f1:
        list1.append(a)
    f1.close()
    return list1


def file_write(x, y):
    f1 = open(x, 'w')
    f1.write(y)
    f1.close()


def file_append(x, y):
    f1 = open(x, 'a')
    f1.write(y)
    f1.close()


def binary_file_read(x):
    f2 = open(x, 'rb')
    list2 = []
    for a in f2:
        list2.append(a)
    f2.close()
    return list2


def binary_file_write(x,y):
    f2 = open(x, 'wb')
    f2.write(y)
    f2.close()


def binary_file_append(x, y):
    f2 = open(x, 'ab')
    f2.write(y)
    f2.close()
