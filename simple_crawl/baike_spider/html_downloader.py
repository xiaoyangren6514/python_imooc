# encoding=utf8
import urllib.request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        request = urllib.request.Request(url)
        resp = urllib.request.urlopen(request)
        if resp.getcode() != 200:
            return None
        return resp.read()
