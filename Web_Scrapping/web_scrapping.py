#from lxml import html
import requests
import time
from threading import Thread
import datetime
import pprint
'''
class UpdateThread(Thread):

    def __init__(self, findMeACivic):
        self.findMeACivic = findMeACivic
        self.stopped = False
        Thread.__init__(self) # Call the super constructor (Thread's one)

    def run(self):
        while not self.stopped:
            self.downloadValue()
            time.sleep(10)

    def downloadValue(self):
        try:
            for civic in self.findMeACivic:
                page = requests.get(civic['url'])
                tree = html.fromstring(page.content)
                price = tree.xpath(civic['path'])
                print("Dealer: ", civic['company'])
                print('Model: %s | Year: %s | Trim: %s | Type: %s |' %(civic['model'], civic['year'], civic['trim'],civic['type']))
                print('Price: ', price[0])
        except Exception as e:
            print(e)


# {'company': ,'url':,'xpath':}
findMeACivic = [{'company': 'Toronto Honda',
                 'model': 'Honda Civic',
                 'year': '2019',
                 'trim': 'LX',
                 'type': 'Sedan',
                 'url': 'https://www.torontohonda.com/new/vehicle/2019-honda-civic-lx-id9047307.htm',
                 'path': '//*[@id="final-price"]/text()'},
                {'company': 'MidTown Honda',
                 'model': 'Honda Civic',
                 'year': '2019',
                 'trim': 'LX',
                 'type': 'Sedan',
                 'url': 'https://www.hondadowntown.ca/new/vehicle/2019-honda-civic-lx-id9062923.htm',
                 'path': '//*[@id="final-price"]/text()'},
                {'company': 'Classic Honda',
                 'model': 'Honda Civic',
                 'year': '2019',
                 'trim': 'LX',
                 'type': 'Sedan',
                 'url': 'https://www.classichonda.ca/new/Honda/2019-Honda-Civic-55ab9c4b0a0e0a172f9264f5a88bdd48.htm',
                 'path': '//*[@class="h1 price"]/text()'}
                ]

p = UpdateThread(findMeACivic)
p.downloadValue()


def test_scrap(url, path):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    price = tree.xpath(path)
    print(price)


url = 'https://www.walmart.ca/en/ip/huggies-snug-dry-diapers-economy-pack-size-1/6000197186351'
path = 'descendant-or-self::text()' #'//*[@class="price-current"]/div/text()'
test_scrap(url, path)
'''
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/home/gtohill/PythonProjects/PythonLibrary/Web_Scrapping/geckodriver32')
browser = webdriver.Firefox(firefox_binary=binary)

browser.get('http://www.garytohill.com')