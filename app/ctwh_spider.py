import requests
import os
import re
from bs4 import BeautifulSoup
from models import Spider


class CtwhSpider:  # 传统文化网站爬取文章信息

    def __init__(self):
        # 爬取的url
        self.url_temp = "https://www.zhwh365.com/article_{}.html"
        # 伪装头部，谷歌浏览器
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

    def get_url_list(self):
        # 生成爬取文章url列表
        return [self.url_temp.format(i) for i in range(28, 50)]

    def pares_url(self, url):
        # 发送请求
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def parse_html(self, html_str):
        # 解析网页，存储文章内容
        list = []
        soup = BeautifulSoup(html_str, "lxml")
        tit = soup.find("span", attrs="tname")
        t = soup.find("span", attrs="tsj")
        data = re.findall(r'\d{4}-\d{1,2}-\d{1,2}', t.string)
        tex = soup.find("div", attrs="mlneirong")
        title = tit.string
        text = tex.text
        list.extend((title, data[0], text))
        return list

    def save_text(self, list):
        # 保存到本地
        path = "E://spiders//ctwh//"
        global article_count  # 使用全局变量，需要在函数中进行标识
        # 获取当前目录文件，截取目录后，并自动创建文件
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            filename = list[0] + '.txt'
            with open(path + filename, 'w', encoding='utf-8') as f:
                f.write(list[2])  # 正文写入文件
                article_count += 1  # 计数变量加1，统计总的下载文件数
        except:
            pass
        print(list[0] + "-->文章保存完毕")  # 提示文章下载完毕

    def save_mysql(self, list, url):
        article = Spider()
        article.status = 1
        article.title = list[0]
        article.time = list[1]
        article.address = "E://spiders//ctwh//" + list[0] + '.txt'
        article.website = url

    def run(self):
        # 主体运行
        url_list = self.get_url_list()
        for url in url_list:
            try:
                html_str = self.pares_url(url)
                list = self.parse_html(html_str)
                self.save_text(list)
                self.save_mysql(list, url)
            except:
                continue


if __name__ == '__main__':
    spider = CtwhSpider()
    spider.run()
