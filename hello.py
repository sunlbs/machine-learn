import requests
import json
import os
import io
from bs4 import BeautifulSoup


# r = requests.get('http://www.mytxt.cc/read/3882/1495691.html')
#
# content = r.content
#
# html_doc = BeautifulSoup(content , "html.parser")
# document=html_doc.prettify()
# a = html_doc.body.find("div","button").find_all("a")[-1]['href']
# print(a)
# div = html_doc.find('body').find("div","detail_con_m62topxs")
# p = div.find("p")
#
#
# article = str(p.get_text())
# title =html_doc.body.find("h1").get_text()

class spider:
    __url__ = None
    __host__= None

    def __init__(self , host , url):
        self.__host__ = host
        self.__url__  = url
        self.execute()

    def execute(self):
        uri = self.getUri()
        r = requests.get(uri)
        allData = self.format(r)
        self.write(allData)
        # print(allData)
        while(allData['next'] != ''):
            uri = self.getUri()
            r = requests.get(uri)
            allData = self.format(r)
            self.setUrl(allData['next'])
            self.write(allData)

    def getUri(self):
        return self.__host__+self.__url__

    def getUrl(self):
        return self.__url__

    def setUrl(self , url):
        self.__url__ = url

    def format(self , rt):
        content = rt.content
        html_doc = BeautifulSoup(content , "html.parser")
        # document=html_doc.prettify()
        div = html_doc.find('body').find("div","detail_con_m62topxs")
        article = str(div.find("p").get_text())
        title =html_doc.body.find("h1").get_text()
        next = html_doc.body.find("div","button").find_all("a")[-1]['href']
        return {
            "title":title,
            "article":article,
            "next":next
        }

    def write(self,data):
        f = open('article_1', 'w+')
        f.write(json.dumps(data)+"\r\n")


spider = spider('http://www.mytxt.cc','/read/3882/1495691.html')
