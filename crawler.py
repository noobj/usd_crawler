#!/usr/bin/python
__author__ = 'jjj'
# -*- coding:utf8 -*-
import urllib2
import re
from datetime import date
from time import sleep
from os.path import expanduser
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import math
import numpy as np

# use ~ as home directory
home = expanduser("~")
# set today as the filename
filename = str(date.today())

# draw the price-time pic
class Drawer:
    # entry point of Class
    def draw(self):
        # store the prices
        numbers = []
    
        with open(home + "/USD/" + filename, "r") as f:
            text = f.readlines()
            for i in text:
                j = i.split()
                k = float(j[3].strip("$"))
                numbers.append(k)
    
        lenth = len(numbers)
    
        x = np.linspace(0, 12, lenth)
        plt.figure(figsize=(8,4))
        plt.plot(x, numbers, lw=2)
        plt.ylim(round(min(numbers), 2), round(max(numbers), 2))
        plt.xlabel("time")
        plt.ylabel("price")
        plt.title("USD price")
        plt.savefig("fuck.jpg", dpi=300, format="jpg") 


# crawl Usd to Twd price from Taishin Bank
class UsdCrawler:
    # get page context
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

    # entry point
    def start(self):
        pattern = re.compile('serif">.*?:(.*?)</FONT>.*?USD.*?center">(.*?)</td>', re.S)
        # store the older update time
        old = ""
        drawer = Drawer()

        while True:
            pageCode = self.getPage()
            items = re.findall(pattern, pageCode)
            for i in items:
                # if price greater then $33, alert me to sell it!
                if float(i[1]) > 33.0:
                    print "sell it!"

                # if there is difference in update time, write it to file
                if i[0] != old:
                    with open(home + "/USD/" + filename, "a") as f:
                        f.write(i[0] + " --- $" + i[1] + "\n")
                    drawer.draw()
            sleep(3)
            old = i[0]


if __name__ == "__main__":
    fucker = UsdCrawler()
    fucker.start()
