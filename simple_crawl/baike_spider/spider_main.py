# encoding=utf8
from simple_crawl.baike_spider import html_downloader
from simple_crawl.baike_spider import url_manager
from simple_crawl.baike_spider import html_parser
from simple_crawl.baike_spider import html_output


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count = count + 1
                if count == 5:
                    break
            except:
                print('craw fail')
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/android/60243'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
