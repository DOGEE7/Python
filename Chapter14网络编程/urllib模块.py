from urllib.request import urlopen
import re

webpage = urlopen("https://www.sina.com.cn/")
text = webpage.read()
m = re.search(b'<a href="([^"]+).*?>about</a>', text, re.IGNORECASE)
# m.group(1)
print(m)