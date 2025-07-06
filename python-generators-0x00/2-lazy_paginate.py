import seed  # assumes seed.py has connect_to_prodev()

def paginate_users(page_size, offset):
    """
    Fetch a page of users from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def lazy_pagination(page_size):
    """
    Generator that lazily fetches paginated data one page at a time.
    """
    offset = 0
    while True:  # This is the **one allowed loop**
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
