from selenium import webdriver


def walmartScrape():
    binary = '../../classes/geckodriver'
    browser = webdriver.Firefox(executable_path=binary)
    try:
        browser.get('https://www.walmart.com/ip/3-Pack-Austin-Cookies-Crackers-Variety-Pack-1-38-8-count/830408055?athcpid=830408055&athpgid=athenaItemPage&athcgid=null&athznid=PWBAB&athieid=v0&athstid=CS020&athguid=bc385880-538-168a5a7755f676&athena=true')
        #pathtoprice = browser.find_element_by_xpath('//*[@class="price-group"]')
        #print(pathtoprice.text)
        p2p = browser.find_element_by_class_name('price-group')
        print(p2p.text)
        browser.close()
    except Exception as e:
        print(e)
        browser.close()

walmartScrape()