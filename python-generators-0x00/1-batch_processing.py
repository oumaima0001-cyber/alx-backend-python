import mysql.connector

def connect_to_prodev():
    return mysql.connector.connect(
        host='localhost',
        user='your_mysql_username',     # 🔁 Change this
        password='your_mysql_password', # 🔁 Change this
        database='ALX_prodev'
    )

def stream_users_in_batches(batch_size):
    """
    Generator that fetches rows from the database in batches.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    offset = 0

    while True:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))
        batch = cursor.fetchall()
        if not batch:
            break
        yield batch
        offset += batch_size

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """
    Processes each batch and prints users with age > 25.
    """
    for batch in stream_users_in_batches(batch_size):           # 1 loop
        for user in batch:                                      # 2nd loop
            if user["age"] > 25:
                print(user)                                     # yield could also be used
