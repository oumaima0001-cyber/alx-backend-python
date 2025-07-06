import mysql.connector
from mysql.connector import errorcode
import csv
import uuid

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_username',   # 🔁 replace with your MySQL user
            password='your_mysql_password'  # 🔁 replace with your MySQL password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_username',   # 🔁 same as above
            password='your_mysql_password',  # 🔁 same as above
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX(user_id)
            )
        """)
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = row.get("user_id") or str(uuid.uuid4())
                name = row["name"]
                email = row["email"]
                age = row["age"]

                # Avoid duplicate insert by checking user_id
                cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (user_id,))
                if not cursor.fetchone():
                    cursor.execute(
                        "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                        (user_id, name, email, age)
                    )
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}")
