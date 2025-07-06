import seed  # assuming seed.py provides connect_to_prodev()

def stream_user_ages():
    """
    Generator that yields user ages one by one from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row[0]
    cursor.close()
    connection.close()

def compute_average_age():
    """
    Computes and prints the average age using the generator.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():  # Loop 1
        total_age += age
        count += 1

    average = total_age / count if count != 0 else 0
    print(f"Average age of users: {average:.2f}")
