def dir_checker(x):
    import os
    import dirs.dir_creator as dccdc
    for a in x:
        dir_path = a
        dir_check = os.path.isdir(dir_path)
        if dir_check is False:
            dccdc.dir_creator(a)
