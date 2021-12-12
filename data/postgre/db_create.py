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
# Printing errors
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
# Closing connection
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")