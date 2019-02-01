from selenium import webdriver
import re

class SeleniumScrap:

    def __init__(self, path, xpath):
        self.binary = './geckodriver'
        browser = webdriver.Firefox(executable_path=self.binary)
        browser.get(path)
        pathtoprice = browser.find_element_by_xpath(xpath)
        st = pathtoprice.text
        self.price = self.getPrice(st)
        browser.close()

    def getPrice(self, a):
        p = a.split('.')
        st = ''
        x = 0
        while x < len(p):
            if x == 0:
                st = p[x].strip() + '.'
            else:
                st = st + p[x].strip()

            x += 1
        strip_price = re.sub('[^0-9|.]', '', st)
        price = strip_price.split('$')
        return(price)

'''
walmartpath = 'https://www.fortinos.ca/Food/Dairy-and-Eggs/Egg-%26-Egg-Substitutes/Whole-Eggs/Grade-A-White-Eggs%2C-Large/p/20812144001_EA'
walmartxpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div/div[2]/div[2]/div/ul[1]/li/span'


print(SeleniumScrap(walmartpath, walmartxpath).price)
'''