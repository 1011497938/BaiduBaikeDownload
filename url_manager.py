# coding:utf-8
import random
class UrlManager(object):
    def __init__(self):
        self.depth = {}
        self.new_urls = set()
        self.old_urls = set()

        new_urls = open('new.txt','r', encoding='utf-8').read().strip('\n').split('\n')
        old_urls = open('old.txt','r', encoding='utf-8').read().strip('\n').split('\n')
        for item in old_urls:
            item.replace('  ',' ')
            item = item.split(' ')
            if len(item) <= 1:
                continue
            url = item[0]
            depth = item[1]
            # print( url, depth)
            self.old_urls.add(url)
            self.depth[url] = int(depth)

        for item in new_urls:
            item.replace('  ',' ')
            item = item.split(' ')
            if len(item) <= 1:
                continue
            url = item[0]
            depth = item[1]
            if url not in self.old_urls:
                self.new_urls.add(url)
                # print( url, depth)
                self.depth[url] = int(depth)

        print(len(self.new_urls), len(self.old_urls))
    
    def _flush_new(self):
        fnew = open('new.txt','w', encoding='utf-8')
        for url in self.new_urls:
            fnew.write(url + ' ' + str(self.depth[url]) + '\n' )
        fnew.close()

    def _flush_old(self):
        self.fold = open('old.txt','w', encoding='utf-8')
        for url in self.old_urls:
            self.fold.write(url + ' ' + str(self.depth[url]) + '\n' )
        self.fold.close()

    def add_new_url(self, url, depth):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            self.depth[url] = depth + 1
        # else:
            # print('conflict')

    def add_new_urls(self, urls, depth):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url, depth)
        # self._flush_new()

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        # self.old_urls.add(new_url)
        return new_url, self.depth[new_url]

    def finish_new_url(self, new_url):
        if len(self.old_urls)%100==0:
            self._flush_new()
            self._flush_old()
        self.old_urls.add(new_url)

    def get_new_url_num(self):
        return len(self.new_urls)

    def finish(self):
        # return
        self._flush_new()
        self._flush_old()

    # def __del__(self):
    #     self.fold.close()