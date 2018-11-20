# coding:utf-8
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.htm
        links = soup.find_all('a', href=re.compile(r'/item/.*'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            # print(new_full_url)
            new_urls.add(new_full_url)
        # print(new_urls)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        
        res_data['content'] = ""
        try:
            # content_node = soup.find('div', class_='main-content')
            # if content_node is not None:
            #     res_data['content'] = content_node.get_Text()
            # else:
            content_nodes = soup.find_all('div', class_='para')
            res_data['content'] = "\n".join([node.get_text() for node in content_nodes if node is not None])
        except:
            print('content failed')
        # res_data['content'] = ""
        # print(res_data)
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')

        # 删除不用的内容
        classNames = ['before-content', 'side-content']  #'lemmaWgt-lemmaCatalog', 
        for className in classNames:
            shouldDeleteNodes =  soup.find_all('div',  class_ = className)
            for shouldDeleteNode in shouldDeleteNodes:
                shouldDeleteNode.extract()

        # print(soup.prettify().encode().decode('GBK', 'ignore'))
        new_urls = self._get_new_urls(page_url, soup)
        new_data = None
        try:
            new_data = self._get_new_data(page_url, soup)
        except:
            print("parse failed")
        # print('mark')
        return new_urls, new_data