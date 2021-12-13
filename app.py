import eel
import psycopg2
from data.postgre.config import host, user, password, db_name

eel.init("web")


# Request from js
@eel.expose
def call_from_js(card_n):
    # Connecting to postgreSQL
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        # Selecting card 
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT * FROM Cards WHERE card_num = 'card{card_n}';"""
            )
            row = cursor.fetchone()
            image = row[1]
            num = row[2].replace(' ', '').split(',')
            num[0] = num[0][1:]
            num[-1] = num[-1][:-1]
            card_holder = row[3]
            card_date = row[4]
            gradient = row[5]
    # Printing errors
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    # Closing connection
    finally:
        # Sending to js
        eel.call_to_js(image, num, card_holder, card_date, gradient)
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")
            
eel.start("index.html", size=(700, 700))