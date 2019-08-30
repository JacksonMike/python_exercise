import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def downloader(image_name,image_url):
    req = urllib.request.urlopen(image_url)
    content = req.read()
    with open(image_name,"wb") as f:
        f.write(content)
def main():
    gevent.joinall([gevent.spawn(downloader,"3.jpg","https://cs-op.douyucdn.cn/dycatr/game_cate/76a6d8b20e6c1a465c6f1bbedc35fd41.jpg"),
                    gevent.spawn(downloader,"4.jpg","https://cs-op.douyucdn.cn/dycatr/99ea1d4600ccd236ecebcf638709ee87.jpg")])
if __name__ == '__main__':
    main()