#!/usr/bin/python
__author__ = 'jjj'
# -*- coding:utf8 -*-
import urllib2
import re
from datetime import date
from time import sleep
from os.path import expanduser

class UsdCrawler:

    def start(self):
        url = 'https://www.taishinbank.com.tw/TS/TS06/TS0605/TS060502/index.htm?urlPath1=TS02&urlPath2=TS0202'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        pageCode = response.read().decode('utf-8')
        pattern = re.compile('serif">.*?:(.*?)</FONT>.*?USD.*?center">(.*?)</td>', re.S)
        home = expanduser("~")
        filename = str(date.today())

        while True:
            items = re.findall(pattern, pageCode)
            for i in items:
                with open(home + "/USD/" + filename, "a") as f:
                    f.write(i[0] + " --- $" + i[1] + "\n")
            sleep(600)


if __name__ == "__main__":
    fucker = UsdCrawler()
    fucker.start()
