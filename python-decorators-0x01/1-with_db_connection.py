#!/usr/bin/env python3
import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # ✅ Open connection
        try:
            return func(conn, *args, **kwargs)  # ✅ Pass conn as first argument
        finally:
            conn.close()  # ✅ Always close connection
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# ✅ Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)
