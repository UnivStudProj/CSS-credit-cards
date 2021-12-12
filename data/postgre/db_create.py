import psycopg2
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
    
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE Cards(
                card_num varchar(6),
                image varchar(50),
                num_list varchar(50),
                card_holder varchar(50),
                card_date varchar(50),
                gradient varchar(50)
                );"""
        )
    
        print("[INFO] Table created successfully")
# Printing errors
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
# Closing connection
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")