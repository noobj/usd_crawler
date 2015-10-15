#!/usr/bin/python
__author__ = 'jjj'
# -*- coding:utf8 -*-
import urllib2
import re
from datetime import date
from time import sleep
from os.path import expanduser

class UsdCrawler:

    def getPage(self):
        try:
            url = 'https://www.taishinbank.com.tw/TS/TS06/TS0605/TS060502/index.htm?urlPath1=TS02&urlPath2=TS0202'
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "fuck u" + str(e.reason)
                return self.getPage()


    def start(self):
        pattern = re.compile('serif">.*?:(.*?)</FONT>.*?USD.*?center">(.*?)</td>', re.S)
        home = expanduser("~")
        filename = str(date.today())
        old = ""

        while True:
            pageCode = self.getPage()
            items = re.findall(pattern, pageCode)
            for i in items:
                if float(i[1]) > 33.0:
                    print "sell it!"

                if i[0] != old:
                    with open(home + "/USD/" + filename, "a") as f:
                        f.write(i[0] + " --- $" + i[1] + "\n")
            sleep(3)
            old = i[0]


if __name__ == "__main__":
    fucker = UsdCrawler()
    fucker.start()
