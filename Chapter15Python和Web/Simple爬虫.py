from urllib.request import urlopen
import re

p = re.compile('<a.*?><a .*? href="(.*?)">(.*?)</a>')
text = urlopen("https://www.sina.com.cn/").read().decode()
for url, name in p.findall(text):
    print('{}({})'.format(name, url))
