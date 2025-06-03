import mysql.connector
from config import db_config


def execute_sql_query(query):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    colums = [desc[0] for desc in cursor.description]
    conn.close()
    return colums, result