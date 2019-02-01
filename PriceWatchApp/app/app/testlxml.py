from lxml import html
import requests


def app():

    page = requests.get('https://brownsautosupply.com/product/05/3m08061/PLASTIC-EMBLEM-ADHESIVE-150-ML')
    tree = html.fromstring(page.content)
    #print(tree.text_content())
    #print(html.tostring(tree))
    regprice = tree.xpath('//span[@class="regular_price"]/text()')

    print(regprice)


app()