import requests
# from lxml import etree


# url = 'http://detail.tmall.com/item.htm?id=22349571247&mt='
# r = requests.get(url)
# html = r.text

# # print html

# myparser = etree.HTMLParser(encoding="utf-8")
# tree = etree.HTML(html, parser=myparser)

# name = tree.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h3')[0].text
# price = tree.xpath('//*[@id="J_PromoPrice"]/div/span')
# images = tree.xpath('//*[@id="J_UlThumb"]/li[1]/a/img')[0].get('src')
# banner = tree.xpath('//*[@id="J_DetailMeta"]/div[1]/div[2]/div[1]/em')[0].text

# print name
# print price
# print images
# print banner

import subprocess
import simplejson

def crawl(url):
    # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
    res = requests.head(url)
    print '>>> ', url, res.status_code
    if res.status_code == 301:
        url = res.headers.get('location', '')

    result = subprocess.Popen(['phantomjs','/home/bo/valentine/lib/crawler.js', url],stdout=subprocess.PIPE)
    line = result.stdout.read()
    product = simplejson.loads(line)
    return product