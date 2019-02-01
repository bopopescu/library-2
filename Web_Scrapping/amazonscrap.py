from selenium import webdriver
from lxml import html
from time import sleep
from selenium.webdriver.common.by import By

def manipstring(a):
    p = a.split('.')
    st = ''
    x = 0
    while x < len(p):
        if x == 0:
            st = p[x].strip() + '.'
        else:
            st = st + p[x].strip()

        x += 1
    price = st.split('$')
    return(float(price[1]))


binary = './geckodriver'
browser = webdriver.Firefox(executable_path=binary)
browser.get('https://www.amazon.ca/All-new-Echo-Dot-3rd-gen/dp/B0792JYXZK/ref=br_msw_pdt-2?_encoding=UTF8&smid=A3DWYIK6Y9EEQB&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_s=&pf_rd_r=DAEDJ49683T9NAD3MK36&pf_rd_t=36701&pf_rd_p=d46e891e-1e72-45e4-8a59-cf31e1a9d6ed&pf_rd_i=desktop')
login_form = browser.find_element_by_xpath('//*[@id="priceblock_dealprice"]')
st = login_form.text
print(st)
price = manipstring(st)
print(price)

browser.close()