def read_files(x):
    f1 = open(x, 'r')
    var0 = []
    for data in f1:
        var0.append(data)
    return var0


def check_files(x, y):
    import dirs.dir_reader
    import os
    f1 = read_files(x)
    f2 = dirs.dir_reader.dir_reader(y)
    var5 = []
    home = os.path.expanduser('~')
    for a, e in zip(f1, f2):
        f4 = os.path.join(home, e, a)
        var5.append(os.path.isdir(f4))
    return var5
