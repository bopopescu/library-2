from ParseExcel import *
from SeleniumScrap import *


# get excel spreadsheet
parsedExcel = ParseExcel('foodlist.xlsx')
# get all the sheet names
sheets = parsedExcel.getSheets()
# process data on each sheet
for sheet in sheets:
    parsedSheet = parsedExcel.getSheet(sheet)
    process = parsedExcel.getParsedExcelList(parsedSheet)
    for pro in process[1:]:
        product = SeleniumScrap(pro[2], pro[3])
        print(product.price[0])