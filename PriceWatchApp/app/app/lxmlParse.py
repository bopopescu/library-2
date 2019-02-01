from lxml import html
import requests
from openpyxl import load_workbook


def app():

    # get excel spreadsheet
    wb = load_workbook('../../classes/foodlist.xlsx')
    nofrills = wb['NoFrills']
    i = 0
    for row in nofrills.rows:
        if i > 0:
            print(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value)
            print("Category: " , row[0].value)
            print("Product Name: ", row[1].value)

            page = requests.get(row[2].value)
            tree = html.fromstring(page.content)
            regprice = tree.xpath(row[3].value)
            saleprice = tree.xpath(row[4].value)
            oldprice = tree.xpath(row[5].value)

            if len(regprice) == 0:
                print('Sale Price: ', saleprice[0])
                print('Old Price: ', oldprice[0])
            else:
                print('Reg. Price: ', regprice[0])
        i += 1
        print()




app()