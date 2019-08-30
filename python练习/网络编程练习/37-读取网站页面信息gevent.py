import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def downloader(img_name,img_url):
    req = urllib.request.urlopen(img_url)
    image_content = req.read()
    with open(img_name, "wb") as f:
        f.write(image_content)
def main():
    gevent.joinall([gevent.spawn(downloader,"1.jpg","https://cs-op.douyucdn.cn/dycatr/game_cate/2a5909699afe89298bd2fde9c25d3407.jpg")
                    ,gevent.spawn(downloader,"11.jpg","https://cs-op.douyucdn.cn/dycatr/game_cate/b14b8890330ca7cb5185b954808485fc.jpg")])

if __name__ == '__main__':
    main()