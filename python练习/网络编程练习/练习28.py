import os
import multiprocessing


def copy_floder(q,temp,old_floder_name,new_floder_name):
    print("复制文件夹从%s到%s,文件名为:%s"%(old_floder_name,new_floder_name,temp))
    old_f = open(old_floder_name + "/" + temp,"rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_floder_name + "/" + temp,"wb")
    new_f.write(content)
    new_f.close()

    q.put(temp)

def main():
    old_floder_name = input("请输入要复制的文件夹:")
    try:
        new_floder_name = old_floder_name + "附件"
        os.mkdir(new_floder_name)
    except:
        pass
    file_names = os.listdir(old_floder_name)
    print(file_names)
    po = multiprocessing.Pool(3)
    q = multiprocessing.Manager().Queue()
    for temp in file_names:
        po.apply_async(copy_floder,args=(q,temp,old_floder_name,new_floder_name))
    all_file_num = len(file_names)
    done_num = 0
    while True:
        a = q.get()
        print(a)
        done_num += 1
        print("拷贝的进度为%.2f%%"%(done_num*100/all_file_num),end="")
        if done_num >= all_file_num:
            break
    print()

if __name__ == '__main__':
    main()