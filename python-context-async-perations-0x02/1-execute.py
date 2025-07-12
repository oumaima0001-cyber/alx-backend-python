#!/usr/bin/env python3
import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=(), db_name='users.db'):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.conn = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result  # Return the result directly

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

# ✅ Use the context manager to execute a parameterized query
query = "SELECT * FROM users WHERE age > ?"
param = (25,)

with ExecuteQuery(query, param) as results:
    print(results)
