import os
import multiprocessing
# 复制文件夹
def copy(q,file_name,old_folder_name,new_floder_name):
    # 打开原文件夹中的文件并读入
    old_f = open(old_folder_name + "/" + file_name,"rb")
    content = old_f.read()
    old_f.close()
    # 打开新文件夹中的文件并写入
    new_f = open(new_floder_name + "/" + file_name,"wb")
    new_f.write(content)
    new_f.close()
    # 向队列中添加文件
    q.put(file_name)
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
    po = multiprocessing.Pool(5)
    # 创建队列
    q = multiprocessing.Manager().Queue()
    # 向进程池中添加任务
    for file_name in file_names:
        po.apply_async(copy,args=(q,file_name,old_folder_name,new_folder_name))
    po.close()
    # 测试文件夹中文件的个数
    all_num = len(file_names)
    # 已经复制的文件的个数
    copy_num = 0
    while True:
        # 从队列中获取文件
        a = q.get()
        print(a)
        copy_num += 1
        print("\r复制的进度为%.2f %%"%(copy_num*100/all_num),end="")
        if copy_num >= all_num:
            break
    print()
if __name__ == '__main__':
    main()