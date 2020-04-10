# import os
#
# from cryptograph.file_decryptor import decrypt_file
# from cryptograph.file_encryptor import encrypt_file
# from dirs.dir_reader import dir_reader
# from file import file
# from files.file_reader import file_reader
# from premium import premium_users as pu
#
# original_path = os.getcwd()
# os.chdir("..")
# x, u = dir_reader('paths.txt')
# y = file_reader('files.txt')
# os.chdir(original_path)
# file_input1 = os.path.join(os.getcwd(), y[3])
# file_output1 = os.path.join(os.getcwd(), y[2])
# os.chdir("..")
# if not os.path.isfile(file_output1):
# 	open(y[2], 'w')
# os.chdir(original_path)
# encrypt_file(file_input1, file_output1)
# f1 = open(y[2], 'r')
# os.chdir(x[1])
# f2 = open(y[0], 'w')
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
# pu.premium_users_writer()
# print(pu.premium_users_checker())
