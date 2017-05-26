import re
import urllib.request

request = urllib.request.Request('http://www.csdn.net')
resp = urllib.request.urlopen(request)
# <img src="http://images.csdn.net/20170525/bannerup.jpg">
list = re.findall(r'src="http:.+\.jpg"', resp.read().decode('utf-8'))


def download_image(url, position):
    data = urllib.request.urlopen(url)
    with open(str(position) + '.jpg', 'w') as file:
        file.write(data)
        file.flush()


i = 0
for item in list:
    sp = item.split("\"");
    download_image(sp[1], i)
    i += 1
