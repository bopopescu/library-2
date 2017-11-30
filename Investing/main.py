import nltk
import csv
from Investing.GDP import *


def main():

    file = open('/home/gary/demographic_data/GDP/GDP.csv', 'r')
    lines = file.read().split(';')
    path = '/home/gary/demographic_data/GDP/GDP.csv'
    gdp = GDP(path)
    gdplist = gdp.getGDP()
    print ("Country Code List")
    #gdp.getCountryCodes()
    #find a specific GDP
    country = gdp.find('USA')
    print('Specific Country: ',country)
    print('\n')
    value = gdp.gdpByValue(1000000)
    for i in value:
        print (i)

    print('\n'+'TOP')
    top = gdp.topGDP(.01)
    for t in top:
        print (t)


if __name__ == "__main__": main()