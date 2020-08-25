import file
from cryptograph.file_decryptor import decrypt_file
from cryptograph.file_encryptor import encrypt_file


def premium_test():
    # original_path = os.path.realpath(os.path.dirname(__file__))
    # os.chdir(original_path)
    # os.chdir("..")
    # x, u = dirs.dirs_reader('paths.txt')
    # y = files.files_reader('files.txt')
    # os.chdir(x[0])
    # f2 = open(y[0], 'w')
    # os.chdir(original_path)
    # var0 = file.file_read(y[0])
    # os.chdir(x[0])
    # f2.write(var0[0])
    # f2.close()
    # os.chdir(original_path)
    # file_input = os.path.join(x[0], y[0])
    # file_output = os.path.join(u[0], y[1])
    # os.chdir("..")
    # decrypt_file(file_input, file_output)
    # os.chdir(original_path)
    # # pu.premium_users_writer()
    # # x2 = pu.premium_users_checker()
    # # if x2 is not None:
    # #     print(x2)
    # # else:
    # #     sleep(2)
    # #     print("\n\nExited successfully!")
    # file_input = os.path.join(u[0], y[1])
    # file_output = os.path.join(original_path, y[0])
    # os.chdir('..')
    # encrypt_file(file_input, file_output)
    # os.chdir(original_path)
    # os.chdir(x[0])
    # f2 = open(y[0], 'w')
    # os.chdir(original_path)
    # var0 = file.file_read(y[0])
    # os.chdir(x[0])
    # f2.write(var0[0])
    # f2.close()
    # os.chdir(original_path)
    import settings
    file.file_copy(settings.PREMIUM_ROOT_USRA_FILE, settings.PREMIUM_USERS_USRA_FILE)
    decrypt_file(settings.PREMIUM_USERS_USRA_FILE, settings.PREMIUM_APPDATA_TXT_FILE)
    encrypt_file(settings.PREMIUM_APPDATA_TXT_FILE, settings.PREMIUM_USERS_USRA_FILE)
    file.file_copy(settings.PREMIUM_USERS_USRA_FILE, settings.PREMIUM_ROOT_USRA_FILE)


if __name__ == '__main__':
    premium_test()
