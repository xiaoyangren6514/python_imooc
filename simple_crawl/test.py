import urllib.request
import http.cookiejar

url = 'http://www.baidu.com'

def test01():
    resp = urllib.request.urlopen('http://www.baidu.com')
    print(resp.getcode())

def test02():
    data = {
        'a':1,
        'b':'1'
    }
    request = urllib.request.Request(url,data=None,headers={})
    resp = urllib.request.urlopen(request)
    print(resp.getcode())

def test03():
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    resp = urllib.request.urlopen(url)
    print(resp.getcode())

test02()
test03()