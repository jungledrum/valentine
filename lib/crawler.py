# encoding=utf-8
import requests
import subprocess
import simplejson

def crawl(url):
    headers = {
        "Referer":"https://www.google.com.hk/", # 不加referer，淘宝不会跳转
        "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
    }
    resp = requests.head(url, headers=headers)

    if resp.status_code == 301:
        url = resp.headers.get('location', '')
    if resp.status_code == 200:
        url = resp.url
    print '>>> ', resp.status_code, url

    result = subprocess.Popen(['phantomjs','/home/bo/valentine/lib/crawler.js', url],stdout=subprocess.PIPE)
    line = result.stdout.read()
    product = simplejson.loads(line)
    return product


def test():
    url = 'http://item.taobao.com/item.htm?id=22349571247'
    print crawl(url)


if __name__ == "__main__":
    test()