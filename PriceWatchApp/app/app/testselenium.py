from selenium import webdriver
import re


def app():
    binary = '../../classes/geckodriver'
    browser = webdriver.Firefox(executable_path=binary)
    try:
        browser.get('https://www.canadiantire.ca/en/pdp/permatex-blue-removable-strength-thread-locker-0383740p.html#spc')
        #pathtoprice = browser.find_element_by_xpath('//*[@class="price__reg-value"]')
        #print(pathtoprice.text)
        p2p = browser.find_element_by_class_name('price__total')
        print(p2p.text)
        browser.close()
    except Exception as e:
        print(e)
        browser.close()


def getPrice(a):
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


app()