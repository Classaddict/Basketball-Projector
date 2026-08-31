import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def connect():
    connection = psycopg2.connect(
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
    )
    return connection


def exec_commit(sql, params=None):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql, params)
    connection.commit()
    result = cursor.fetchall() if cursor.description else None
    cursor.close()
    connection.close()
    return result