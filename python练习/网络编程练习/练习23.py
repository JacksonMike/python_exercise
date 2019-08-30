import multiprocessing
def download(q):
    data = [11,22,33,44,55]
    for temp in data:
        q.put(temp)
    print("下载器已经下载完数据并且存放在队列中")
def deal(q):
    wait_data = list()
    while True:
        data = q.get()
        wait_data.append(data)
        if q.empty():
            break;
    print(wait_data)
def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=download,args=(q,))
    p2 = multiprocessing.Process(target=deal,args=(q,))
    p1.start()
    p2.start()
if __name__ == '__main__':
    main()