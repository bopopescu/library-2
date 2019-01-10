import mysql.connector
from datetime import datetime, date, time


cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='priceapp')


#COMPANY RELATED QUERIES
#select a company
def select_retailer():
    try:
        cursor = cnx.cursor()
        query = ("SELECT * FROM retailer_link")
        cursor.execute(query)
        item = cursor.fetchall()
        cnx.commit()
        return item

    except Exception as e:
        return False

def add_retail_link(name, link):
    cursor = cnx.cursor()
    query = ("INSERT INTO retailer_link(name, link) VALUES(%s, %s)")
    insert = (name, link)
    cursor.execute(query, insert)
    cnx.commit()
    return True
