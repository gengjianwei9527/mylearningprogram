import os

folder_path = "C:/VZW"  # 更改为你要获取文件名的文件夹路径
file_list = os.listdir(folder_path)  # 获取文件夹下所有文件名的列表

with open("VZW.txt", "w") as f:  # 打开一个文件用于写入文件路径
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)  # 拼接文件路径
        f.write(file_path + "\n")  # 将文件路径写入文件，每行一个