import os
import multiprocessing
def copy_file(q,file_name,old_floder_name,new_floder_name):
    '''完成文件复制'''
    old_f = open(old_floder_name +"/" + file_name,"rb")
    content = old_f.read()
    old_f.close()
    new_f = open(new_floder_name +"/" + file_name,"wb")
    new_f.write(content)
    new_f.close()
    # 如果拷贝完了文件,就向队列中写入一个信息,表示已经完成
    q.put(file_name)
def main():
    # 获取用户要复制的文件夹名字
    old_floder_name = input("请输入要复制的文件名字:")
    # 创建一个新的文件夹
    try:
        new_floder_name = old_floder_name + "[附件]"
        os.mkdir(new_floder_name)
    except:
        pass
    # 获取文件夹中所有要复制文件的名字
    file_names = os.listdir(old_floder_name)
    # print(file_names)
    # 创建线程池
    po = multiprocessing.Pool(5)
    # 创建一个队列
    q = multiprocessing.Manager().Queue() #方便将q作为参数传递到进程池
    # 向线程池里添加copy任务
    for file_name in file_names:
        po.apply_async(copy_file,args=(q,file_name,old_floder_name,new_floder_name))
    po.close()
    # 测一下所有文件个数
    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        copy_ok_num += 1
        print("\r拷贝的进度为%.2f%%"%(copy_ok_num*100/all_file_num),end="")
        if copy_ok_num >= all_file_num:
            break
    print()
if __name__ == '__main__':
    main()