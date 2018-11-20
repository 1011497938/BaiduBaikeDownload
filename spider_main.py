# coding:utf-8
import url_manager, html_downloader, html_parser, html_outputer
import re
import sys
import time
import random
import traceback
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        depth = 0
        try_count = 0
        downLoadNum = 1
        self.urls.add_new_urls(root_url, depth)
        while self.urls.has_new_url():
            try:
                new_url, depth = self.urls.get_new_url()
                print('depth %d : %s' % (depth, new_url))
                html_cont = self.downloader.download(new_url)  #下载html页面
                # print(html_cont)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                
                if depth < 10:
                    self.urls.add_new_urls(new_urls, depth)

                self.outputer.output_text(new_data)
                print("已下载" + str(downLoadNum) + "/" + str(self.urls.get_new_url_num()) )
                downLoadNum += 1
                try_count = 0
                self.urls.finish_new_url(new_url)
                # if downLoadNum%300 == 0:
                #     time.sleep(random.uniform(60, 120))
                # time.sleep(random.uniform(0, 1))
            except BaseException:
                traceback.print_exc()
                try_count += 1
                if try_count<10:
                    print('craw failed, retry')
                    self.urls.add_new_urls([new_url], depth-1)
                else:
                    try_count = 0
                    # ffail.write(new_url + '\n')
                    print('craw failed')
        self.urls.finish()
        # self.outputer.output_html()


if __name__=='__main__':
    print('目前系统的编码为：',sys.getdefaultencoding())
    root_url = [ 'https://baike.baidu.com/item/%E5%AE%8B%E6%9C%9D/2919?fr=aladdin',
                 'https://baike.baidu.com/item/%E5%AE%8B%E4%BB%A3%E6%96%87%E5%AD%A6/2286985?fr=aladdin',
                 'https://baike.baidu.com/item/%E5%8D%97%E6%9C%9D%E5%AE%8B/913897'
                ] 
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
