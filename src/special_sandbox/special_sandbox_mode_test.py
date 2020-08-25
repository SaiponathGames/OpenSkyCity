import file
from cryptograph.file_decryptor import decrypt_file
from cryptograph.file_encryptor import encrypt_file


def special_sandbox_mode_test():
    # original_path = os.path.realpath(os.path.dirname(__file__))
    # os.chdir("..")
    # x, u = dirs.dirs_reader('paths.txt')
    # y = files.files_reader('files.txt')
    # os.chdir(original_path)
    # f1 = open(y[2], 'r')
    # os.chdir(x[1])
    # f2 = open(y[2], 'w')
    # os.chdir(original_path)
    # var0 = file.file_read(y[2])
    # os.chdir(x[1])
    # f2.write(var0[0])
    # f2.close()
    # os.chdir(original_path)
    # file_input = os.path.join(x[1], y[2])
    # file_output = os.path.join(u[1], y[3])
    # os.chdir("..")
    # decrypt_file(file_input, file_output)
    # os.chdir(original_path)
    # # su.special_sandbox_mode_users_writer()
    # # x2 = su.special_sandbox_mode_users_checker()
    # # if x2 is not None:
    # #     print(x2)
    # # else:
    # #     t.sleep(2)
    # #     print("\n\nExited successfully!")
    # file_input = os.path.join(u[1], y[3])
    # file_output = os.path.join(original_path, y[2])
    # os.chdir('..')
    # encrypt_file(file_input, file_output)
    # os.chdir(original_path)
    import settings
    file.file_copy(settings.SPECIAL_SANDBOX_ROOT_USRA_FILE, settings.SPECIAL_SANDBOX_USERS_USRA_FILE)
    decrypt_file(settings.SPECIAL_SANDBOX_USERS_USRA_FILE, settings.SPECIAL_SANDBOX_APPDATA_TXT_FILE)
    encrypt_file(settings.SPECIAL_SANDBOX_APPDATA_TXT_FILE, settings.SPECIAL_SANDBOX_USERS_USRA_FILE)
    file.file_copy(settings.SPECIAL_SANDBOX_USERS_USRA_FILE, settings.SPECIAL_SANDBOX_ROOT_USRA_FILE)


if __name__ == '__main__':
    special_sandbox_mode_test()
