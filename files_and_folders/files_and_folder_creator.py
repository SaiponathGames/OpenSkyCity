def folder_and_file_creator():
    import os
    import random as r
    from dirs import dir_reader, dir_checker
    from files import file_reader, file_checker
    from initialization.intialize import OpenCity

    original_path = os.path.realpath(os.path.dirname(__file__))
    os.chdir(original_path)
    type(OpenCity)
    os.chdir("..")
    mapnames = []
    f1 = open("some_city_names.txt", "r")
    for cityname in f1:
        cityname1 = cityname.replace("\n", "")
        mapnames.append(cityname1)

    x, u = dir_reader.dir_reader('paths.txt')
    dir_checker.dir_checker(x)
    dir_checker.dir_checker(u)
    y = file_reader.file_reader('files.txt')
    os.chdir(original_path)
    os.chdir(x[0])
    file_checker.file_checker(y[0])
    os.chdir(x[1])
    file_checker.file_checker(y[2])
    os.chdir(u[0])
    file_checker.file_checker(y[1])
    os.chdir(u[1])
    file_checker.file_checker(y[3])
    os.chdir(x[8])
    for i in range(10):
        file_checker.file_checker(y[5].format(i))
    os.chdir(x[6])
    for i in range(5):
        x12 = os.listdir(x[6])
        if len(x12) < 5:
            mapname = r.choice(mapnames)
            file_checker.file_checker(y[4].format(mapname))
        else:
            break

