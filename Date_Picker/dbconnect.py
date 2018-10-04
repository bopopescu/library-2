import mysql.connector

cnx = mysql.connector.connect(user='root', password='Gt153328@', host='localhost', database='date_picker')


def insert(label, female):
    print("Label: ", label)
    try:
        cursor = cnx.cursor()
        query = "INSERT INTO user_choice(label, age, race, hair, eye, education, height, user_id, body_type) " \
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, (label, female.age, female.race, female.hair, female.eyes, female.education,
                               female.height, 1, female.body_type))
        cnx.commit()
        return True

    except Exception as e:
        return e


# get all data from user_choice table

def get_user_choice_data():
    try:
        cursor = cnx.cursor()
        query = "SELECT * FROM user_choice"
        cursor.execute(query)
        item = cursor.fetchall()
        cnx.commit()
        cnx.close()
        return item

    except Exception as e:
        return e

# reset user choice table
def truncate_user_choice_table():
    try:
        cursor = cnx.cursor()
        query = "TRUNCATE user_choice"
        cursor.execute(query)
        cnx.commit()
        return True

    except Exception as e:
        return e

