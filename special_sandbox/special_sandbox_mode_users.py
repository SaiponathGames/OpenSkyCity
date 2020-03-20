def special_sandbox_mode_users_writer():
    import os
    import reusable_code as rc
    from dirs.dir_reader import dir_reader
    original_path = os.getcwd()
    os.chdir("..")
    x, u = dir_reader('paths.txt')
    os.chdir(u[1])
    rc.user_writer('special_sandbox_mode_users.txt', 'special sandbox', 100000000000000000000000000000,
                   999999999999999999999999999999, 35)
    os.chdir(original_path)


def special_sandbox_mode_users_checker():
    import os
    import reusable_code as rc
    from dirs.dir_reader import dir_reader
    original_path = os.getcwd()
    os.chdir("..")
    x, u = dir_reader('paths.txt')
    os.chdir(u[1])
    x1 = rc.users_checker('special sandbox', 'special_sandbox_mode_users.txt')
    os.chdir(original_path)
    return x1
