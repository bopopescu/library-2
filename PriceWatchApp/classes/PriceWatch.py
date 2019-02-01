from SeleniumScrap import *


class PriceWatch:
    def __init__(self):
        self.db = {}

    def priceChange(self, company, product, price):

        if len(self.db) == 0:
            self.db.update({company: [product, price, price]})

        else:

            if company in self.db:
                item = self.db.get(company)
                currentprice = item[1]
                if currentprice > price:
                    newprice = currentprice - price
                    percentagechange = newprice/currentprice
                    if percentagechange > .1:
                        self.priceObserver(company, currentprice, price)

                    item[2] = price

            else:
                self.db.update({company: [product, price, price]})

    def priceObserver(self, company, currentprice, newprice):
        print('Lower Price for %s | Old price $%s | New Price $%s' % (company, currentprice, newprice))











'''
path = 'https://www.amazon.ca/All-new-Echo-Dot-3rd-gen/dp/B0792JYXZK/ref=br_msw_pdt-2?_encoding=UTF8&smid=A3DWYIK6Y9EEQB&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_s=&pf_rd_r=DAEDJ49683T9NAD3MK36&pf_rd_t=36701&pf_rd_p=d46e891e-1e72-45e4-8a59-cf31e1a9d6ed&pf_rd_i=desktop'
xpath = '//*[@id="priceblock_dealprice"]'

walmartpath = 'https://www.fortinos.ca/Food/Dairy-and-Eggs/Egg-%26-Egg-Substitutes/Whole-Eggs/Grade-A-White-Eggs%2C-Large/p/20812144001_EA'
walmartxpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div/div[2]/div[2]/div/ul[1]/li/span'


walmart = SeleniumScrap(walmartpath, walmartxpath)
print(walmart.price)
'''
'''
items = [('Walmart', 'Samsung 60 HDTV', 569),
         ('Amazon', 'Samsung 60 HDTV', 578),
         ('Target', 'Samsung 60 HDTV', 589),
         ('Walmart', 'Samsung 60 HDTV', 559),
         ('Amazon', 'Samsung 60 HDTV', 523),
         ('Target', 'Samsung 60 HDTV', 589),
         ('Walmart', 'Samsung 60 HDTV', 559),
         ('Amazon', 'Samsung 60 HDTV', 578),
         ('Target', 'Samsung 60 HDTV', 589),
         ('Walmart', 'Samsung 60 HDTV', 505),
         ('Amazon', 'Samsung 60 HDTV', 500),
         ('Target', 'Samsung 60 HDTV', 522)
         ]


p = PriceWatch()

for item in items:
    co = item[0]
    prod = item[1]
    pr = item[2]
    p.priceChange(co, prod, pr)
    '''