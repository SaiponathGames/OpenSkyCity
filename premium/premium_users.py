def premium_users_writer():
    import os
    import reusable_code as rc
    from dirs.dir_reader import dir_reader
    original_path = os.getcwd()
    os.chdir("..")
    x, u = dir_reader('paths.txt')
    os.chdir(u[0])
    rc.user_writer('premium_users.txt', 'premium', 10000000000, 99999999999, 25)
    os.chdir(original_path)


def premium_users_checker():
    import os
    import reusable_code as rc
    from dirs.dir_reader import dir_reader
    original_path = os.getcwd()
    os.chdir("..")
    x, u = dir_reader('paths.txt')
    os.chdir(u[0])
    x1 = rc.users_checker('premium', 'premium_users.txt')
    os.chdir(original_path)
    return x1
