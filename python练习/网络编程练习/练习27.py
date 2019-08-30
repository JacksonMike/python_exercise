import multiprocessing
import os
def copy_floder(q,temp,old_floder_name,new_floder_name):

    old_f = open(old_floder_name + "/" + temp,"rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_floder_name + "/" + temp,"wb")
    new_f.write(content)
    new_f.close()

    q.put(temp)
def main():
    old_floder_name = input("请输入要复制的文件夹名字:")
    try:
        new_floder_name = old_floder_name + "附件"
        os.mkdir(new_floder_name)
    except:
        pass
    file_names = os.listdir(old_floder_name)

    po = multiprocessing.Pool(5)
    q = multiprocessing.Manager().Queue()
    for temp in file_names:
        po.apply_async(copy_floder,args=(q,temp,old_floder_name,new_floder_name))
    po.close()
    all_file_num = len(file_names)
    downloader_file_num = 0
    while True:
        temp = q.get()
        downloader_file_num += 1
        print("\r拷贝的进度为%.2f%%"%(downloader_file_num*100/all_file_num),end="")
        if downloader_file_num >= all_file_num:
            break
    print()
if __name__ == '__main__':
    main()