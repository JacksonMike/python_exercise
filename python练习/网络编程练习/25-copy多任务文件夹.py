import os
import multiprocessing
def copy_file(file_name,old_floder_name,new_floder_name):
    '''完成文件复制'''
    print("模拟文件复制,从%s到%s,文件名是%s"%(old_floder_name,new_floder_name,file_name))
    old_f = open(old_floder_name +"/" + file_name,"rb")
    content = old_f.read()
    old_f.close()
    new_f = open(new_floder_name +"/" + file_name,"wb")
    new_f.write(content)
    new_f.close()
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
    print(file_names)
    # 创建线程池
    po = multiprocessing.Pool(5)
    # 向线程池里添加copy任务
    for file_name in file_names:
        po.apply_async(copy_file,args=(file_name,old_floder_name,new_floder_name))
    po.close()
    po.join()
if __name__ == '__main__':
    main()