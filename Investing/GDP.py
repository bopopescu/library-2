import csv


class GDP():

    def __init__(self, path):
        self.gdplist = list()

        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            globalGDP = 0
            for row in reader:
                num = row['Dollars']
                if num:
                    self.gdplist.append({'code': row['Code'], 'ranking': row['Ranking'], 'economy': row['Economy'],
                                    'gdp': row['Dollars']})

    def getGDP(self):
        return self.gdplist


    def getCountryCodes(self):
        for code in self.gdplist:
            print ('Code: ', code['code'], ' Country: ', code['economy'])


    #find GDP by country code
    def find(self, code):
        for item in self.gdplist:
            if item['code'] == code:
                return item

    #get GDP data based on value
    def gdpByValue(self, value):
        retlist = list()
        for item in self.gdplist:
            if int(item['gdp']) >= value:
                retlist.append(item)

        return retlist

    #return list of GDP by country if countries % of GDP is > than percent
    def topGDP(self, per):
        cutoff = per
        worldTotal = float()
        for item in self.gdplist:
            if item['code'] == 'WLD':
                worldTotal = float(item['gdp'])
        top = list()
        for item in self.gdplist:
            percent = float(item['gdp']) / float(worldTotal)
            if percent > cutoff:
                top.append(item)

        return top
