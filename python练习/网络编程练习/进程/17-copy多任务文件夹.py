import os
from multiprocessing import Pool
# 复制文件夹
def copy(file_name,old_folder_name,new_floder_name):
    # 打开原文件夹中的文件并读入
    old_f = open(old_folder_name + "/" + file_name,"rb")
    content = old_f.read()
    old_f.close()
    # 打开新文件夹中的文件并写入
    new_f = open(new_floder_name + "/" + file_name,"wb")
    new_f.write(content)
    new_f.close()
def main():
    # 获取要复制的文件夹
    old_folder_name = input("请输入要复制的文件夹:")
    # 创建新的文件夹
    new_folder_name = old_folder_name + "附件"
    os.mkdir(new_folder_name)
    # 获取原来文件夹中文件的名字
    file_names = os.listdir(old_folder_name)
    print(file_names)
    # 创建进程池
    pool = Pool(5)
    # 向进程池中添加任务
    for file_name in file_names:
        pool.apply_async(copy,args=(file_name,old_folder_name,new_folder_name))
    # 关闭进程池
    pool.close()
    # 等待主进程结束,解堵塞
    pool.join()
if __name__ == '__main__':
    main()