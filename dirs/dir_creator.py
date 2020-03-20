def dir_creator(y):
    import os
    dir_path = y
    if os.path.isdir(dir_path) is False:
        os.makedirs(dir_path)



