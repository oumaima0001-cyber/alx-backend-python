import mysql.connector

def stream_users():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_username',        # 🔁 replace with your MySQL username
            password='your_mysql_password',    # 🔁 replace with your MySQL password
            database='ALX_prodev'
        )

        cursor = connection.cursor(dictionary=True)  # fetch as dicts

        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row

        cursor.close()
        connection.close()
