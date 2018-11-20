# coding:utf-8
import urllib.request
from urllib.parse import quote
import socks
import socket
import string
import random


class HtmlDownloader(object):
    def download(self, url):
        def load_req(req): 
            PROXY_INFO = { 'host' : '127.0.0.1' , 'port' : 8118}
            proxy_support = urllib.request.ProxyHandler({"http" : "http://%(host)s:%(port)d" % PROXY_INFO})
            opener = urllib.request.build_opener(proxy_support,urllib.request.HTTPHandler) 
            urllib.request.install_opener(opener) 
            response = urllib.request.urlopen(req, timeout=5)
            if response.getcode() != 200:
                print("下载失败" )
                return None
            # print('下载成功')

            if random.randint(10,50)<11:
                ipcheck_url = 'http://checkip.amazonaws.com/'
                print('\n' + urllib.request.urlopen(ipcheck_url, timeout=2).read() + '\n')
            return response.read()

        def create_connection(address, timeout=None, source_address=None):
            sock = socks.socksocket()
            sock.connect(address)
            return sock

        # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050) #9050

        # # patch the socket module
        # socket.socket = socks.socksocket
        # socket.create_connection = create_connection

        # print("下载中")
        if url is None:
            return None
        url = quote(url,safe=string.printable)
        USER_AGENTS = [
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
        ]
    
        user_agent = random.choice(USER_AGENTS)
        headers = {
            "User-Agent": user_agent,
        }
        req = urllib.request.Request(url, headers=headers) #urlopen
        # response = urllib.request.urlopen(req, timeout=0.5)
        # if response.getcode() != 200:
        #     print("下载失败")
        #     return None
        # print('下载成功')

        # return response.read()
        return load_req(req) 
