import multiprocessing
def down_from_web(q):
    '''下载数据'''
    # 模拟从网上下载的数据
    data = [1,2,3,4,5,6]
    # 向队列中下载数据
    for temp in data:
        q.put(temp)
    print("下载器已经下载完数据,并存在队列中.")
def analysis_data(q):
    '''数据处理'''
    # 从队列中获取数据
    wait_data = list()
    while True:
        data = q.get()
        wait_data.append(data)
        if q.empty():
            break
    # 模拟数据处理
    print(wait_data)
def main():
    # 创建一个队列
    q = multiprocessing.Queue()
    # 创建多个进程,将队列的引用作为实参传递到里面
    m1 = multiprocessing.Process(target=down_from_web,args=(q,))
    m2 = multiprocessing.Process(target=analysis_data,args=(q,))
    m1.start()
    m2.start()
if __name__ == '__main__':
    main()