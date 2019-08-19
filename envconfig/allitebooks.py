#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import os
import re
import requests
from hashlib import md5
from bs4 import BeautifulSoup
import  multiprocessing  as mp
import threading
import time
import queue
import json


# 定义一个变量， 保存爬取的结果

class SpiderBook():

    def __init__(self, pg_index, queue):
        # 爬取数据url
        self.base_url = 'http://www.allitebooks.org/page/{}/'
        # 存储json文件路径
        # 定义请求头部
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
            'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'www.allitebooks.org',
            'Referer': 'http://www.allitebooks.org/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/'
            '537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        # 需要爬取数据的总页数
        # self.pages = self.total_pages()
        # 页面索引
        self.pg_index = pg_index
        # 保存页面数据
        self.__queue = queue

    def total_pages(self):
        total_page_url = 'http://www.allitebooks.org/'
        phtml = requests.get(total_page_url, headers=self.headers).text
        # 获得页总数re表达式
        re_pages = re.compile(r'pages">1 / (\d+) Pages', re.S)

        return int(re_pages.search(phtml).group(1))

    def get_one_page(self):
        """get_page

        :param page_index: 第几页
        """
        try:
            url = self.base_url.format(self.pg_index)
            print("current page %d, %s" % (self.pg_index, url))

            response = requests.get(url, headers=self.headers)
            self.parse_html(response.text)
        except Exception as err:
            print(err)


    def parse_html(self, html):
        """parse_html

        :param html: 解释页面数据，提取book信息
        """
        soup = BeautifulSoup(html, 'html.parser')
        articles = soup.find_all('article')

        for article in articles:
            a_tag = article.find_all('a', attrs={'rel': 'bookmark'})
            name = a_tag[1].string if len(a_tag) >= 2 else ''
            img  = article.div.a.img['src'],

            author_tag = article.find_all('a', attrs={'rel': 'tag'})
            author = author_tag[0].string if len(author_tag) > 0 else ''

            summary_tag =  article.find_all('div', attrs={'class': 'entry-summary'})
            summary =  summary_tag[0].p.string if len(summary_tag) > 0 else ''

            self.__queue.put({
                'name': name,
                'img': img,
                'author': author,
                'summary': summary
            })



def save_to_local(books_lst):
    """save_local

    :param books: 以json格式保存到本地
    """
    # 获得保存数据的文件名
    fdump = os.path.join(os.getcwd(), 'books{}.json'.format(
        md5(str(time.time()).encode('utf-8')).hexdigest()))

    # 转换list to string
    books = json.dumps(
        books_lst,
        ensure_ascii=False,
        indent=4,
        sort_keys=True)

    with open(self.fdump, 'w',) as f:
        f.write(books)
        f.close()

# 定义爬取数据线程
class SpiderThread(threading.Thread):
    def __init__(self, q_jobs, q_res):
        """__init__

        :param q_jbos: 爬取总量
        :param q_res:  爬取的结果
        """
        threading.Thread.__init__(self)
        self.q_jobs = q_jobs
        self.q_res = q_res

    def run(self):
        #进入循环爬取所有页面数据
        while True:
            pg_index = self.q_jobs.get()
            s = SpiderBook(pg_index, self.q_res)
            s.get_one_page()
            # 通知队列
            self.q_jobs.task_done()


def main():
    # 启动爬取线程
    q_jobs = queue.Queue()
    q_res = queue.Queue()


    num_worker_threads = 8
    threads = [] 
    for _ in range(num_worker_threads):
        t = SpiderThread(q_jobs, q_res)
        t.setDaemon(True)
        t.start()
        threads.append(t)
    
    for i in range(1, 832):
        q_jobs.put(i)
    # 阻塞 主线程
    q_jobs.join()


    items = [item for item in q_res.get_nowait()]
    save_to_local(items)


     


def test_uint():

    pass

if __name__ == '__main__':
    # pool = Pool(10)
    # faild with pool.map
    # books_lst = pool.map_async(main, [ i for i in range(1, 832)])
    # s = SpiderBook()
    # s.save_to_local(books_lst)
    # test_uint()
    main()
