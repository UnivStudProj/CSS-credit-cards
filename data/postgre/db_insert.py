import psycopg2
import json
from config import host, user, password, db_name

# Connecting to postgreSQL
try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    
    connection.autocommit = True
    
    with open('data/cards.json') as f:
        jsn = json.load(f)
        for card in jsn:
            print(jsn[card]["num_list"][0])
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""INSERT INTO Cards (card_num, image, num_list, card_holder, card_date, gradient) VALUES
                    ('{card}', 
                    '{jsn[card]["image"]}', 
                    '{jsn[card]["num_list"]}', 
                    '{jsn[card]["card_holder"]}',
                    '{jsn[card]["card_date"]}',
                    '{jsn[card]["gradient"]}');"""
                )
        print("[INFO] Data was succesfully inserted")
# Printing errors
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
# Closing connection
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")