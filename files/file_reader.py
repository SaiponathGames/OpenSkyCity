def file_reader(x):
    f1 = open(x, 'r')
    var0 = []
    for data in f1:
        data = data.rstrip('\n')
        var0.append(data)
    return var0
