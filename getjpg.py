#coding=utf-8
import urllib
import re
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getCity(html):
    reg = r'href="http\:\/\/(.+?)\.meituan\.com".*?\>(.+?)\<\/a\>'
    urlre = re.compile(reg)
    buff = []
    urlList = re.findall(urlre, html).group(1)
    buff.append(urlList)
    writer = open('abc.txt', 'w')
    writer.write(str(urlList))
    writer.close()
    return urlList

html = getHtml('http://www.meituan.com/index/changecity/initiative')
print getCity(html)
