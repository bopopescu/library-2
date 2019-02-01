from mysql.connector import connect


def select_all():
    cnx = connect(user='root', password='Gt153328@', host='localhost', database='pricewatch')
    cursor = cnx.cursor()
    query = ("SELECT DISTINCT company, product, url, path, xpath, base_price, current_price FROM WatchItem ORDER BY company")
    cursor.execute(query)
    items = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return items


def insert_contact(first, last, address, phone, email):
    cnx = connect(user='root', password='Gt153328@', host='localhost', database='exceldb')
    cursor = cnx.cursor()
    try:
        query = ("INSERT INTO Contact(firstname, lastname, address, phone, email) VALUES(%s,%s,%s,%s,%s)")
        insertUser = (first, last, address, phone, email)
        cursor.execute(query, insertUser)
        cnx.commit()
        cnx.close()
        return True

    except Exception as e:
        print(e)
        return False


def insert_rates(company, one, two, three, four, five):
    cnx = connect(user='root', password='Gt153328@', host='localhost', database='exceldb')
    cursor = cnx.cursor()
    try:
        query = ("INSERT INTO Rate(company, one, two, three, four, five) VALUES(%s,%s,%s,%s,%s,%s)")
        insert_rate = (company, one, two, three, four, five)
        cursor.execute(query, insert_rate)
        cnx.commit()
        cnx.close()
        return True

    except Exception as e:
        print(e)
        return False

    '''
def select(username):
    cnx = connect(user='root', password='Gt153328@', host='localhost', database='exceldb')
    cursor = cnx.cursor()
    usr = username
    query = ("SELECT * FROM Contact WHERE user_name = '%s' " %(usr))
    cursor.execute(query, usr)
    item = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return item


def create_user(user_name, password, root, email):
    cnx = mysql.connector.connect(user='root', password='Gt153328@', host='localhost', database='resume_screener')
    cursor = cnx.cursor()
    try:
        query = ("INSERT INTO User(user_name, password, root_folder, email) VALUES(%s,%s,%s,%s)")
        insertUser = (user_name, password, root, email)
        cursor.execute(query, insertUser)
        cnx.commit()
        cnx.close()
        return True

    except Exception as e:
        print(e)
        return False


def delete(user_name, user_id, email):
    try:
        cnx = mysql.connector.connect(user='root', password='Gt153328@', host='localhost', database='resume_screener')
        cursor = cnx.cursor()
        query = ("delete from User where user_name = %s AND user_id = %s AND email = %s")
        cursor.execute(query, (user_name, user_id, email))
        cnx.commit()
        cnx.close()
        return True

    except Exception as e:
        return False

def create_directory(search_name, user_id, file_location, search_criteria):
    try:
        cnx = mysql.connector.connect(user='root', password='Gt153328@', host='localhost', database='resume_screener')
        cursor = cnx.cursor()
        query = ("INSERT INTO SearchName(search_name, user_id, file_location, search_criteria) VALUES(%s,%s,%s,%s)")
        cursor.execute(query, (search_name, user_id, file_location, search_criteria))
        cnx.commit()
        cnx.close()
        return True

    except Exception as e:
        return False

#delete directory

def insertToDirectory(DirId, SubFolder, JobDescription):
    try:
        cnx = mysql.connector.connect(user='root', password='Gt153328@', host='localhost', database='resume_screener')
        cursor = cnx.cursor()
        query = "UPDATE Directory SET Job_Description = %s WHERE DirId = %s AND SubFolder = %s"
        cursor.execute(query, (JobDescription, DirId, SubFolder))
        cnx.commit()
        cnx.close()
        return True

    except Exception as e:
        return False

def directory_list(user_id):
    try:
        cnx = mysql.connector.connect(user='root', password='Gt153328@', host='localhost', database='resume_screener')
        cursor = cnx.cursor()
        query = ("SELECT search_id, file_location FROM SearchName WHERE user_id = %s ")
        cursor.execute(query, (user_id,))
        list = cursor.fetchall()
        cnx.commit()
        cnx.close()
        retList = []
        for i in list:
            retList.append(i)
        return retList

    except Exception as e:
        return e


def directory_job_description(search_id):
    try:
        cnx = mysql.connector.connect(user='root', password='Gt153328@', host='localhost', database='resume_screener')
        cursor = cnx.cursor()
        query = ("SELECT search_id, search_criteria FROM SearchName WHERE search_id = %s")
        cursor.execute(query, (search_id,))
        job_description = cursor.fetchall()
        cnx.commit()
        cnx.close()

        return job_description

    except Exception as e:
    '''