from lxml import html
import requests
import time
from threading import Thread
import datetime


class UpdateThread(Thread):

    def __init__(self):
        self.stopped = False
        Thread.__init__(self) # Call the super construcor (Thread's one)

    def run(self):
        while not self.stopped:
            self.downloadValue()
            time.sleep(10)

    def downloadValue(self):
        page = requests.get('https://bagreligion.com/product/prada-saffiano-lux-galleria-double-zip-tote/')
        # page = requests.get('http://www.home-tyme.com/product/bacon-wrapped-scallops/')
        tree = html.fromstring(page.content)
        price = tree.xpath('//p/ins/span[@class="woocommerce-Price-amount amount"]/text()')
        return price[0]

"""
myThread = UpdateThread()
myThread.start()

for i in range(10):
    print("Getting Price...")
    now = datetime.datetime.now()
    print(now.date())
    time.sleep(10)
"""
